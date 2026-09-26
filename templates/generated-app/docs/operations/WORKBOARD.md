# Status, workboard, and decision log

Keep this short and current. It is the first thing a new agent reads after the brief.

## Status

| Field | Now |
| --- | --- |
| Current goal | First useful result |
| Current bottleneck | Name the one constraint that most directly blocks the goal. |
| Next smallest step | One step that reduces the bottleneck, with its check. |
| Security or privacy risk | Write `None known` only after review. |
| Active migration | Old path, new path, how it is verified, and the rollback point; or `None`. |
| Accepted regressions | Owner and exit condition; or `None`. |

## Capabilities

Levels: absent, works, reliable, observable, efficient, resilient. The goal and risk set the required level.

| Capability | Current | Required | Evidence |
| --- | --- | --- | --- |
| First useful result | absent | reliable | |

## Tasks

Keep one active milestone small enough to demonstrate. Move tasks only when acceptance evidence exists.

| ID | User outcome | Owner | State | Acceptance evidence | Blocker |
| --- | --- | --- | --- | --- | --- |
| 001 | First useful result | Builder | Idea | Demo on primary device | Product not chosen |

States: idea, ready, active, review, done, blocked. For an agent task, fill `docs/agents/TASK-PACKET.md` with exact `May edit` paths, shared-file coordination, downstream consumers, constraints, acceptance evidence, and stop condition. Assign one owner per shared source file. Review changed behavior and actual test output before marking done.

## Decisions

| Date | Decision | Why | Evidence | Revisit when |
| --- | --- | --- | --- | --- |
| Pending | Primary platform | | | |
| Pending | Minimum OS | | | |
| Pending | Data location and sync | | | |
| Pending | Payment model | | | |
