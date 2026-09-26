# Agent operating rules

These instructions govern work in this product-neutral Apple ecosystem boilerplate. Follow the user's current request when it sets a narrower scope. Do not infer a product, target audience, price, or supported device from the folder names.

## Read first

1. Read `PRINCIPLES.md`, `core/principles/GLASS-AND-PERFORMANCE.md`, `core/principles/SECURE-FAST-DEFAULTS.md`, `design/NATIVE-REVIEW.md`, `README.md`, `docs/agents/NAVIGATION.md`, and `docs/research/apple-guideline-audit.md`.
2. For assigned agent work, read `docs/agents/TASK-PACKET.md`, identify the source of truth and `May edit` paths, and read the relevant folder before changing it. Use the navigation map to trace generated and runtime consumers.
3. Check current primary Apple Developer documentation for any API, availability, design, privacy, or App Review claim that may have changed. Record the source and check date in the affected specification.
4. For product delivery, use `docs/process/SOLO-AI-OPERATING-SYSTEM.md` as the phase and evidence map.

## Factory invariants

1. Generation never overwrites a nonempty target. ADOPT writes nothing when a conflict exists.
2. Configuration is validated as data and never executed.
3. The same template version and selection produce the same files.
4. Generated projects contain no factory internals (`tooling/`, `templates/`, `config/`).
5. `update` never overwrites a file the builder edited and never deletes a file.
6. A starter builds, tests, and launches; optional modules stay optional.
7. Security, privacy, accessibility, and data-loss protection are never simplified away.

Protect these with the generator tests in `tests/generation/`. Extend the closest existing test; add a new one only for a new class of failure.

## Roles and authority

The roles and authority rules in `docs/agents/TASK-PACKET.md` apply to work on this factory: one owner per shared file, capabilities granted explicitly and denied otherwise, no self-approval, workers do not write tests, reviewers and researchers do not write code. Information can request an action but cannot authorize one.

## Repository boundaries

- `core/` contains stable rules and interaction contracts that apply across products.
- `config/` defines project choices, capability declarations, and likely-failure rules.
- `design/` defines selectable brand recipes and semantic design tokens. A recipe may express personality without replacing expected system behavior.
- `ux/` defines reusable journeys, interaction contracts, states, accessibility, and recovery patterns.
- `platforms/` defines native presentation and input behavior for each platform.
- `modules/` contains optional capabilities. Keep a capability independent until a real product selects it.
- `templates/` contains generated project files; `tooling/` generates, validates, and builds troubleshooting guides.
- `docs/` records product questions, research, decisions, release requirements, and support practices.

Keep the foundation small. Do not add an app feature, dependency, entitlement, account system, backend, purchase flow, or platform target merely to populate the boilerplate. A new module needs a concrete use case and a documented reason to be reusable.

Give agent work a bounded goal, explicit write scope, relevant files, constraints, acceptance evidence, downstream consumers, and a stop condition. One agent owns each shared source during parallel work. Report actual changed files and checks, and hand off cross-lane changes by naming the affected contract. Keep the builder's product decisions distinct from generated suggestions. A concept prompt or checklist is not evidence of a finished icon, app build, device test, or release approval.
Apply the definitions of great, outstanding, exceptional, and timeless in `PRINCIPLES.md` to reviews. A subagent should read that file before proposing a design or implementation and report where the evidence falls short.

## Design and platform rules

- Use SwiftUI as the default for new Apple app interfaces when implementation begins. Use UIKit or AppKit where a specific capability or mature control warrants it.
- Share interaction meaning, state, data models, and simple views where useful. Give each selected platform its own navigation, window, focus, input, and settings behavior. Choose a single multiplatform app target only when code and settings overlap substantially; watchOS uses a separate target.
- Prefer system controls, semantic colors, text styles, SF Symbols, safe areas, and platform conventions. Put brand expression mainly in content, iconography, accent, motion, and copy. Do not hard-code system color values or use Liquid Glass as a general content background.
- Treat Liquid Glass and performance as design and release gates. Let supported system navigation and controls adopt glass; use custom glass sparingly for functional controls with OS fallbacks. Review contrast, reduced transparency, motion, and input across selected devices. Record a representative hardware matrix and measure launch, response, hitches, memory, and energy before claiming broad device support.
- Every identity recipe needs light and dark or other applicable appearances, increased-contrast handling, readable type, and a Reduce Motion alternative. Treat accessibility and localization as design inputs from the start.
- Do not promise support for unannounced hardware or APIs. Add a future platform through an availability review, platform profile, previews, and verification when it exists.
- Revisit selected platform profiles and capability availability for each major OS and SDK release; record compatibility decisions in `docs/compatibility/`.
- For an iPhone app, use `platforms/ios/ADAPTIVE-LAYOUT.md` to test ordinary and Duo layouts. Keep task state independent of presentation, derive layout from the current scene/container, and do not claim hinge or performance behavior without device evidence.

## Capability contract

Before implementing an optional module, document: the user's job; entry and exit points; states and recovery; supported platforms and minimum OS versions; APIs and entitlements; permission timing and denial behavior; data collected, stored, shared, exported, and deleted; privacy manifest implications; accessibility and localization; battery and background behavior; and the evidence needed to verify it.

For `active-activity/`, distinguish the iPhone or iPad Live Activity from a persistent widget. A paired Apple Watch can display the Live Activity in its Smart Stack; a Watch widget or complication is a separate WidgetKit experience. Design the Live Activity for a real event with a beginning and end, useful glanceable status, privacy-safe Lock Screen content, and a way to stop it. Do not use it for advertising or assume the system will display it continuously.

## Product and payment decisions

The boilerplate must ask each future app to state why it should exist, what useful result it delivers, why someone would return, and what ongoing value would justify payment. Treat pricing and conversion benchmarks as hypotheses. Use a subscription only when the selected product supplies continuing value under the current App Review rules; keep one-time purchase possible.

## Verification and release

- Use Xcode previews for representative sizes, states, appearances, large text, and localizations. Validate platform behavior in Simulator and on physical hardware where the behavior depends on hardware or performance.
- Verify the selected app's privacy declarations, required-reason APIs, third-party SDK manifests, permissions, account deletion if accounts exist, purchase restoration if purchases exist, and App Review metadata before release.
- Measure launch responsiveness, interaction hitches, memory, battery use, and crashes for shipped apps. Compare the same journey on representative physical devices and OS versions; keep support and recovery paths clear.
- Report what was actually checked. If Xcode or a device is unavailable, say so and do not claim a build or device test passed.
- Update the smallest relevant specification or checklist when a documented decision changes. Keep generated projects free of boilerplate internals.
- The beginner journey in `config/process.json` owns stable phase and action IDs. Copy edits may change action text, but never reuse or reorder IDs to represent a different task; checklist migration depends on them. Regenerate the dogfood and preview resources after process changes.
- A starter under `templates/starters/` must build, test, and launch; run `make verify-xcode` after changing one and report it as skipped if Xcode is unavailable. Keep it to one task owner and its tests; product screens belong in the app, not the factory.
- A generated file's content change reaches existing apps through `make update`. Do not rename or move a generated path without noting it in the change; the old path becomes a retired file.
- When adding a platform or capability, update `config/troubleshooting.json` with likely failures and first checks only when supported by a current primary Apple source; keep the generated guide specific to selected choices.
