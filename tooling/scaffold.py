#!/usr/bin/env python3
"""Validate a project selection, generate a planning scaffold (optionally with a runnable starter), and update it."""

import argparse
import difflib
import hashlib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "config" / "catalog.json").read_text(encoding="utf-8"))
TEMPLATES = ROOT / "templates" / "generated-app"
STARTERS = ROOT / "templates" / "starters"
MANIFEST = ".apple-scaffold.json"
ROLE_PACKETS = ("WORKER_TASK.md", "ARCHITECT_TASK.md", "REVIEWER_TASK.md", "SECURITY_REVIEWER_TASK.md", "RESEARCH_TASK.md")
# ADOPT keeps these when the project already has them; the project owns them afterwards.
KEEP_IF_PRESENT = ("README.md", "Makefile", ".gitignore")
MERGED = "AGENTS.md"
SLUG = re.compile(r"^[a-z](?:[a-z0-9-]{0,62}[a-z0-9])?$")


class ScaffoldError(Exception):
    pass


def _exact_keys(value, required, where):
    if not isinstance(value, dict) or set(value) != set(required):
        raise ScaffoldError(f"{where} must contain exactly: {', '.join(required)}")


def _selection(value, allowed, where, require_one=False):
    if not isinstance(value, list) or (require_one and not value):
        raise ScaffoldError(f"{where} must be {'a nonempty' if require_one else 'an'} array")
    if any(not isinstance(item, str) or item not in allowed for item in value):
        raise ScaffoldError(f"{where} contains an unknown choice")
    if len(value) != len(set(value)):
        raise ScaffoldError(f"{where} contains a duplicate choice")


def load_config(path):
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ScaffoldError(f"Cannot read configuration: {exc}") from exc
    return validate(config)


def validate(config):
    _exact_keys(config, ("schema_version", "project", "identity", "platforms", "modules"), "Configuration")
    if type(config["schema_version"]) is not int or config["schema_version"] != CATALOG["schema_version"]:
        raise ScaffoldError("Unsupported schema_version")
    _exact_keys(config["project"], ("name", "slug"), "project")
    name = config["project"]["name"]
    slug = config["project"]["slug"]
    if not isinstance(name, str) or not name.strip() or len(name) > 80 or any(ord(char) < 32 for char in name):
        raise ScaffoldError("project.name must be 1-80 printable characters")
    if not isinstance(slug, str) or not SLUG.fullmatch(slug):
        raise ScaffoldError("project.slug must be lowercase letters, digits, and internal hyphens")
    if not isinstance(config["identity"], str) or config["identity"] not in CATALOG["identities"]:
        raise ScaffoldError("identity is not in the catalog")
    _selection(config["platforms"], CATALOG["platforms"], "platforms", require_one=True)
    _selection(config["modules"], CATALOG["modules"], "modules")
    if "active-activity" in config["modules"] and not {"ios", "ipados"}.intersection(config["platforms"]):
        raise ScaffoldError("active-activity needs iOS or iPadOS; a paired Watch displays it")
    if "widgets" in config["modules"] and not {"ios", "ipados", "macos", "watchos", "visionos"}.intersection(config["platforms"]):
        raise ScaffoldError("widgets needs a WidgetKit platform; tvOS has no WidgetKit widgets")
    return config


def _check_starter(config, starter):
    if starter is None:
        return
    if starter not in {path.name for path in STARTERS.iterdir() if path.is_dir()}:
        raise ScaffoldError(f"Unknown starter: {starter}")
    if starter == "ios" and not {"ios", "ipados"}.intersection(config["platforms"]):
        raise ScaffoldError("The ios starter needs iOS or iPadOS in platforms")


def _render(text, tokens):
    for key, value in tokens.items():
        text = text.replace("{{" + key + "}}", value)
    if re.search(r"\{\{[A-Z_]+\}\}", text):
        raise ScaffoldError("An unresolved template token remains")
    return text


def _write_from_template(source, destination, tokens):
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(_render(source.read_text(encoding="utf-8"), tokens), encoding="utf-8")
    shutil.copymode(source, destination)


def _digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _hashes(root):
    return {
        path.relative_to(root).as_posix(): _digest(path)
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.name != MANIFEST
    }


def _module_text(module):
    source = ROOT / "modules" / module / "README.md"
    if not source.is_file():
        raise ScaffoldError(f"Missing module contract: {source.relative_to(ROOT)}")
    return source.read_text(encoding="utf-8")


