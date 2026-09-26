# OS and device compatibility review

Use this record when an Apple SDK, major OS, device class, input method, or shared boilerplate version changes. Record a separate row per supported platform and release. A future product is a new review trigger once Apple documents its APIs and behavior; this file makes no advance support promise.

## Release record

| Date | SDK and Xcode | Platform and OS | Device or input class | Current minimum OS | Owner | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| Pending | Pending | Pending | Pending | Pending | Pending | Pending |

## Inspect the change

| Area | Question | Evidence or decision |
| --- | --- | --- |
| Availability | Do selected APIs, targets, extensions, and entitlements compile and run at the minimum OS? | Pending |
| Native behavior | Did navigation, windows, menus, focus, controls, material, or system surfaces change? | Pending |
| Layout and input | Do size classes, safe areas, text sizes, touch, pointer, keyboard, remote, gaze, and assistive input still fit selected devices? | Pending |
| Appearance and icon | Do light/dark, contrast, reduced transparency, motion, icon variants, and store assets remain correct? | Pending |
| Data and privacy | Do storage, sync, permissions, manifests, account flows, and deletion still behave as promised? | Pending |
| Dependencies | Are third-party packages and SDKs compatible, maintained, and privacy-declared? | Pending |
| Performance | Does the same core journey regress in launch, response, memory, energy, or background behavior? | Pending |
| Distribution | Do signing, TestFlight, App Store Connect, review rules, and support claims need an update? | Pending |

## Decide and verify

1. Read the current platform release notes, API availability, HIG, and App Review changes. Record source URLs and the date checked beside each affected decision.
2. Build the existing app with the new toolchain. Keep the oldest supported OS in the test matrix. Check new OS behavior in Simulator, then use physical devices for hardware and performance claims.
3. Run the core user job, recovery path, relevant extensions, and `docs/design/NATIVE-REVIEW.md` rows on affected surfaces. Compare performance using the same scenario and data.
4. For a new platform or device class, define the specific user job, native presentation, input path, data ownership, privacy, support cost, and platform profile before adding a target. For a removed platform, plan data access and user communication.
5. Record a decision: **supported**, **supported with fallback**, **deferred**, or **unsupported**. Name the affected app version, test evidence, open defects, and next review date.

Keep the app's release checklist and store claims aligned with the decision. A scaffold version change is reviewed as a migration; copy only the rules that apply to the existing app and preserve its product decisions.

Apple starting points, checked 2026-09-25: [Developer release notes](https://developer.apple.com/documentation/updates), [Xcode documentation](https://developer.apple.com/documentation/xcode), [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).
