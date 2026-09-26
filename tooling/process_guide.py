#!/usr/bin/env python3
"""Validate the beginner journey and render it as a readable guide."""

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "config" / "process.json"
PHASE_FIELDS = {"id", "title", "goal", "actions", "output", "failure", "recovery", "reference"}


class ProcessError(Exception):
    pass


def load_process(path=SOURCE):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ProcessError(f"Cannot read process: {exc}") from exc
    if not isinstance(data, dict) or set(data) != {"version", "title", "introduction", "phases"}:
        raise ProcessError("Process needs version, title, introduction, and phases")
    if type(data["version"]) is not int or data["version"] != 2:
        raise ProcessError("Unsupported process version")
    if not all(isinstance(data[key], str) and data[key].strip() for key in ("title", "introduction")):
        raise ProcessError("Process title and introduction must be nonempty")
    phases = data["phases"]
    if not isinstance(phases, list) or not phases:
        raise ProcessError("Process needs phases")
    seen = set()
    action_ids = set()
    for index, phase in enumerate(phases, 1):
        if not isinstance(phase, dict) or set(phase) != PHASE_FIELDS:
            raise ProcessError(f"Phase {index} has missing or unknown fields")
        if not all(isinstance(phase[key], str) and phase[key].strip() for key in PHASE_FIELDS - {"actions"}):
            raise ProcessError(f"Phase {index} has an empty text field")
        if not isinstance(phase["actions"], list) or not phase["actions"]:
            raise ProcessError(f"Phase {index} needs concrete actions")
        for action in phase["actions"]:
            if not isinstance(action, dict) or set(action) != {"id", "text"} or not all(
                isinstance(action[key], str) and action[key].strip() for key in ("id", "text")
            ):
                raise ProcessError(f"Phase {index} has an invalid action")
            if action["id"] in action_ids:
                raise ProcessError(f"Duplicate action id: {action['id']}")
            action_ids.add(action["id"])
        if phase["id"] in seen:
            raise ProcessError(f"Duplicate phase id: {phase['id']}")
        seen.add(phase["id"])
        if not phase["reference"].startswith("https://developer.apple.com/"):
            raise ProcessError(f"Phase {index} needs an Apple Developer reference")
    return data


def render_guide(process):
    lines = [f"# {process['title']}", "", process["introduction"], "", "## Route", ""]
    for index, phase in enumerate(process["phases"], 1):
        lines.append(f"{index}. [{phase['title']}](#{index}-{phase['title'].lower().replace(' ', '-')})")
    lines.append("")
    for index, phase in enumerate(process["phases"], 1):
        lines.extend([
            f"## {index}. {phase['title']}", "",
            f"**Aim:** {phase['goal']}", "",
            "Do this:", "",
        ])
        lines.extend(f"- {action['text']}" for action in phase["actions"])
        lines.extend([
            "", f"**Move on when:** {phase['output']}", "",
            f"**What can go wrong:** {phase['failure']}", "",
            f"**If blocked:** {phase['recovery']}", "",
            f"[Apple reference]({phase['reference']})", "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        guide = render_guide(load_process(args.source))
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(guide, encoding="utf-8")
            print(f"Generated {args.output}")
        else:
            print(guide, end="")
    except (ProcessError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