def _build(config, starter, temporary):
    """Write every generated file except the manifest into an empty directory."""
    name = config["project"]["name"].strip()
    platforms = config["platforms"]
    tokens = {
        "PROJECT_NAME": name,
        # JSON string escaping matches Swift and project-file quoting for quotes and backslashes.
        "SWIFT_NAME": json.dumps(name, ensure_ascii=False)[1:-1],
        "TARGET_NAME": "".join(part.capitalize() for part in config["project"]["slug"].split("-")),
        "BUNDLE_ID": f"com.example.{config['project']['slug']}",
        "DEVICE_FAMILY": ",".join(
            family for family, platform in (("1", "ios"), ("2", "ipados")) if platform in platforms
        ),
        "IDENTITY": config["identity"],
        "PLATFORMS": "\n".join(f"- {item}" for item in config["platforms"]),
        "MODULES": "\n".join(f"- {item}" for item in config["modules"]) or "- None selected",
        "SELECTED_PLATFORM_FILES": "\n".join(
            f"- [{item}](../../platforms/{item}/PROFILE.md): `platforms/{item}/PROFILE.md`"
            for item in config["platforms"]
        ),
        "SELECTED_MODULE_FILES": "\n".join(
            f"- [{item}](../../modules/{item}/CONTRACT.md): `modules/{item}/CONTRACT.md`"
            for item in config["modules"]
        ) or "- None selected; add a capability only after its user job is clear.",
        "SELECTED_COMPATIBILITY_FILES": (
            "- [Adaptive iPhone layout](../compatibility/IPHONE-DUO.md): `docs/compatibility/IPHONE-DUO.md`"
            if "ios" in config["platforms"] else
            "- [Compatibility review](../compatibility/REVIEW.md): `docs/compatibility/REVIEW.md`"
        ),
        "IPHONE_TEST_MATRIX_ROW": (
            "| Adaptive iPhone | Compact to regular, open/close, rotate, resize, split view, and scene restoration; see `../compatibility/IPHONE-DUO.md` | iPhone Duo simulator and physical hardware | | Pending |"
            if "ios" in config["platforms"] else ""
        ),
        "IPHONE_AGENT_RULE": (
            "For an iPhone target, read `docs/compatibility/IPHONE-DUO.md` before designing navigation or promising new-device support. Preserve task state across compact, regular, rotation, posture, and scene transitions; record device evidence rather than inferring compatibility from an iPhone preview."
            if "ios" in config["platforms"] else ""
        ),
    }
    for source in TEMPLATES.rglob("*"):
        if source.is_file() and source.name != ".gitkeep":
            _write_from_template(source, temporary / source.relative_to(TEMPLATES), tokens)
    _write_from_template(ROOT / "PRINCIPLES.md", temporary / "PRINCIPLES.md", tokens)
    _write_from_template(
        ROOT / "core" / "principles" / "GLASS-AND-PERFORMANCE.md",
        temporary / "docs" / "quality" / "GLASS-AND-PERFORMANCE.md",
        tokens,
    )
    _write_from_template(
        ROOT / "core" / "principles" / "SECURE-FAST-DEFAULTS.md",
        temporary / "docs" / "engineering" / "SECURE-FAST-DEFAULTS.md",
        tokens,
    )
    _write_from_template(
        ROOT / "docs" / "agents" / "TASK-PACKET.md",
        temporary / "docs" / "agents" / "TASK-PACKET.md",
        tokens,
    )
    # Role packets synced from agent-engineering (tooling/sync-agent-engineering.sh); TASK-PACKET.md points to them.
    for packet in ROLE_PACKETS:
        shutil.copyfile(ROOT / packet, temporary / packet)
    _write_from_template(
        ROOT / "docs" / "compatibility" / "REVIEW.md",
        temporary / "docs" / "compatibility" / "REVIEW.md",
        tokens,
    )
    if "ios" in config["platforms"]:
        _write_from_template(
            ROOT / "platforms" / "ios" / "ADAPTIVE-LAYOUT.md",
            temporary / "docs" / "compatibility" / "IPHONE-DUO.md",
            tokens,
        )

    _write_from_template(
        ROOT / "design" / "identity" / config["identity"] / "README.md",
        temporary / "design" / "identity" / "RECIPE.md",
        tokens,
    )
    _write_from_template(
        ROOT / "design" / "app-icon" / "README.md",
        temporary / "docs" / "design" / "APP-ICON.md",
        tokens,
    )
    _write_from_template(
        ROOT / "design" / "NATIVE-REVIEW.md",
        temporary / "docs" / "design" / "NATIVE-REVIEW.md",
        tokens,
    )
    (temporary / "tools").mkdir(parents=True, exist_ok=True)
    for tool in ("icon_plan.py", "readiness.py"):
        shutil.copyfile(ROOT / "tooling" / tool, temporary / "tools" / tool)
    (temporary / "docs" / "quality" / "evidence").mkdir(parents=True, exist_ok=True)
    (temporary / "docs" / "quality" / "evidence" / ".gitkeep").touch()
    icon_brief = {
        "schema_version": 1,
        "app_name": config["project"]["name"].strip(),
        "identity": config["identity"],
        "platforms": config["platforms"],
        "product_promise": "",
        "visual_motifs": [],
        "avoid": [],
    }
    (temporary / "design" / "icon-brief.json").write_text(
        json.dumps(icon_brief, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    for source in (ROOT / "ux" / "interactions").glob("*.md"):
        _write_from_template(
            source, temporary / "docs" / "ux" / "interactions" / source.name, tokens
        )
    for source in (ROOT / "ux" / "patterns").glob("*.md"):
        _write_from_template(
            source, temporary / "docs" / "ux" / "patterns" / source.name, tokens
        )
    _write_from_template(
        ROOT / "docs" / "process" / "START-TO-SHIP.md",
        temporary / "docs" / "START-TO-SHIP.md",
        tokens,
    )
    _write_from_template(
        ROOT / "docs" / "process" / "SOLO-AI-OPERATING-SYSTEM.md",
        temporary / "docs" / "OPERATING-SYSTEM.md",
        tokens,
    )
    from process_guide import load_process, render_guide
    process = load_process()
    (temporary / "docs" / "BEGINNER-GUIDE.md").write_text(
        render_guide(process), encoding="utf-8"
    )
    (temporary / "resources").mkdir(parents=True, exist_ok=True)
    (temporary / "resources" / "process.json").write_text(
        json.dumps(process, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (temporary / "design" / "assets").mkdir(parents=True, exist_ok=True)
    (temporary / "design" / "assets" / ".gitkeep").touch()

    for platform in config["platforms"]:
        _write_from_template(
            ROOT / "platforms" / platform / "README.md",
            temporary / "platforms" / platform / "PROFILE.md",
            tokens,
        )
    for module in config["modules"]:
        destination = temporary / "modules" / module / "CONTRACT.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(_module_text(module), encoding="utf-8")

    from troubleshoot import build_guide
    (temporary / "docs" / "TROUBLESHOOTING.md").write_text(
        build_guide(config), encoding="utf-8"
    )

    if starter:
        for source in (STARTERS / starter).rglob("*"):
            if source.is_file():
                _write_from_template(source, temporary / source.relative_to(STARTERS / starter), tokens)


def _manifest(config, starter, files, unmanaged=()):
    manifest = {
        "template_version": (ROOT / "TEMPLATE_VERSION").read_text(encoding="utf-8").strip(),
        "selection": config,
        "starter": starter,
        "files": files,
    }
    if unmanaged:
        manifest["unmanaged"] = sorted(unmanaged)
    return manifest


def _write_manifest(root, manifest):
    (root / MANIFEST).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def generate(config, output, starter=None):
    _check_starter(config, starter)
    output = output.resolve()
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ScaffoldError(f"Refusing to overwrite nonempty target: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".apple-scaffold-", dir=output.parent))
    try:
        _build(config, starter, temporary)
        _write_manifest(temporary, _manifest(config, starter, _hashes(temporary)))
        if output.exists():
            output.rmdir()
        temporary.replace(output)
    except Exception:
        shutil.rmtree(temporary)
        raise


def update(project, apply=False):
    """Compare a generated project with the current factory output.

    A file the builder never edited (its hash still matches the manifest) is safe to replace.
    A file the builder edited is a conflict: it is reported with a diff and never overwritten.
    Files the factory no longer produces are reported, never deleted.
    """
    project = project.resolve()
    try:
        manifest = json.loads((project / MANIFEST).read_text(encoding="utf-8"))
        config = validate(manifest["selection"])
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise ScaffoldError(f"Cannot read {MANIFEST}: {exc}") from exc
    starter = manifest.get("starter")
    _check_starter(config, starter)
    recorded = manifest.get("files") or {}
    unmanaged = set(manifest.get("unmanaged") or ())
    plan = {"add": [], "update": [], "conflict": [], "retired": [], "diffs": []}
    with tempfile.TemporaryDirectory() as directory:
        fresh = Path(directory)
        _build(config, starter, fresh)
        fresh_hashes = _hashes(fresh)
        files = dict(recorded)
        for relative, digest in fresh_hashes.items():
            if relative in unmanaged:
                continue
            current = project / relative
            if not current.exists():
                plan["add"].append(relative)
            elif _digest(current) == digest:
                files[relative] = digest
            elif recorded.get(relative) == _digest(current):
                plan["update"].append(relative)
            else:
                plan["conflict"].append(relative)
                diff = difflib.unified_diff(
                    current.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True),
                    (fresh / relative).read_text(encoding="utf-8", errors="replace").splitlines(keepends=True),
                    f"project/{relative}", f"factory/{relative}",
                )
                plan["diffs"].append("".join(diff))
        plan["retired"] = sorted(set(recorded) - set(fresh_hashes))
        if apply:
            for relative in plan["add"] + plan["update"]:
                destination = project / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(fresh / relative, destination)
                files[relative] = fresh_hashes[relative]
            _write_manifest(project, _manifest(config, starter, dict(sorted(files.items())), unmanaged))
    return plan


def adopt(config, project):
    """Add the planning and operating layer to an existing app without touching its code.

    Existing README.md, Makefile, .gitignore, and .github/ files are kept. An existing AGENTS.md
    gets the generated rules appended. Any other existing path is a conflict, and then nothing is written.
    """
    project = project.resolve()
    if not project.is_dir():
        raise ScaffoldError(f"Existing project directory not found: {project}")
    if (project / MANIFEST).exists():
        raise ScaffoldError(f"{MANIFEST} already exists; use update instead")
    with tempfile.TemporaryDirectory() as directory:
        fresh = Path(directory)
        _build(config, None, fresh)
        paths = sorted(path.relative_to(fresh).as_posix() for path in fresh.rglob("*") if path.is_file())
        present = [relative for relative in paths
                   if (project / relative).exists() or (project / relative).is_symlink()]
        kept = [relative for relative in present
                if relative in KEEP_IF_PRESENT or relative.startswith(".github/")]
        merged = [relative for relative in present if relative == MERGED and (project / relative).is_file()]
        conflicts = sorted(set(present) - set(kept) - set(merged))
        if conflicts:
            raise ScaffoldError("ADOPT conflict; nothing was written. Already present: " + ", ".join(conflicts))
        written = [relative for relative in paths if relative not in present]
        for relative in written:
            destination = project / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(fresh / relative, destination)
        for relative in merged:
            rules = (fresh / relative).read_text(encoding="utf-8").split("\n", 1)[1]
            with (project / relative).open("a", encoding="utf-8") as handle:
                handle.write("\n\n## App Workshop operating layer\n" + rules)
        files = {relative: _digest(project / relative) for relative in written}
        _write_manifest(project, _manifest(config, None, files, kept + merged))
    return written, kept, merged


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "generate"):
        sub = subparsers.add_parser(command)
        sub.add_argument("--config", required=True, type=Path)
        if command == "generate":
            sub.add_argument("--output", required=True, type=Path)
            sub.add_argument("--starter", choices=sorted(path.name for path in STARTERS.iterdir() if path.is_dir()),
                             help="also generate a runnable app starter")
    sub = subparsers.add_parser("adopt", help="add the planning layer to an existing app")
    sub.add_argument("--config", required=True, type=Path)
    sub.add_argument("--project", required=True, type=Path)
    sub = subparsers.add_parser("update", help="dry-run by default; --apply writes only unedited files")
    sub.add_argument("--project", required=True, type=Path)
    sub.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "update":
            plan = update(args.project, args.apply)
            for kind in ("add", "update", "conflict", "retired"):
                for relative in plan[kind]:
                    print(f"{kind:9} {relative}")
            for diff in plan["diffs"]:
                print(diff)
            changes = len(plan["add"]) + len(plan["update"])
            print(f"{'Applied' if args.apply else 'Would apply'} {changes} change(s); "
                  f"{len(plan['conflict'])} conflict(s) left for review; retired files are never deleted.")
            return 0
        config = load_config(args.config)
        if args.command == "adopt":
            written, kept, merged = adopt(config, args.project)
            print(f"Adopted {args.project}: wrote {len(written)} file(s).")
            for relative in kept:
                print(f"kept      {relative}")
            if "Makefile" in kept:
                print("Your Makefile was kept. Add: check: ; python3 tools/readiness.py")
            for relative in merged:
                print(f"appended  {relative}")
            return 0
        if args.command == "generate":
            generate(config, args.output, args.starter)
            print(f"Generated {args.output}")
        else:
            print(f"Valid selection: {config['project']['slug']}")
    except (ScaffoldError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
