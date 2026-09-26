# Secure and responsive defaults

This is the implementation contract when a product becomes code. The scaffold cannot guarantee a secure or fast app before its data, permissions, network work, and supported devices are known. It can make the safe path the shortest path and require evidence for exceptions.

## Default shape

`Scene → View → task state → operation → storage/system API`

- Views render state and send named actions. Keep I/O, parsing, image decoding, and long work outside view bodies and the main actor.
- One owner manages each task's state. Give saved items stable IDs and explicit loading, empty, success, error, cancellation, and retry states. Preserve drafts through navigation and scene changes.
- Operations have a clear start, completion, cancellation, and idempotency rule. Treat repeated taps, app suspension, and duplicate callbacks as normal inputs.
- Inject storage and external services at the boundary so a test can run a task without a real account, network, purchase, or sensor. Test the state transition and recovery, not the SwiftUI layout implementation.
- Keep shared business meaning separate from platform presentation. A new device may rearrange controls without creating a second copy of the task logic.

## Build, diagnose, and evolve

1. Build in the Swift 6 language mode. A warning you turn off in the first week becomes a migration later. The `--starter ios` project sets this up.
2. Log with `Logger` (subsystem and category). Dynamic strings are redacted by default; mark a value `.public` only when it is not user data. Do not ship `print`. Put an `OSSignposter` interval around slow work before you tune it.
3. Keep test hooks such as launch-environment switches inside `#if DEBUG`. A release build must not read them.
4. Version persisted data from the first release (for SwiftData, a `VersionedSchema`). During a phased release, the old and new versions read the same store, and you cannot roll back a binary.
5. When a defect is in Apple's code, reduce it to a sample project, file it in Feedback Assistant, and record the FB number beside the workaround.

## Privacy and security gates

1. Start with no extra entitlement, background mode, SDK, account, analytics, or network dependency. Add one only for a selected user job, record its data flow, and test denial or absence.
2. Keep credentials out of the repository, logs, previews, and screenshots. Use system credential storage for secrets when a product actually needs them; do not invent encryption around a hard-coded key.
3. Validate external input at the boundary: deep-link destinations, imported files, server data, and URL hosts. Give errors a safe recovery path without printing private content.
4. Keep permission prompts close to the action that needs access. The app must still explain or offer useful work after denial.
5. For a Mac App Store target, use the [App Sandbox](https://developer.apple.com/documentation/security/protecting-user-data-with-app-sandbox) and grant only needed capabilities. Verify the entitlements in the signed build. App Workshop's local bundle uses a sandbox entitlement as a concrete example.
6. Reconcile actual collection, SDK behavior, storage, sharing, deletion, and account behavior with the privacy plan and App Store declarations before release.

## Responsiveness gates

1. Start the app and perform the first useful action on the oldest supported device before broadening scope. Save a baseline with device, OS, build, dataset, and scenario.
2. Keep expensive work asynchronous and cancellable. Render progress honestly, retain user input, and avoid kicking off the same work on every view recomputation.
3. Bound images, lists, caches, and background work. Profile a long session as well as launch, scrolling, and transitions. Extensions get their own memory and time checks.
4. Compare the same task before and after a change using [Xcode performance tools](https://developer.apple.com/documentation/xcode/performance-and-metrics). Fix the cause of hitches or battery use; do not declare a universal performance number without a device baseline.
5. For iPhone, include compact-to-regular scene transitions and restoration from `docs/compatibility/IPHONE-DUO.md` when that file exists.

## Definition of done for a code slice

The primary action completes, duplicate input is harmless, interruption preserves work, denial and failure have recovery, sensitive information stays out of logs, and the measured journey does not regress on a supported device. Record what was actually run in `docs/quality/TEST-MATRIX.md`; leave hardware-only claims pending when hardware is unavailable.

Apple sources checked 2026-09-25: [App Sandbox](https://developer.apple.com/documentation/security/protecting-user-data-with-app-sandbox), [Performance and metrics](https://developer.apple.com/documentation/xcode/performance-and-metrics).
