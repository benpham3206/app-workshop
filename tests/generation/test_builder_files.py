"""Every project state in WORLD, checked against the builder-file rules.

Guards ARCHITECTURE.md invariants 1 and 5: `update` and `adopt` never change, remove, or
write around a file the builder owns. `test_scaffold.py` tries the cases someone thought of.
This file builds every combination in WORLD and runs the real `update` and `adopt` on each.
`.claude/skills/verify-builder-files/SKILL.md` says how to read a failure and when to rerun.

Scope: one generated path and its folder take every shape in WORLD while the rest of the
project holds one file of each ordinary kind. Left out: two odd shapes on different paths at
once, a change made while the tool runs, permissions, hard links, and case-folded names.
"""

import hashlib
import itertools
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tooling"))
import scaffold  # noqa: E402

EXAMPLE = ROOT / "examples" / "neutral-preview" / "project.json"
MANIFEST = scaffold.MANIFEST

STALE = b"text an older factory wrote\n"
EDITED = b"text the builder wrote\n"

# WORLD: what a builder can leave at one generated path, at its folder, and in the manifest.
ENTRIES = (
    "absent", "current", "stale", "edited",
    "link to an outside file", "link to an own file",
    "link to an outside stale file", "link to an own stale file",
    "dangling link outside", "dangling link inside", "link to itself",
    "empty folder", "folder with a file",
)
FOLDERS = ("folder", "link to an outside folder", "link to an own folder", "file", "absent")
RECORDS = ("matches", "differs", "missing", "unmanaged")
# `update` treats every generated path alike. `adopt` has three classes: written, merged, kept.
UPDATE_TARGET = "docs/product/BRIEF.md"
ADOPT_TARGETS = ("docs/product/BRIEF.md", scaffold.MERGED, "README.md", ".github/workflows/ci.yml")
# Ordinary files beside the target. PENDING_ADD sorts first, so it is written before the target.
PENDING_ADD = "docs/BEGINNER-GUIDE.md"
PENDING_UPDATE = "docs/ux/STATES.md"
EDITED_ELSEWHERE = "docs/START-TO-SHIP.md"
OWN_FOLDER = "own-folder"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def snapshot(root):
    """Every path under root: its kind, and its bytes or link text. Links are never followed."""
    seen = {}
    for folder, names, files in os.walk(root, followlinks=False):
        for name in names + files:
            path = Path(folder, name)
            key = path.relative_to(root).as_posix()
            if path.is_symlink():
                seen[key] = ("link", os.readlink(path))
            elif path.is_dir():
                seen[key] = ("folder", None)
            else:
                seen[key] = ("file", path.read_bytes())
    return seen


def differs(before, after):
    return sorted(key for key in set(before) | set(after) if before.get(key) != after.get(key))


def shape(project, outside, target, entry, folder, current):
    """Give `target` one ENTRIES shape under one FOLDERS shape.

    Returns False for a state that cannot exist, else the bytes a reader of the path gets.
    """
    path, parent = project / target, (project / target).parent
    if parent == project:
        if folder != "folder":
            return False
        real = project
    else:
        if parent.is_symlink() or parent.is_file():
            parent.unlink()
        elif parent.is_dir():
            shutil.rmtree(parent)
        parent.parent.mkdir(parents=True, exist_ok=True)
        if folder in ("file", "absent"):
            if entry != "absent":
                return False
            if folder == "file":
                parent.write_bytes(EDITED)
            return None
        real = {"folder": parent, "link to an outside folder": outside / "linked",
                "link to an own folder": project / OWN_FOLDER / "linked"}[folder]
        real.mkdir()
        if real != parent:
            parent.symlink_to(real, target_is_directory=True)
    where = real / path.name
    if where.is_file() or where.is_symlink():
        where.unlink()
    if entry in ("current", "stale", "edited"):
        data = {"current": current, "stale": STALE, "edited": EDITED}[entry]
        where.write_bytes(data)
        return data
    if entry == "link to itself":
        where.symlink_to(where)
    elif entry.startswith("link to"):
        data = STALE if "stale" in entry else EDITED
        aim = (outside if "outside" in entry else project) / "link-target.md"
        aim.write_bytes(data)
        where.symlink_to(aim)
        return data
    elif entry.startswith("dangling"):
        where.symlink_to((outside if "outside" in entry else project) / "nothing-here.md")
    elif "folder" in entry:
        where.mkdir()
        if entry == "folder with a file":
            (where / "inside.md").write_bytes(EDITED)
    return None


