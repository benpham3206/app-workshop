#!/usr/bin/env python3
"""Turn a completed app icon brief into concept prompts and a production checklist."""

import argparse
import json
import sys
from pathlib import Path


class IconBriefError(Exception):
    pass


def _nonempty(value, field):
    if not isinstance(value, str) or not value.strip():
        raise IconBriefError(f"{field} needs a real product decision")
    return value.strip()


def load_brief(path):
    try:
        brief = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise IconBriefError(f"Cannot read icon brief: {exc}") from exc
    required = {"schema_version", "app_name", "identity", "platforms", "product_promise", "visual_motifs", "avoid"}
    if not isinstance(brief, dict) or set(brief) != required:
        raise IconBriefError("Icon brief has missing or unknown fields")
    if type(brief["schema_version"]) is not int or brief["schema_version"] != 1:
        raise IconBriefError("Unsupported icon brief version")
    _nonempty(brief["app_name"], "app_name")
    _nonempty(brief["product_promise"], "product_promise")
    if not isinstance(brief["identity"], str) or brief["identity"] not in {"playful-kinetic", "calm-precise", "dark-technical"}:
        raise IconBriefError("Unknown identity")
    if not isinstance(brief["platforms"], list) or not brief["platforms"] or any(
        not isinstance(item, str) or item not in {"ios", "ipados", "macos", "watchos", "tvos", "visionos"} for item in brief["platforms"]
    ):
        raise IconBriefError("Select at least one supported platform")
    if not isinstance(brief["visual_motifs"], list) or not 1 <= len(brief["visual_motifs"]) <= 5 or any(
        not isinstance(item, str) or not item.strip() for item in brief["visual_motifs"]
    ):
        raise IconBriefError("visual_motifs needs one to five meaningful ideas")
    if not isinstance(brief["avoid"], list) or any(not isinstance(item, str) for item in brief["avoid"]):
        raise IconBriefError("avoid must be a list of strings")
    return brief


def build_plan(brief):
    name = brief["app_name"].strip()
    promise = brief["product_promise"].strip()
    motifs = [item.strip() for item in brief["visual_motifs"]]
    avoid = [item.strip() for item in brief["avoid"] if item.strip()]
    constraints = "; ".join(avoid) if avoid else "No additional product-specific exclusions recorded."
    platform_names = ", ".join(brief["platforms"])
    directions = [
        ("Single symbol", f"Distill {motifs[0]} into one unmistakable silhouette."),
        ("Relationship", f"Show a clear visual relationship between {motifs[0]} and {motifs[-1]}."),
        ("Distinctive geometry", f"Abstract {', '.join(motifs)} into a simple geometric mark."),
    ]
    lines = [
        f"# Icon concept plan: {name}", "",
        f"**Product promise:** {promise}",
        f"**Identity:** {brief['identity']}",
        f"**Selected platforms:** {platform_names}", "",
        "## Generate concepts", "",
        "Use these as image-generation or designer briefs. Produce several candidates per direction; "
        "these are concept images, not final app assets. Keep editable source artwork when refining a choice.", "",
    ]
    for title, direction in directions:
        lines.extend([
            f"### {title}", "",
            f"Create an original app icon concept for {name}, whose purpose is: {promise} "
            f"{direction} Express a {brief['identity'].replace('-', ', ')} character. "
            "Use a legible small-size silhouette, restrained detail, intentional color, and a clean square composition. "
            "Avoid small text, screenshots, device frames, Apple logos, and copied brand marks. "
            "Use lettering only if the approved icon concept calls for it. "
            f"Avoid: {constraints}", "",
        ])
    lines.extend([
        "## Select and finish", "",
        "- [ ] Compare candidates at actual small size, in grayscale, and beside neighboring app icons.",
        "- [ ] Check uniqueness, meaning, legibility, contrast, and resemblance to existing brands.",
        "- [ ] Refine one concept into editable, properly licensed source layers or artwork.",
        "- [ ] Check the current Apple App icons HIG and the Xcode icon workflow for every selected platform.",
        "- [ ] For iOS, iPadOS, macOS, and watchOS, evaluate Icon Composer and its appearance variants.",
        "- [ ] For tvOS or visionOS, review the platform's layered asset-catalog requirements.",
        "- [ ] Preview the built icon in Simulator and on relevant hardware across supported appearances.",
        "- [ ] Save the chosen source, exports, review screenshots, and decision rationale in the app repository.",
        "",
        "Apple references: https://developer.apple.com/design/human-interface-guidelines/app-icons "
        "and https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer "
        "and https://developer.apple.com/documentation/xcode/configuring-your-app-icon", "",
    ])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brief", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        plan = build_plan(load_brief(args.brief))
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(plan, encoding="utf-8")
            print(f"Generated {args.output}")
        else:
            print(plan, end="")
    except (IconBriefError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
