# App Workshop

A factory for Apple apps, built for one person working with AI agents. It takes you from an idea to a running app, through App Review, to a first renewing subscriber. It does not choose your product: you pick the job, platforms, and capabilities; it generates the plan, the starter app, the checklists, and the guardrails.

## The path

| Stage | What you do | Where to start |
| --- | --- | --- |
| 1. Idea | Name the person, the repeated problem, the first useful result, and why they would return. | `docs/process/START-TO-SHIP.md` |
| 2. Setup (week 1) | Enroll in the Apple Developer Program; have the Account Holder accept the Paid Apps Agreement and finish tax and banking. Clear the app name. These take days to weeks and block selling. | Generated `docs/BEGINNER-GUIDE.md`, research `REPORT.md` |
| 3. Build | Generate a runnable app and build one complete task end to end. | `make generate … STARTER=ios` |
| 4. Sell | Choose one-time or subscription value, then follow the commerce contract. | `modules/commerce/README.md` |
| 5. Ship | Publish privacy, terms, and support pages; test with TestFlight; fill the store page; submit with a released (non-beta) Xcode. | Generated `docs/release/CHECKLIST.md`, `docs/legal/` |
| 6. First customer | Build a waitlist, tune the listing, decide on ads, and watch the funnel to the first renewal. | Generated `docs/BEGINNER-GUIDE.md` (launch), `docs/operations/MEASUREMENT.md` |
| 7. Operate | Fix crashes and confusion before adding features; review each new OS. | Generated `docs/TROUBLESHOOTING.md`, `docs/operations/WORKBOARD.md` |

The research behind stages 2–6 (accounts, fees, payouts, App Review, StoreKit and RevenueCat, payment routes, legal and regional blockers, acquisition, failure modes) is in [`docs/research/app-store-to-first-subscriber/`](docs/research/app-store-to-first-subscriber/REPORT.md). It is dated; recheck Apple's rules before relying on it.

## Quick start

```sh
make verify                                   # factory self-test
make generate                                 # preview into dist/neutral-preview/
make generate CONFIG=my-app.json OUTPUT=dist/my-app STARTER=ios
cd dist/my-app && make run                    # build and launch in Simulator (needs Xcode)
make test                                     # Swift Testing state tests
make check                                    # structure, release gates, and tracked-secret scan
```

Start `my-app.json` by copying `examples/neutral-preview/project.json` and choosing an identity, platforms, and modules from `config/catalog.json`. Generation never overwrites a nonempty folder. Set `DEVELOPER_DIR` if Xcode is not the active developer directory.

Already have an app? Add the planning layer without touching app code, and pull later factory fixes:

```sh
make adopt CONFIG=my-app.json PROJECT=path/to/app
make update PROJECT=path/to/app               # report only
make update PROJECT=path/to/app APPLY=1       # update files you never edited
```

## What you get

- **A starter app** (`--starter ios`): Xcode project, Swift 6, one task owner with tests, `make run` and `make test`.
- **Planning documents**: brief, flows, action contracts, identity and icon brief, privacy plan, architecture prompts.
- **Capability contracts** for optional modules (commerce, accounts, sync, notifications, widgets, Live Activities, App Intents, and more), each with a native-first build-vs-buy table.
- **Release gates**: checklist, store page, evidence-backed gates checked by `make check`, and a troubleshooting guide tailored to your selection.
- **Guardrails**: a tracked-secret scan (file names and contents), no-rollback release rules, and an entitlement-failure policy for purchases.

## Working with agents

Agents start at [`AGENTS.md`](AGENTS.md). Assign work with [`docs/agents/TASK-PACKET.md`](docs/agents/TASK-PACKET.md): a bounded goal, exact write scope, granted capabilities, and the evidence that proves it is done. [`docs/agents/NAVIGATION.md`](docs/agents/NAVIGATION.md) maps each topic to its source of truth. [`PRINCIPLES.md`](PRINCIPLES.md) defines the quality bar and the verification ladder. Signing, App Store Connect, pricing, and submission stay with the builder unless a packet grants one named action.

## Not included yet

These can block a first app, so plan for them:

- **Purchase code.** Commerce is a contract, not an implementation. The starter has no paywall or StoreKit code.
- **A macOS starter.** Only iOS has a runnable starter. Mac apps that cannot pass Mac App Store review need Developer ID signing, notarization, and their own payment provider.
- **Release automation.** Upload, screenshots, and review status are manual; the proposed agent tooling is in `07_agent_operable_pipeline.md`.

## Repository map

| Directory | Contents |
| --- | --- |
| `core/` | Principles shared by every app (performance, Liquid Glass, secure defaults). |
| `config/` | Selection catalog, schema, beginner journey, troubleshooting rules. |
| `design/`, `ux/` | Identity recipes, icon process, interaction contracts, onboarding and permission patterns. |
| `platforms/` | Native behavior for each Apple platform. |
| `modules/` | Optional capability contracts. |
| `templates/`, `tooling/` | Generated files and the generator, checker, and planners. |
| `docs/` | Process, research, compatibility, and agent guides. |
| `dogfood/` | App Workshop's own Mac app, built with the factory. `make verify` fails when it falls behind the factory; files the app owns are listed under `unmanaged` in its `.apple-scaffold.json`. |
| `tests/` | Generator contract tests (`make verify`). |
| `vendor/` | agent-engineering's language-neutral standards, pinned in `vendor/agent-engineering.lock`. `tooling/sync-agent-engineering.sh` refreshes them; a daily workflow opens the PR. |

Adapted from [agent-engineering](https://github.com/benpham3206/agent-engineering) for Apple apps.
