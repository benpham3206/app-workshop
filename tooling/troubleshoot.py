#!/usr/bin/env python3
"""Generate a likely-failure checklist for a selected Apple app scaffold."""

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "config" / "troubleshooting.json"


def build_guide(config):
    catalog = json.loads(RULES.read_text(encoding="utf-8"))
    selected_platforms = set(config["platforms"])
    selected_modules = set(config["modules"])
    lines = [
        "# Likely failures and first checks",
        "",
        f"Generated for **{config['project']['name']}**. These are hypotheses to investigate, "
        "not diagnoses. Recheck linked Apple guidance when implementing a capability.",
        "",
        "## Use this guide",
        "",
        "1. Reproduce the symptom and record OS, device, build, account, and network state.",
        "2. Follow the checks for the matching symptom; preserve the exact error or log.",
        "3. Add the confirmed cause, fix, and regression check to the project issue or support note.",
        "4. If the cause is in Apple's code, reduce it to a sample project, file it in "
        "[Feedback Assistant](https://developer.apple.com/bug-reporting/), and record the FB number "
        "beside the workaround.",
        "",
    ]
    for rule in catalog["rules"]:
        if rule["platforms_any"] and not selected_platforms.intersection(rule["platforms_any"]):
            continue
        if rule["modules_any"] and not selected_modules.intersection(rule["modules_any"]):
            continue
        lines.extend([f"## {rule['title']}", "", f"**Symptom:** {rule['symptom']}", "", "First checks:", ""])
        lines.extend(f"- {check}" for check in rule["checks"])
        lines.extend(["", f"Apple reference: {rule['source']}", ""])
    return "\n".join(lines).rstrip() + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output", type=Path, help="Write the guide to a file; otherwise print it")
    args = parser.parse_args(argv)
    from scaffold import ScaffoldError, load_config

    try:
        guide = build_guide(load_config(args.config))
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(guide, encoding="utf-8")
            print(f"Generated {args.output}")
        else:
            print(guide, end="")
    except (ScaffoldError, OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
