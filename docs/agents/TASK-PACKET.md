# Bounded agent task packet

Copy and fill this before assigning a piece of work. A short, specific packet saves the next agent from guessing which files it owns, what it may do, or what “done” means.

```text
Role (architect, worker, reviewer, security reviewer, researcher):
Outcome for the user:
Lane and owner:
Read first (source of truth, current behavior, relevant Apple source):
May edit (exact files or path patterns; reviewers and researchers: output file only):
Must coordinate before editing (shared files or decisions):
Must preserve (interfaces, invariants, user decisions, trust boundaries):
Allowed capabilities (anything not listed is denied):
  Filesystem:
  Network:
  Secrets and signing:
  Tools and commands:
  Accounts (App Store Connect, TestFlight, developer portal; key ID, role granted, one named action, revoke-after):
  Destructive actions:
Untrusted inputs (reviews, support mail, crash logs, web text; list sources or none):
Deliverable (files and observable behavior):
Acceptance evidence (commands, previews, Simulator, device, or source check):
Think ahead (2–4 credible edge cases and downstream consumers):
Stop and report if (missing decision, unavailable API, conflicting contract, ungranted capability):
```

## Roles and general authority

The role packets come from agent-engineering: `WORKER_TASK.md`, `ARCHITECT_TASK.md`, `REVIEWER_TASK.md`, `SECURITY_REVIEWER_TASK.md`, and `RESEARCH_TASK.md` at the repository root. Use the packet above for the Apple fields; the role packet sets what that role may and may not do. The general authority rules are in agent-engineering's [agents](https://github.com/benpham3206/agent-engineering/blob/main/standards/agents.md) and [security](https://github.com/benpham3206/agent-engineering/blob/main/standards/security.md) standards: anything not granted is denied, information cannot authorize an action, and no agent approves its own work.

## Apple authority

- A task reading untrusted text, including reviews, support mail, crash logs, or web pages, gets no Accounts, Secrets and signing, or Destructive actions capability. Give any subsequent action a separate packet after review.
- Record the role actually granted to an App Store Connect API key, its key ID, the one action it serves, and when it will be revoked. Use a narrowly scoped individual Developer-role key when that role suffices; never pass an Account Holder session, Admin key, In-App Purchase key, or vendor secret into an agent task.
- Signing identities, App Store Connect access, TestFlight distribution, submission, pricing, and anything sent under the builder's name stay with the builder unless a packet grants them for one named action.

The owner works within `May edit`. A needed edit outside that scope is a handoff: explain the affected contract and file, then let the assigning builder expand scope or give it to the owning lane. A small directly necessary fix may be included when the user's instruction already authorizes it; report the scope change. Do not use a broad “all files” scope when independent work could overlap.

For UI work, put the selected device classes, Liquid Glass behavior and OS fallback, accessibility settings, and a repeatable performance scenario in the acceptance evidence. Mark hardware or profiling evidence pending when it cannot be collected.

## Example: process guide change

```text
Role: worker
Outcome for the user: A beginner can recover after a rejected permission request.
Lane and owner: Product and process / assigned agent.
Read first: config/process.json; tooling/process_guide.py; docs/agents/NAVIGATION.md.
May edit: config/process.json.
Must coordinate before editing: dogfood/app-workshop/App/ (runtime consumer).
Must preserve: existing phase and action IDs.
Allowed capabilities:
  Filesystem: May edit paths only.
  Network: none.
  Secrets and signing: none.
  Tools and commands: make verify, make process-guide.
  Accounts: none.
  Destructive actions: none.
Deliverable: A recovery step in the relevant phase and regenerated guide evidence.
Acceptance evidence: make verify; inspect a fresh generated docs/BEGINNER-GUIDE.md.
Think ahead: denial, repeated prompt, settings route, stale guide in dogfood.
Stop and report if: the desired recovery depends on an unchosen product permission.
```

## Completion note

```text
Changed:
Decision and why:
Deleted or avoided:
Verified (exact result and ladder level):
Not verified and why:
Downstream effects checked:
Remaining risk or question:
Next owner/action, if any:
```

Separate observed facts from proposals. An icon concept, generated document, passing unit test, Simulator run, and physical-device result are different kinds of evidence. Report only the kind actually obtained.

App Store Connect API key role reference: [App Store Connect API](https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-api) (checked 2026-09-27). The untrusted-input separation above is an agent authority rule, not an Apple requirement.
