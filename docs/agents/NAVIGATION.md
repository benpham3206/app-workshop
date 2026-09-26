# Agent navigation: boilerplate factory

This map is for changing the **factory**. A generated app has a separate `docs/agents/NAVIGATION.md`. Start with [AGENTS.md](../../AGENTS.md) and [PRINCIPLES.md](../../PRINCIPLES.md); then read the [task packet](TASK-PACKET.md) and the smallest relevant lane below. The assigned outcome and file scope govern the work, not the size of a directory.

## Find the right file

| If the task is about… | Source of truth | Derived files or evidence to inspect |
| --- | --- | --- |
| What a future app must decide | `docs/process/`, `config/process.json` | `tooling/process_guide.py`, generated `docs/BEGINNER-GUIDE.md` and `resources/process.json`, `dogfood/app-workshop/App/` |
| Meaning of an action or its states | `ux/interactions/`, `ux/patterns/` | generated `docs/ux/interactions/`, `docs/ux/patterns/`, `docs/ux/FLOWS.md`, platform profiles, relevant modules |
| Visual identity or icons | `design/identity/`, `design/app-icon/`, `design/NATIVE-REVIEW.md` | generated `design/identity/RECIPE.md`, `docs/design/`, `design/icon-brief.json`, dogfood assets |
| Liquid Glass or device performance | `core/principles/GLASS-AND-PERFORMANCE.md` | generated `docs/quality/GLASS-AND-PERFORMANCE.md`, selected platform profiles, quality matrix, physical-device evidence |
| Secure and responsive implementation | `core/principles/SECURE-FAST-DEFAULTS.md` | generated `docs/engineering/SECURE-FAST-DEFAULTS.md`, app state and service boundaries, privacy plan, test matrix |
| Native platform behavior | `platforms/<platform>/README.md` | generated `platforms/<platform>/PROFILE.md`, selected module contracts, quality matrix |
| A new OS, SDK, or device class | `docs/compatibility/REVIEW.md`, relevant platform profile; `platforms/ios/ADAPTIVE-LAYOUT.md` for iPhone | generated compatibility review, iPhone Duo contract if iOS is selected, native review, test matrix, release checklist |
| An optional capability | `modules/<module>/README.md`, `config/catalog.json` | generated `modules/<module>/CONTRACT.md`, `config/troubleshooting.json`, privacy and release prompts |
| A configuration choice or validation rule | `config/catalog.json`, `config/schema/project.schema.json`, `tooling/scaffold.py` | `examples/`, `tests/generation/`, generated `.apple-scaffold.json` |
| Generated wording or file layout | `templates/generated-app/`, `tooling/scaffold.py` | fresh temporary generation, `tests/generation/test_scaffold.py` |
| A likely failure | `config/troubleshooting.json`, `tooling/troubleshoot.py` | generated `docs/TROUBLESHOOTING.md`, selected platform/module source |
| A real app built to test the factory | `dogfood/app-workshop/` | `examples/self-dogfood/project.json`, its build and UI evidence; upstream factory files if a generated rule is wrong |

Find files with `rg --files <lane>`; find consumers with `rg -n 'term' config tooling templates docs tests dogfood`. Search names and symbols before making a new file. Generated `dist/` previews and `dogfood/` snapshots are **outputs**: fix a shared rule at its source, then deliberately refresh the affected output. Keep a genuine app-specific change inside dogfood.

## Lanes and write scope

| Lane | Normal write scope | Read across to | Handoff trigger |
| --- | --- | --- | --- |
| Product and process | `docs/process/`, `config/process.json` | beginner guide generator, dogfood app, release | A phase, promise, or acceptance gate changes. |
| Experience and identity | `ux/`, `design/` | platform profiles, generated design docs, quality | An interaction requires API support, state ownership, or a new asset contract. |
| Platform and capability | `platforms/`, `modules/`, capability entries in `config/` | privacy, troubleshooting, generation | Selection, entitlement, data lifecycle, or availability changes. |
| Generation | `tooling/`, `templates/`, schema and catalog | every output consumed by the changed generator | New output path, config field, or rendering behavior appears. |
| Quality | `tests/`, `examples/`, `dogfood/` evidence | owning source and generated artifact | A failure points to a design or factory defect. |
| Research, release, support | `docs/research/`, release and support guidance | product, capability, generated checklist | A current Apple rule changes a promise or implementation. |

The write scope is a default, not a substitute for the user's instruction. If an assigned task must cross lanes, name the shared contract and affected files in the handoff. Avoid simultaneous edits to a shared source file; split work at independent files or agree on one owner first. Do not silently change another lane's product decision to make a test pass.

## Follow the change to its consequences

1. **Locate the authority.** Read the source, relevant selected platform/module profile, and current tests. For Apple API or policy claims, check primary Apple documentation and record the check date.
2. **Draw the path.** Name the inputs, generated copies, runtime consumers, and user-visible behavior. For example, `config/process.json` → `tooling/process_guide.py` → generated guide and `resources/process.json` → dogfood Mac UI.
3. **Probe the next failure.** Consider missing/old data, interruption, permission denial, accessibility, localization, device size, appearance, OS availability, privacy, battery, and support burden where relevant. Pick credible cases; do not add speculative machinery.
4. **Change the narrowest source set.** Update a consuming contract or test when the behavior actually changes. Regenerate a snapshot only when it consumes the changed source.
5. **Verify at the right level.** Run `make verify` for factory contracts, generate into a fresh temporary directory for output changes, and build or inspect the dogfood app for runtime changes. Report checks you could not run.
6. **Hand off clearly.** State changed files, decision and reason, observed evidence, credible remaining risk, and the exact next owner/action. Use `TASK-PACKET.md` before assignment and its completion format afterward.

## Quick routes

- **New platform:** platform profile → catalog/schema/validator → generated navigation and profile → troubleshooting → tests → compatibility note.
- **New module:** concrete user job → module contract → catalog/validator → privacy/availability → troubleshooting → generation test. A catalog entry without a real module contract is incomplete.
- **New interaction:** action contract → state/recovery → platform input paths → accessibility → generated copy → focused test or preview.
- **New design asset:** brief → rough exploration → vector or production source → sizes/appearances → generated asset path → visual check.
- **Generator defect:** failing selection or output fixture → source/template fix → repeatable test → fresh generation. Do not patch only `dist/`.
