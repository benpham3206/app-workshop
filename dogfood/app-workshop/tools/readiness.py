#!/usr/bin/env python3
"""Check a generated app's structure and show which planning decisions remain open."""

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


SECRET_NAMES = (
    ".env", ".env.*", "*.env", "*.p8", "*.p12", "*.pfx", "*.pem", "*.key",
    "*.mobileprovision", "*.provisionprofile", "id_rsa", "id_ed25519",
)
SECRET_EXAMPLES = (".env.example", "example.env", "*.env.example", "*.example.env")
PRIVATE_KEY_HEADER = re.compile(rb"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----")
REVENUECAT_SECRET = re.compile(rb"(?<![A-Za-z0-9_])sk_[A-Za-z0-9_]{16,}")


REQUIRED = (
    "AGENTS.md", "PRINCIPLES.md", "README.md", "Makefile",
    "docs/BEGINNER-GUIDE.md", "docs/product/BRIEF.md", "docs/ux/FLOWS.md",
    "docs/design/IDENTITY.md", "docs/design/NATIVE-REVIEW.md",
    "docs/design/APP-ICON.md", "docs/compatibility/REVIEW.md", "docs/quality/TEST-MATRIX.md",
    "docs/ux/patterns/ONBOARDING.md", "docs/ux/patterns/PERMISSIONS.md",
    "docs/ux/patterns/SETTINGS-AND-HELP.md",
    "docs/quality/GLASS-AND-PERFORMANCE.md", "docs/release/CHECKLIST.md",
    "design/identity/RECIPE.md", "design/icon-brief.json",
    "tools/icon_plan.py", "tools/readiness.py", "resources/process.json",
)
DECISIONS = (
    "docs/product/BRIEF.md", "docs/design/IDENTITY.md",
    "docs/design/NATIVE-REVIEW.md", "docs/engineering/PROJECT-SETUP.md",
    "docs/quality/TEST-MATRIX.md",
)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
TOKEN = re.compile(r"\{\{[A-Z_]+\}\}")


def inspect(root):
    errors = []
    pending = []
    manifest_path = root / ".apple-scaffold.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        selection = manifest["selection"]
        if not isinstance(selection, dict):
            raise ValueError("selection is not an object")
        for field in ("identity", "platforms", "modules"):
            if field not in selection:
                raise ValueError(f"selection is missing {field}")
        if not isinstance(selection["identity"], str) or not isinstance(selection["platforms"], list) or not isinstance(selection["modules"], list):
            raise ValueError("selection has invalid types")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f".apple-scaffold.json: {exc}")
        selection = None

    paths = list(REQUIRED)
    if selection:
        if not selection["platforms"]:
            errors.append("selection has no platforms")
        for item in selection["platforms"]:
            if isinstance(item, str) and re.fullmatch(r"[a-z0-9-]+", item):
                paths.append(f"platforms/{item}/PROFILE.md")
            else:
                errors.append("selection has an invalid platform path")
        for item in selection["modules"]:
            if isinstance(item, str) and re.fullmatch(r"[a-z0-9-]+", item):
                paths.append(f"modules/{item}/CONTRACT.md")
            else:
                errors.append("selection has an invalid module path")
    for relative in paths:
        if not (root / relative).is_file():
            errors.append(f"Missing {relative}")

    documents = list(root.glob("*.md"))
    for folder in ("docs", "design", "platforms", "modules"):
        source = root / folder
        if source.is_dir():
            documents.extend(source.rglob("*.md"))
    for path in documents:
        relative = path.relative_to(root)
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {relative}: {exc}")
            continue
        if TOKEN.search(content):
            errors.append(f"Unresolved template token in {relative}")
        for target in LINK.findall(content):
            parts = target.strip().split()
            if not parts:
                errors.append(f"Empty link in {relative}")
                continue
            target = parts[0]
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            destination = unquote(target.split("#", 1)[0])
            if destination and not (path.parent / destination).resolve().exists():
                errors.append(f"Broken link in {relative}: {target}")
    errors.extend(tracked_secrets(root))
    for relative in DECISIONS:
        path = root / relative
        if path.is_file() and re.search(r"\bPending\b", path.read_text(encoding="utf-8"), re.IGNORECASE):
            pending.append(relative)
    return errors, pending


def tracked_secrets(root):
    """Reject tracked signing assets and private-key or secret-key content."""
    try:
        top = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True).stdout.strip()
        if Path(top).resolve() != root:
            return []
        listed = subprocess.run(["git", "-C", str(root), "ls-files", "-z"],
                                capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return []
    found = []
    for path in filter(None, listed.split("\0")):
        name = path.rsplit("/", 1)[-1]
        if not any(fnmatch.fnmatch(name, pattern) for pattern in SECRET_EXAMPLES) and any(fnmatch.fnmatch(name, pattern) for pattern in SECRET_NAMES):
            found.append(f"Secret or signing file is tracked by Git: {path}")
        tracked = root / path
        if tracked.is_symlink() or not tracked.is_file():
            continue
        try:
            content = tracked.read_bytes()
        except OSError as exc:
            found.append(f"Cannot scan tracked file {path}: {exc}")
            continue
        if PRIVATE_KEY_HEADER.search(content) or REVENUECAT_SECRET.search(content):
            found.append(f"Private key or secret token is tracked by Git: {path}")
    return found


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true", help="also fail when tracked planning decisions remain pending")
    args = parser.parse_args(argv)
    root = args.project.resolve()
    errors, pending = inspect(root)
    if errors:
        print("Structure: FAIL")
        for issue in errors:
            print(f"  - {issue}")
    else:
        print("Structure: PASS")
    if pending:
        print("Planning decisions still pending:")
        for path in pending:
            print(f"  - {path}")
    else:
        print("Tracked planning decisions: no Pending markers")
    print("This check does not verify a build, native design quality, or release readiness.")
    return 2 if errors else (1 if args.strict and pending else 0)


if __name__ == "__main__":
    sys.exit(main())
