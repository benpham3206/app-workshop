# App Workshop

A product-neutral factory for native Apple apps. Select the platforms, identity, and optional capabilities. Generate an app scaffold, add the iOS starter when needed, and carry later factory changes into existing apps without overwriting your edits.

This repository owns app construction and build verification. The [Principles skills](https://github.com/benpham3206/principles) supply the engineering method. Sales, publishing, and hosted legal templates live in the repositories linked below.

## Quick start

```sh
make verify                                   # factory and repository checks
make generate                                 # preview into dist/neutral-preview/
make generate CONFIG=my-app.json OUTPUT=dist/my-app STARTER=ios
cd dist/my-app && make run                     # build and launch in Simulator
make test                                     # Swift Testing state tests
make check                                    # structure, evidence gates, and tracked-secret scan
```

Copy `examples/neutral-preview/project.json` to start `my-app.json`. Choose an identity, platforms, and modules from `config/catalog.json`. Generation requires an empty destination. The supported platforms are iOS, iPadOS, macOS, watchOS, and visionOS. Only iOS and iPadOS have a runnable starter.

Xcode and an installed iOS Simulator runtime are required for `make run`, `make test`, and the factory's `make verify-xcode`. Set `DEVELOPER_DIR` when Xcode is not the active developer directory.

To add the scaffold to an existing app and receive later changes, run these commands from the factory:

```sh
make adopt CONFIG=my-app.json PROJECT=path/to/app
make update PROJECT=path/to/app               # report only
make update PROJECT=path/to/app APPLY=1       # update files you never edited
```

Adoption preserves app source and existing root instructions. It writes nothing when a generated path conflicts. Updates preserve edited files and report retired files without deleting them.

## What the factory supplies

- An optional iOS starter with an Xcode project, Swift 6, one task owner with tests, and Simulator build and launch commands.
- App specifications for the first useful result, flows, state, native interactions, identity, icons, privacy, and architecture.
- Optional capability contracts for accounts, commerce, sync, notifications, widgets, Live Activities, App Intents, background work, and sharing.
- Release requirements, evidence gates, and troubleshooting filtered to the selected platforms and modules. A passing structure check does not approve a release.
- A tracked-secret scan, signing exclusions, privacy manifest, icon and entitlement requirements, and version checks for the starter.

Purchase code, a macOS starter, upload automation, and store publishing are outside the current implementation.

## External material

| Material | Home |
| --- | --- |
| Account, payment, review, legal, and acquisition research | [Distribution research](https://github.com/benpham3206/distribution/tree/main/research/app-store-to-first-subscriber) |
| Product and publishing platform research | [Productivity platform research](https://github.com/benpham3206/distribution/tree/main/research/productivity-platform) |
| Store page and measurement templates | [App Store templates](https://github.com/benpham3206/distribution/tree/main/templates/app-store) |
| Privacy policy, Terms of Use, and support page templates | [Legal templates](https://github.com/benpham3206/web-workshop/tree/main/templates/legal) |

The research is dated. Recheck current Apple requirements before release.

## Working with agents

Start at [AGENTS.md](AGENTS.md). [The navigation map](docs/agents/NAVIGATION.md) identifies the owning files. Give each assignment a bounded goal, exact write scope, granted capabilities, constraints, and acceptance evidence. Signing, account, pricing, and submission actions require the builder's explicit authorization.

[The Apple quality guide](PRINCIPLES.md) is locally authored and records app-specific review and release expectations. It is separate from the external Principles skills.

## Repository map

| Directory | Contents |
| --- | --- |
| `core/` | Shared Apple app performance, Liquid Glass, and security requirements. |
| `config/` | Selection catalog, schema, process, and troubleshooting rules. |
| `design/`, `ux/` | Identity recipes, icon process, native interactions, and recovery patterns. |
| `platforms/` | Profiles for the five supported Apple platforms. |
| `modules/` | Optional capability contracts. |
| `templates/`, `tooling/` | Generated files, the iOS starter, generator, checker, and planners. |
| `docs/` | App process, compatibility, Apple guideline audit, and navigation. |
| `scripts/` | Locally owned repository structure, token, and tracked-secret checks. |
| `tests/` | Generation, adoption, update, security, and optional Simulator checks. |

The main CI workflow runs `make verify` on pull requests. Its manual Xcode job runs `make verify-xcode`.
