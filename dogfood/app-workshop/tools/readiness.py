#!/usr/bin/env python3
"""Check a generated app's structure and show which planning decisions remain open."""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


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
    for relative in DECISIONS:
        path = root / relative
        if path.is_file() and re.search(r"\bPending\b", path.read_text(encoding="utf-8"), re.IGNORECASE):
            pending.append(relative)
    return errors, pending


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
