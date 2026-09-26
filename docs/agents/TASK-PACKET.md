# Bounded agent task packet

Copy and fill this before assigning a piece of work. A short, specific packet saves the next agent from guessing which files it owns or what “done” means.

```text
Outcome for the user:
Lane and owner:
Read first (source of truth, current behavior, relevant Apple source):
May edit (exact files or path patterns):
Must coordinate before editing (shared files or decisions):
Deliverable (files and observable behavior):
Acceptance evidence (commands, previews, device, or source check):
Think ahead (2–4 credible edge cases and downstream consumers):
Stop and report if (missing decision, unavailable API, conflicting contract):
```

The owner works within `May edit`. A needed edit outside that scope is a handoff: explain the affected contract and file, then let the assigning builder expand scope or give it to the owning lane. A small directly necessary fix may be included when the user's instruction already authorizes it; report the scope change. Do not use a broad “all files” scope when independent work could overlap.

For UI work, put the selected device classes, Liquid Glass behavior and OS fallback, accessibility settings, and a repeatable performance scenario in the acceptance evidence. Mark hardware or profiling evidence pending when it cannot be collected.

## Example: process guide change

```text
Outcome for the user: A beginner can recover after a rejected permission request.
Lane and owner: Product and process / assigned agent.
Read first: config/process.json; tooling/process_guide.py; docs/agents/NAVIGATION.md.
May edit: config/process.json; focused process-guide test.
Must coordinate before editing: dogfood/app-workshop/App/ (runtime consumer).
Deliverable: A recovery step in the relevant phase and regenerated guide evidence.
Acceptance evidence: make verify; inspect a fresh generated docs/BEGINNER-GUIDE.md.
Think ahead: denial, repeated prompt, settings route, stale guide in dogfood.
Stop and report if: the desired recovery depends on an unchosen product permission.
```

## Completion note

```text
Changed:
Decision and why:
Verified (exact result):
Not verified and why:
Downstream effects checked:
Remaining risk or question:
Next owner/action, if any:
```

Separate observed facts from proposals. An icon concept, generated document, passing unit test, Simulator run, and physical-device result are different kinds of evidence. Report only the kind actually obtained.
