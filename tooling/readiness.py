#!/usr/bin/env python3
"""Check a generated app's structure and links, and report its explicit gates."""

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


GATES = "docs/quality/gates.json"
STATUSES = ("open", "done")
REQUIRED = (
    "AGENTS.md", "PRINCIPLES.md", "README.md", "Makefile",
    "docs/BEGINNER-GUIDE.md", "docs/product/BRIEF.md", "docs/ux/FLOWS.md",
    "docs/design/IDENTITY.md", "docs/design/NATIVE-REVIEW.md",
    "docs/design/APP-ICON.md", "docs/compatibility/REVIEW.md", "docs/quality/TEST-MATRIX.md",
    "docs/ux/patterns/ONBOARDING.md", "docs/ux/patterns/PERMISSIONS.md",
    "docs/ux/patterns/SETTINGS-AND-HELP.md",
    "docs/quality/GLASS-AND-PERFORMANCE.md", "docs/release/CHECKLIST.md",
    "docs/engineering/SECURE-FAST-DEFAULTS.md",
    "design/identity/RECIPE.md", "design/icon-brief.json",
    "tools/icon_plan.py", "tools/readiness.py", "resources/process.json",
    GATES,
)
SECRET_NAMES = (
    ".env", ".env.*", "*.env", "*.p8", "*.p12", "*.pfx", "*.pem", "*.key",
    "*.mobileprovision", "*.provisionprofile", "id_rsa", "id_ed25519",
)
SECRET_EXAMPLES = (".env.example", "example.env", "*.env.example", "*.example.env")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
TOKEN = re.compile(r"\{\{[A-Z_]+\}\}")


def inspect(root):
    errors = []
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
        if "ios" in selection["platforms"]:
            paths.append("docs/compatibility/IPHONE-DUO.md")
        if manifest.get("starter") == "ios":
            paths.extend(("App.xcodeproj/project.pbxproj", "scripts/simulator.sh", "starter.mk"))
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
    gates = read_gates(root, errors)
    return errors, gates


def tracked_secrets(root):
    """Signing keys, certificates, profiles, and env files must never be tracked by Git."""
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
        if any(fnmatch.fnmatch(name, pattern) for pattern in SECRET_EXAMPLES):
            continue
        if any(fnmatch.fnmatch(name, pattern) for pattern in SECRET_NAMES):
            found.append(f"Secret or signing file is tracked by Git: {path}")
    return found


def read_gates(root, errors):
    """Return [(id, question, status)]. A done gate without existing evidence is a structure error."""
    try:
        data = json.loads((root / GATES).read_text(encoding="utf-8"))
        items = data["gates"]
        if not isinstance(items, list):
            raise TypeError("gates is not an array")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"{GATES}: {exc}")
        return []
    gates = []
    for index, gate in enumerate(items):
        where = f"{GATES} gate {index + 1}"
        if not isinstance(gate, dict) or not all(isinstance(gate.get(key), str) for key in ("id", "question", "status")):
            errors.append(f"{where}: needs string id, question, and status")
            continue
        evidence = gate.get("evidence", [])
        if gate["status"] not in STATUSES:
            errors.append(f"{where} ({gate['id']}): status must be one of {', '.join(STATUSES)}")
        elif not isinstance(evidence, list) or not all(isinstance(item, str) for item in evidence):
            errors.append(f"{where} ({gate['id']}): evidence must be an array of paths")
        elif gate["status"] == "done":
            if not evidence:
                errors.append(f"{where} ({gate['id']}): done needs at least one evidence path")
            for item in evidence:
                if not (root / item).exists():
                    errors.append(f"{where} ({gate['id']}): evidence not found: {item}")
        gates.append((gate["id"], gate["question"], gate["status"]))
    return gates


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true", help="also fail while any gate in docs/quality/gates.json is open")
    args = parser.parse_args(argv)
    root = args.project.resolve()
    errors, gates = inspect(root)
    if errors:
        print("Structure: FAIL")
        for issue in errors:
            print(f"  - {issue}")
    else:
        print("Structure: PASS")
    open_gates = [gate for gate in gates if gate[2] != "done"]
    print(f"Gates: {len(gates) - len(open_gates)} of {len(gates)} done ({GATES})")
    for gate_id, _, status in gates:
        print(f"  [{'x' if status == 'done' else ' '}] {gate_id}")
    if open_gates:
        print(f"Next: {open_gates[0][0]} - {open_gates[0][1]}")
    print("A done gate is only as true as its evidence files. This check does not run a build or approve a release.")
    return 2 if errors else (1 if args.strict and open_gates else 0)


if __name__ == "__main__":
    sys.exit(main())
