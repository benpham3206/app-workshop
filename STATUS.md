# Status

Keep this file current and short.

## Current goal

The factory uses agent-engineering as its upstream layer. See `GOAL.md`.

## Working

- Generation, adoption, and update pass `make verify`; dogfood matches the factory.
- agent-engineering's standards, role packets, and `scripts/` sync daily through a reviewed PR.
- `main` is protected by a ruleset.

## Failing or missing

- The daily sync has not yet opened a PR on its own since CI dispatch was added.
- Dogfood gates in `docs/quality/gates.json` are all open; none has evidence files yet.

## Current bottleneck

Device, glass, and performance evidence for the dogfood app.

## Security and trust risks

Synced agent instructions come from agent-engineering; each sync is a PR for review.

## Active migration

None.

## Next smallest step

Run the agent-engineering sync once by hand and confirm its PR gets the required `verify` check.
