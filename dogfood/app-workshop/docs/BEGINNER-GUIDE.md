# Your first Apple app, from idea to support

Build one useful task on one primary device first. Add other Apple surfaces when they help that task. Each phase has a small piece of evidence that tells you when to move on.

## Route

1. [Set up the workspace](#1-set-up-the-workspace)
2. [Find a repeated problem](#2-find-a-repeated-problem)
3. [Promise one useful result](#3-promise-one-useful-result)
4. [Choose the first device](#4-choose-the-first-device)
5. [Draw the complete journey](#5-draw-the-complete-journey)
6. [Choose a visual identity](#6-choose-a-visual-identity)
7. [Create the app foundation](#7-create-the-app-foundation)
8. [Build one complete task](#8-build-one-complete-task)
9. [Add useful system surfaces](#9-add-useful-system-surfaces)
10. [Test the whole experience](#10-test-the-whole-experience)
11. [Put it in testers' hands](#11-put-it-in-testers'-hands)
12. [Prepare and ship honestly](#12-prepare-and-ship-honestly)
13. [Support and improve it](#13-support-and-improve-it)

## 1. Set up the workspace

**Aim:** Make your work reproducible before you make screens.

Do this:

- Install and open a compatible Xcode release on a Mac.
- Put the project under source control and record the Xcode and SDK versions.
- Run a tiny starter app in Simulator; use a physical device when the feature depends on hardware.

**Move on when:** A clean checkout that another person could open and run.

**What can go wrong:** Tool versions, signing, or missing assets make later builds fail only on another machine.

**If blocked:** Write down the toolchain and build steps now; keep credentials out of the repository.

[Apple reference](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices)

## 2. Find a repeated problem

**Aim:** Choose a job people already try to complete.

Do this:

- Describe the person and the moment the problem appears.
- Watch or ask a few people how they handle it today.
- Write down the free Apple feature or existing app you must beat.

**Move on when:** A one-sentence user problem with evidence from real behavior.

**What can go wrong:** A clever feature is built before anyone needs it, so there is no reason to return.

**If blocked:** Narrow the idea to one recurring moment and ask people about their current workaround.

[Apple reference](https://developer.apple.com/design/human-interface-guidelines/design-principles)

## 3. Promise one useful result

**Aim:** Know what the person gets in the first session and why they would come back.

Do this:

- Write the first useful result in plain language.
- Describe the repeat-use trigger and the smallest version that delivers it.
- Choose free, one-time, or subscription value only after the ongoing job is clear.

**Move on when:** A brief with first result, return loop, success measure, and non-goals.

**What can go wrong:** Scope expands faster than proof of value, while pricing is chosen from benchmarks rather than this product.

**If blocked:** Cut the first release back to one complete result and treat pricing as a hypothesis.

[Apple reference](https://developer.apple.com/app-store/subscriptions/)

## 4. Choose the first device

**Aim:** Start where the job is easiest to perform well.

Do this:

- Pick one primary platform and minimum OS version.
- List what each additional device would uniquely contribute and choose representative hardware for performance checks.
- Check APIs, entitlements, permissions, and hardware before promising a surface.

**Move on when:** A platform and capability matrix with one primary target.

**What can go wrong:** Supporting every device from day one creates many layouts and tests before the core job works.

**If blocked:** Keep shared meaning and data, but add native device presentations one at a time.

[Apple reference](https://developer.apple.com/documentation/xcode/configuring-a-new-target-in-your-project/)

## 5. Draw the complete journey

**Aim:** Make the action understandable from entry through success and recovery.

Do this:

- Draw launch, first action, result, repeat use, and exit.
- For each important action, specify button label, feedback, failure, retry, and undo.
- Include empty, offline, permission-denied, and accessibility paths that apply.

**Move on when:** A flowchart, action contracts, and state inventory.

**What can go wrong:** Happy-path screens look polished while errors or permissions strand the user.

**If blocked:** Walk the journey with a novice and deliberately trigger a failure before adding polish.

[Apple reference](https://developer.apple.com/design/human-interface-guidelines/)

## 6. Choose a visual identity

**Aim:** Make the product recognizable while keeping native behavior clear.

Do this:

- Select a personality recipe and define semantic colors, type, copy, and motion.
- Use native Liquid Glass navigation and controls where supported; keep the content layer clear and define an earlier-OS fallback.
- Brief the app icon from the product promise; explore several concepts.
- Preview light, dark, contrast, reduced transparency, larger text, reduced motion, and icon variants.

**Move on when:** Identity decisions, design tokens, editable icon source, and reviewed previews.

**What can go wrong:** A pretty mockup hides weak labels, low contrast, or an icon that disappears at small size.

**If blocked:** Test native controls and actual-size icon previews before custom styling spreads.

[Apple reference](https://developer.apple.com/design/human-interface-guidelines/app-icons)

## 7. Create the app foundation

**Aim:** Make the smallest native project that can run and evolve.

Do this:

- Create the app target, bundle identifier, scene, assets, and focused tests.
- Choose local storage and data ownership before adding sync or accounts.
- Add an extension or entitlement only for a selected capability.

**Move on when:** A running native app with recorded project settings and an empty-state preview.

**What can go wrong:** Premature packages, backends, and extensions slow every change and increase signing failures.

**If blocked:** Remove unused layers and make the first target build cleanly before adding another.

[Apple reference](https://developer.apple.com/documentation/xcode/configuring-a-new-target-in-your-project/)

## 8. Build one complete task

**Aim:** Ship a thin path from launch to the promised result.

Do this:

- Implement the action and its real state transitions.
- Make data durable enough for the job and preserve user work on failure.
- Run it on the primary device and fix confusing points.

**Move on when:** A demonstrated useful result, including a failure and recovery route.

**What can go wrong:** Many half-built features create activity without a usable product.

**If blocked:** Stop starting new surfaces until one journey is complete end to end.

[Apple reference](https://developer.apple.com/documentation/swiftui/managing-user-interface-state/)

## 9. Add useful system surfaces

**Aim:** Let people reach the same job in the right context.

Do this:

- Select widgets, Live Activities, Watch, Mac commands, App Intents, sharing, or notifications only for a specific job.
- Define each surface's lifecycle, privacy, fallback, and tap destination.
- Test it on supported hardware and with the main app unavailable or suspended.

**Move on when:** A verified module contract for every selected system surface.

**What can go wrong:** Extensions, background rules, and refresh budgets are assumed to behave like the foreground app.

**If blocked:** Treat each surface as an independent delivery path with its own limits and diagnostics.

[Apple reference](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy/)

## 10. Test the whole experience

**Aim:** Find failures before a stranger does.

Do this:

- Test the core result, restart, offline, denied permissions, large text, VoiceOver, and localization.
- Review Liquid Glass legibility and input behavior in each selected platform and appearance.
- Measure launch, interaction hitches, memory, energy, and long-session behavior on representative physical devices; compare with a recorded baseline.
- Check data lifecycle, privacy declarations, and crashes; run purchase and restore tests if the app sells digital goods.

**Move on when:** A test matrix with device, OS, build, result, and remaining risks.

**What can go wrong:** Simulator success is mistaken for device, account, network, or distribution success.

**If blocked:** Reproduce critical paths on hardware and record exactly what was and was not checked.

[Apple reference](https://developer.apple.com/documentation/xcode/performance-and-metrics)

## 11. Put it in testers' hands

**Aim:** Learn what happens when you are not guiding the user.

Do this:

- Prepare signing and an App Store Connect record for TestFlight where applicable.
- Give testers a task, not a tour of the features.
- Collect confusion, crashes, failed results, and repeated requests.

**Move on when:** A triaged beta feedback list and a stable release candidate.

**What can go wrong:** Friendly testers say the app looks good while the core job remains hard to finish.

**If blocked:** Observe task completion and fix the most repeated block before adding features.

[Apple reference](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/)

## 12. Prepare and ship honestly

**Aim:** Make the build, listing, payment, privacy, and support promise agree.

Do this:

- Prepare screenshots, description, support and privacy URLs, rating, regions, and review access.
- Check signed build, entitlements, app icon, purchases, restore, and export compliance as applicable.
- Choose App Store release or a direct Mac distribution path and complete its requirements.

**Move on when:** An approved release candidate with a complete distribution checklist.

**What can go wrong:** Store metadata or signing describes a different app than the one submitted.

**If blocked:** Run the reviewer path from a clean install and compare every claim with the final build.

[Apple reference](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution)

## 13. Support and improve it

**Aim:** Keep the app useful after launch.

Do this:

- Watch crashes, support requests, reviews, performance, and repeat task completion.
- Fix reliability and confusing recovery before expanding scope.
- Review each new OS and device for compatibility and update the app's promises.

**Move on when:** A support loop, release notes, compatibility record, and next evidence-based change.

**What can go wrong:** The app ships once, then OS changes and unresolved customer friction accumulate.

**If blocked:** Reserve time for maintenance and let observed problems choose the next iteration.

[Apple reference](https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-workflow)
