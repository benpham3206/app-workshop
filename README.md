# Apple ecosystem boilerplate

A product-neutral planning scaffold for apps across Apple platforms. It includes selectable identity recipes, platform profiles, optional capability contracts, an interaction library, an icon concept planner, and a generator for likely troubleshooting checks. It does not choose a product. With `--starter ios` it also generates a minimal iOS app that builds, tests, and launches in Simulator.

`PRINCIPLES.md` defines the quality standard for builders and agents: great and outstanding are the baseline; timeless is the long-term goal.
`core/principles/GLASS-AND-PERFORMANCE.md` makes native Liquid Glass and responsive performance across selected devices explicit design and release gates.
`core/principles/SECURE-FAST-DEFAULTS.md` gives each generated app a state, permission, privacy, and responsiveness contract for its first real code slice.
`design/NATIVE-REVIEW.md` is a review record for layout, controls, states, accessibility, icon, and performance on a runnable app. It requires evidence rather than visual claims from a template.
`docs/compatibility/REVIEW.md` gives each app a repeatable review when an Apple SDK, OS, or device class changes.
`platforms/ios/ADAPTIVE-LAYOUT.md` turns iPhone Duo into the iPhone layout stress test; iOS projects receive it as `docs/compatibility/IPHONE-DUO.md`.

For delegated work, `docs/agents/NAVIGATION.md` routes an agent to the source of truth and downstream outputs. `docs/agents/TASK-PACKET.md` defines its file scope, handoff, and evidence. Each generated app receives its own selection-aware navigation map.

## Try it

From this directory:

```sh
make validate
make verify
make generate
```

The sample selection in `examples/neutral-preview/project.json` generates `dist/neutral-preview/`. The generated project has a brief, identity decision, flowchart, interaction guides, icon guide, architecture and privacy prompts, platform and module notes, release checklist, and tailored troubleshooting guide. `dist/` is ignored by Git. Generation refuses to overwrite a nonempty destination.

To try another selection, copy the sample JSON and change its identity, platforms, and modules from `config/catalog.json`:

```sh
make validate CONFIG=path/to/project.json
make generate CONFIG=path/to/project.json OUTPUT=dist/my-preview
make troubleshoot CONFIG=path/to/project.json
```

To get a runnable iOS app on day one, add the starter. It needs Xcode; set `DEVELOPER_DIR` if Xcode is not the active developer directory.

```sh
make generate CONFIG=path/to/project.json OUTPUT=dist/my-app STARTER=ios
cd dist/my-app && make run    # build and launch in Simulator
make test                     # Swift Testing state tests
```

The starter is an Xcode project with synchronized folders, so new Swift files in `App/` or `AppTests/` build without project-file edits. It uses Swift 6 language mode, a `Logger`, and one task owner with tests for duplicate taps and failure recovery. `make verify-xcode` runs the same generate-and-test check from this factory.

To add the planning and operating layer to an app that already exists, adopt it:

```sh
make adopt CONFIG=path/to/project.json PROJECT=path/to/app
```

ADOPT never touches app code. It keeps an existing `README.md`, `Makefile`, `.gitignore`, and `.github/` files, appends the generated rules to an existing `AGENTS.md`, and stops before writing anything if any other generated path already exists. Kept and merged files are recorded as unmanaged, so `update` leaves them alone.

To adopt later factory fixes in an existing app, run a dry run first:

```sh
make update PROJECT=path/to/app          # report only
make update PROJECT=path/to/app APPLY=1  # write files the builder never edited
```

The manifest records a hash of each generated file. A file the builder edited is reported as a conflict with a diff and is never overwritten. Projects generated before 0.5.0 have no hashes, so every changed file is a conflict.

Each generated project includes `make check` and `make icon-plan`. Run `make check` inside the generated project to inspect its structure and its gates in `docs/quality/gates.json`. A gate is `open` or `done`; `done` must cite evidence files that exist. Once a real app has a purpose and icon motifs, fill its `design/icon-brief.json` and run `make icon-plan` there. The planner creates concept prompts and a production checklist; artwork and Xcode previews remain separate steps.

The configuration contract is in `config/schema/project.schema.json`. The CLI performs its own selection checks; the JSON Schema is provided for editors and external tooling.

## Learn the system

The change discipline, verification ladder, defect loop, capability levels, agent roles, and authority rules are adapted from [agent-engineering](https://github.com/benpham3206/agent-engineering) for Apple apps. So are ADOPT, the tracked-secret check, and the generated CI and pull request template.


1. Read `docs/research/apple-guideline-audit.md` for Apple guidance and open questions.
   Follow `docs/process/START-TO-SHIP.md` for the full learning path.
2. Read `ux/interactions/README.md` for action behavior, button states, menus, and inputs. Use `ux/patterns/` for onboarding, permissions, settings, and help.
3. Read `design/app-icon/README.md` and the three `design/identity/` recipes.
   `docs/process/SOLO-AI-OPERATING-SYSTEM.md` maps the builder-and-agent workflow from discovery through support.
   `docs/process/PORTFOLIO-ARCHITECTURE.md` covers reuse across several apps and future Apple devices.
4. Generate the neutral preview and follow its `README.md` from user job to flow, action contracts, design, platform adaptations, and likely failure checks.
5. Choose a real product before adding app targets, entitlements, dependencies, or payment behavior.

## Directory map

| Directory | Intended responsibility |
| --- | --- |
| `core/` | Stable principles and interaction contracts shared by future products. |
| `config/` | Selection catalog, schema, and troubleshooting rules. |
| `design/` | Identity directions, semantic tokens, components, motion, content, assets, and icon process. |
| `ux/` | Flows, action behavior, inputs, states, and accessibility. |
| `platforms/` | Native presentation and input rules per Apple platform. |
| `modules/` | Optional capabilities including Live Activities, widgets, commerce, accounts, notifications, and sync. |
| `templates/` | Files copied into a generated project. |
| `tooling/` | Validation, generation, icon concept planning, and troubleshooting tools. |
| `examples/` | A neutral sample to inspect the system without choosing a product. |
| `tests/` | Generator contract tests and future app checks. |
| `docs/` | Apple research, decisions, privacy, localization, performance, compatibility, release, and support notes. |

`modules/active-activity/` separates the activity contract from its presentations. An iPhone or iPad Live Activity can appear in the Dynamic Island and Lock Screen, and on a paired Watch in the Smart Stack. A persistent Watch widget belongs in the separate `modules/widgets/` module. These are distinct system features even when they show the same underlying state.

The three directories under `design/identity/` are selectable starting directions for future apps: Playful/Kinetic, Calm/Precise, and Dark/Technical. They do not define a product or force one appearance on every app. Read `AGENTS.md` before changing this boilerplate.
