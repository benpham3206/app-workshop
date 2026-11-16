---
name: verify-builder-files
description: Check that update and adopt never change, remove, or write around a builder's file, in every project state the check can build. Use when a change touches update, adopt, _blocked, the manifest, or generated file paths in tooling/scaffold.py.
---

# Verify builder files

The promise: `update` and `adopt` never change, remove, or write around a file the builder owns.

The harm when it breaks: a builder loses work they wrote, or the factory writes files outside their project.

`tests/generation/test_builder_files.py` builds every project state in its `WORLD` table and runs the real `update` and `adopt` on each state. It checks invariants 1 and 5 in `ARCHITECTURE.md`. It is an exhaustive check up to a bound. It is not a proof.

## When to run it

Run it when your change touches one of these:

| File | What it covers |
|---|---|
| `tooling/scaffold.py` | `update`, `adopt`, `_blocked`, `_hashes`, `_digest`, `_manifest`, `_write_manifest`, `KEEP_IF_PRESENT`, `MERGED` |
| `templates/generated-app/` | a new generated path that `adopt` must keep or merge |
| `tests/generation/test_builder_files.py` | the check itself |

Last confirmed against the code at commit `03afe18`. If `git log 03afe18..HEAD -- tooling/scaffold.py` shows a commit, read that diff first. The check can be out of date.

## Run it

```
make verify-builder-files
```

It needs Python 3 and nothing else. It takes about 30 seconds. `make verify` and CI run it too.

## Read a failure

Each break has three lines: the rule, the state, and what changed.

```
Adopt writes nothing outside the project
    state: target='docs/product/BRIEF.md' entry='absent' folder='link to an outside folder'
    changed outside: ['linked/BRIEF.md']
```

Read it as steps. The builder's `docs/product` is a link to a folder outside the project. The builder runs `adopt`. A file appears in the outside folder.

The rules:

| Rule | Meaning |
|---|---|
| Update answers every state with a plan | An odd shape is a conflict in the plan. It is not a crash. |
| A dry run changes nothing | `update` without `--apply` writes no file. |
| Update writes nothing outside the project | No path outside the project folder changes. |
| Update never changes or removes a file the builder owns | The factory owns one thing: a plain file at a generated path, under real folders, with bytes that match the manifest. All other paths belong to the builder. |
| Update creates files only at generated paths | A link is never followed to a new place. |
| An update that stops with an error changes nothing | No half-applied update. |
| Update still applies the files the factory owns | One odd path does not block the other paths. |
| A second update has nothing left to apply | The first run finished the work. |
| Adopt writes nothing outside the project | Same as update. |
| An adopt that refuses writes nothing | A conflict leaves the app as it was. |
| Adopt never changes or removes a file the builder owns | Only a plain `AGENTS.md` can grow, and only at its end. |
| Adopt creates files only at generated paths | Same as update. |
| An adopted project has nothing left to update | `adopt` and `update` agree on the result. |

## Real bug or wrong check

1. Build the state by hand in a scratch folder. Run `python3 tooling/scaffold.py update --project <folder> --apply` or the `adopt` command.
2. If the file changes there too, the bug is in `scaffold.py`. Fix the code. Do not weaken the rule.
3. If it does not, the check built the state wrong. Fix `shape` in the test, and say why in the commit.

A failure that says `WORLD shrank` means a change removed states from the check. Put them back, or lower the number in the same commit and give the reason.

## When you change behavior on purpose

- A new shape a builder can leave on disk: add it to `ENTRIES` or `FOLDERS`.
- A new class of path in `adopt`, such as a new merged file: add one path of that class to `ADOPT_TARGETS`.
- A rule that must change: change it in the test and in `ARCHITECTURE.md` in the same commit. State the old rule and the new rule in the commit message.

Then prove that the check can still fail. In `_blocked`, delete `current.is_symlink() or`. Run the check. It must report breaks for `link to itself`. Put the line back and run it again. It must pass.

Move the commit in "When to run it" forward only after you do these steps on the new code.

## What it does not cover

- Two odd shapes on two different paths at the same time.
- A file that changes while `update` or `adopt` runs.
- File permissions, hard links, and file systems that fold case.
- Windows. Links there are junctions, and the check runs on macOS and Linux only.
- `generate`. The tests in `test_scaffold.py` cover it.
- The real template output. The check builds the factory files once and reuses them for every state.
