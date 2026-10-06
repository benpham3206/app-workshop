# From first idea to an Apple app ecosystem

This is the learning and delivery path for a future product. The boilerplate can supply prompts, patterns, and checks. A real app begins when a specific user job is chosen.

| Stage | Questions and work | Evidence to leave behind |
| --- | --- | --- |
| 1. Product | Who has the problem, what useful result can the first session produce, why return, and what continuing value could justify payment? | Brief, real user conversations, smallest testable scope. |
| 2. Platform | Which device is the best starting point? Which other devices add a distinct use case? What is the minimum supported OS? | Platform and capability matrix, availability decisions. |
| 3. Experience | What are the entry point, primary action, states, error path, and repeat-use loop? | Flowchart, action contracts, native control choices, accessibility preview. |
| 4. Identity | What should the app feel like, and what may branding change without obscuring system behavior? | Identity recipe, semantic tokens, icon concept and platform variants; native review criteria. |
| 5. Xcode foundation | Create an app target, bundle identifier, scenes, asset catalog or icon file, and test target. Add extensions only for selected system surfaces. | A running empty app in Simulator and on a device; recorded target settings. |
| 6. Data and services | What stays on device? Does data need sync, accounts, export, deletion, or a server? | Data model, ownership and conflict policy, privacy inventory, recovery plan. |
| 7. Vertical slice | Implement one real task from launch through useful result and failure recovery. | Demo on the primary device, source code, focused tests, known limitations. |
| 8. System integration | Add only chosen widgets, Live Activities, App Intents, Watch or Mac experiences, notifications, and background work. | Capability-specific contracts, entitlements, platform checks, failure tests. |
| 9. Distribution | Review the runnable experience; prepare signing, App Store Connect record, privacy answers, screenshots, description, age rating, purchase products if any, and review access. | Native review evidence, archive, TestFlight feedback, completed release checklist. |
| 10. Operation | Watch crashes, performance, support requests, retention, and repeated user jobs; update for OS changes. | Triage log, release notes, compatibility decisions, next product change. |

## What the scaffold already does

- Generates a product brief, flow, identity prompts, action guides, platform profiles, selected module contracts, release prompts, and a likely-failure guide.
- Generates an icon brief for a future product; the icon planner turns a completed brief into concept directions and a finishing checklist.
- Includes a self-contained structure check and an evidence record for native design quality in each generated project.
- Provides a solo-builder operating map, task packets for agents, quality and automation plans, a workboard, and post-release support records.
- Keeps Playful/Kinetic, Calm/Precise, and Dark/Technical as choices per future app.
- Separates event-based Live Activities from persistent widgets and distinguishes shared action meaning from platform presentation.
- Validates selections, refuses to overwrite a nonempty project, and checks deterministic generated contents.

## What still needs a real app

Without `--starter ios`, the scaffold has no Xcode project. The starter gives one target, one task owner, and state tests; it has no product screen, data model, icon artwork, signing identity, backend, App Store Connect record, or product-specific test plan. Those would be guesses before the product and target device are chosen. The first implementation milestone should be a single native app target and one complete task, followed by optional extensions.

## Controls and boundaries

| Mostly system-defined | The app developer controls |
| --- | --- |
| Platform input conventions, native control behavior, accessibility semantics, system permission prompts, widget and activity scheduling limits, App Review requirements. | User job, information architecture, action labels and outcomes, data policy, brand identity, icon artwork, app-specific commands, selected capabilities, error recovery, pricing model when justified. |

Treat a new Apple device or OS as a compatibility review: inspect the available SDK, choose a native presentation, then test. A shared product model does not imply identical screens everywhere.

Apple references (reviewed 2026-09-25): [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), [Xcode target configuration](https://developer.apple.com/documentation/xcode/configuring-a-new-target-in-your-project/), [local packages](https://developer.apple.com/documentation/xcode/organizing-your-code-with-local-packages), [App Store Connect workflow](https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-workflow), [new app record](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app), [App Review submission](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app).