def plain_parents(key, paths):
    return all(paths.get(parent.as_posix(), ("folder",))[0] == "folder" for parent in list(Path(key).parents)[:-1])


def run(action):
    """Run one scaffold call. Returns (result, error). A refusal is an answer, not a crash."""
    try:
        return action(), None
    except (scaffold.ScaffoldError, OSError) as exc:
        return None, exc


class BuilderFiles(unittest.TestCase):
    """Rule: ARCHITECTURE.md invariants 1 and 5 hold in every WORLD state."""

    @classmethod
    def setUpClass(cls):
        cls.scratch = Path(tempfile.mkdtemp(prefix="builder-files-")).resolve()
        cls.config = scaffold.load_config(EXAMPLE)
        cls.fresh = cls.scratch / "fresh"
        scaffold.generate(cls.config, cls.fresh)
        cls.generated = set(json.loads((cls.fresh / MANIFEST).read_text(encoding="utf-8"))["files"])
        # One build serves every state: the factory output does not depend on the project.
        cls.real_build = scaffold._build
        scaffold._build = lambda config, starter, temporary: shutil.copytree(
            cls.fresh, temporary, dirs_exist_ok=True, copy_function=os.link,
            ignore=shutil.ignore_patterns(MANIFEST))

    @classmethod
    def tearDownClass(cls):
        scaffold._build = cls.real_build
        shutil.rmtree(cls.scratch)

    def setUp(self):
        self.breaks, self.states, self.built = [], 0, 0

    def world(self):
        self.built += 1
        base = self.scratch / f"world-{self._testMethodName}-{self.built}"
        (base / "outside").mkdir(parents=True)
        (base / "outside" / "kept.md").write_bytes(EDITED)
        self.addCleanup(shutil.rmtree, base, ignore_errors=True)
        return base / "project", base / "outside"

    def broke(self, state, rule, detail):
        where = " ".join(f"{name}={value!r}" for name, value in zip(self.names, state))
        self.breaks.append(f"{rule}\n    state: {where}\n    {detail}")

    def report(self, least):
        self.assertGreaterEqual(self.states, least, "WORLD shrank; a state that is not built is not checked")
        if self.breaks:
            self.fail(f"{len(self.breaks)} break(s) in {self.states} states:\n\n" + "\n\n".join(self.breaks))

    def created_elsewhere(self, before, after):
        return sorted(key for key in after if key not in before and key != MANIFEST and key not in self.generated
                      and not any(path.startswith(key + "/") for path in self.generated))

    def test_update_keeps_every_builder_file(self):
        target, self.names = UPDATE_TARGET, ("entry", "folder", "record")
        for state in itertools.product(ENTRIES, FOLDERS, RECORDS):
            entry, folder, record = state
            project, outside = self.world()
            shutil.copytree(self.fresh, project)
            manifest = json.loads((project / MANIFEST).read_text(encoding="utf-8"))
            (project / PENDING_ADD).unlink()
            (project / PENDING_UPDATE).write_bytes(STALE)
            manifest["files"][PENDING_UPDATE] = digest(STALE)
            (project / EDITED_ELSEWHERE).write_bytes(EDITED)
            (project / "docs" / "RETIRED.md").write_bytes(STALE)
            manifest["files"]["docs/RETIRED.md"] = digest(STALE)
            (project / OWN_FOLDER).mkdir()
            reads = shape(project, outside, target, entry, folder, (self.fresh / target).read_bytes())
            if reads is False:
                continue
            self.states += 1
            del manifest["files"][target]
            if record == "matches":
                manifest["files"][target] = digest(reads if reads is not None else STALE)
            elif record == "differs":
                manifest["files"][target] = digest(b"neither\n")
            elif record == "unmanaged":
                manifest["unmanaged"] = [target]
            (project / MANIFEST).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

            before, outside_before = snapshot(project), snapshot(outside)
            # The factory owns one thing: a plain file at a generated path, under real folders,
            # whose bytes still match the manifest. Every other path is the builder's.
            owned = {
                key: value for key, value in before.items()
                if key != MANIFEST and not (
                    value[0] == "file" and key in self.generated and plain_parents(key, before)
                    and manifest["files"].get(key) == digest(value[1])
                    and key not in manifest.get("unmanaged", ()))
            }

            plan, error = run(lambda: scaffold.update(project))
            if error is not None:
                self.broke(state, "Update answers every state with a plan", f"error: {error!r}")
            if snapshot(project) != before or snapshot(outside) != outside_before:
                self.broke(state, "A dry run changes nothing", f"changed: {differs(before, snapshot(project))}")
                continue

            plan, error = run(lambda: scaffold.update(project, apply=True))
            after = snapshot(project)
            if snapshot(outside) != outside_before:
                self.broke(state, "Update writes nothing outside the project",
                           f"changed outside: {differs(outside_before, snapshot(outside))}")
            changed = sorted(key for key, value in owned.items() if after.get(key) != value)
            if changed:
                self.broke(state, "Update never changes or removes a file the builder owns", f"changed: {changed}")
            if self.created_elsewhere(before, after):
                self.broke(state, "Update creates files only at generated paths",
                           f"created: {self.created_elsewhere(before, after)}")
            if error is not None and after != before:
                self.broke(state, "An update that stops with an error changes nothing",
                           f"error: {error!r}; changed: {differs(before, after)}")
            if error is None:
                for pending in (PENDING_ADD, PENDING_UPDATE):
                    if after.get(pending) != ("file", (self.fresh / pending).read_bytes()):
                        self.broke(state, "Update still applies the files the factory owns", f"not applied: {pending}")
                again, error = run(lambda: scaffold.update(project))
                if error is not None or again["add"] or again["update"]:
                    self.broke(state, "A second update has nothing left to apply",
                               f"error: {error!r}" if error else f"add={again['add']} update={again['update']}")
        self.report(least=150)

    def test_adopt_keeps_every_builder_file(self):
        self.names = ("target", "entry", "folder")
        for state in itertools.product(ADOPT_TARGETS, ENTRIES, FOLDERS):
            target, entry, folder = state
            if entry in ("current", "stale"):      # an app that was never generated has neither
                continue
            project, outside = self.world()
            (project / "Sources").mkdir(parents=True)
            (project / "Sources" / "main.swift").write_bytes(EDITED)
            (project / OWN_FOLDER).mkdir()
            if shape(project, outside, target, entry, folder, None) is False:
                continue
            self.states += 1
            before, outside_before = snapshot(project), snapshot(outside)

            _, error = run(lambda: scaffold.adopt(self.config, project))
            after = snapshot(project)
            if snapshot(outside) != outside_before:
                self.broke(state, "Adopt writes nothing outside the project",
                           f"changed outside: {differs(outside_before, snapshot(outside))}")
            if error is not None and after != before:
                self.broke(state, "An adopt that refuses writes nothing",
                           f"error: {error}; first changes: {differs(before, after)[:4]}")
            # Adopt may add text to the end of a plain AGENTS.md. It changes nothing else.
            changed = sorted(
                key for key, value in before.items() if after.get(key) != value and not (
                    key == scaffold.MERGED and value[0] == "file" and after.get(key, ("",))[0] == "file"
                    and after[key][1].startswith(value[1])))
            if changed:
                self.broke(state, "Adopt never changes or removes a file the builder owns", f"changed: {changed}")
            if self.created_elsewhere(before, after):
                self.broke(state, "Adopt creates files only at generated paths",
                           f"created: {self.created_elsewhere(before, after)}")
            if error is None:
                plan, error = run(lambda: scaffold.update(project))
                if error is not None or plan["add"] or plan["update"] or plan["conflict"]:
                    self.broke(state, "An adopted project has nothing left to update", f"plan: {error or plan}")
        self.report(least=90)


if __name__ == "__main__":
    unittest.main()
