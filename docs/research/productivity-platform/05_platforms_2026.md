# App Workshop platform recommendation

> Corrections from [`06_factcheck.md`](06_factcheck.md) are applied inline and marked **[FC]**.


**INFERENCE — decision:** Generate the first productivity starter for **iPhone and iPad as one iOS app target, with a native macOS target and a separate watchOS app target**. Share product logic and models in Swift packages, but keep each platform’s app lifecycle, navigation, and interface native. Set initial minimum OS versions to **iOS/iPadOS 18, macOS 15, and watchOS 11**. Use **Xcode 27.1 and Swift 6 language mode** for release builds; use newer betas only for deliberate compatibility checks.

**INFERENCE — WWDC 2026 priority:** Make the app adapt to changing window and display sizes, especially iPhone Duo, and use current system UI conventions. Treat App Intents and Foundation Models as product capabilities to add where they serve a real user task; neither requires every productivity app to add AI. The submission deadlines below are the enforceable SDK requirements.

**FACT — date and evidence:** Live Apple and vendor sources were checked **October 19, 2026**. I read the requested `README.md`, `GOAL.md`, commerce module, and two first-subscriber research documents first. The repo’s commerce module still describes StoreKit 2 as its default and RevenueCat as conditional; that conflicts with the owner’s newer decision to default to RevenueCat. This is a research finding, not a file change.

## Current versions and App Store submission requirements

| Item | Status on October 19, 2026 |
|---|---|
| iOS | **FACT:** iOS 27.0.1 is the latest stable release shown in Apple’s release list. [Apple releases](https://developer.apple.com/news/releases/) |
| iPadOS | **FACT:** iPadOS 27.0.1 is the latest stable release shown in Apple’s release list. [Apple releases](https://developer.apple.com/news/releases/) |
| macOS | **FACT:** macOS 27.0.1 is the latest stable release shown in Apple’s release list. [Apple releases](https://developer.apple.com/news/releases/) |
| watchOS | **FACT:** watchOS 27.0.1 is the latest stable release shown in Apple’s release list. [Apple releases](https://developer.apple.com/news/releases/) |
| visionOS | **FACT:** visionOS 27.0.1 is the latest stable release shown in Apple’s release list. [Apple releases](https://developer.apple.com/news/releases/) |
| Xcode release | **FACT:** Xcode 27.1 was released October 15. It includes Swift 6.4 and the iOS 27.1 SDK; the other platform SDKs are version 27. [Xcode 27.1 release](https://developer.apple.com/news/releases/?id=10152026a), [Xcode requirements](https://developer.apple.com/xcode/system-requirements/) |
| Xcode beta | **FACT:** Xcode 27.2 beta 3 was released October 14. [Xcode 27.2 beta 3](https://developer.apple.com/news/releases/?id=10142026b) |
| Swift | **FACT:** Xcode 27.1’s compiler is Swift 6.4. It supports Swift 6, Swift 5, Swift 4.2, and Swift 4 language modes. **INFERENCE:** Set generated targets to Swift 6 language mode, then make concurrency warnings and errors part of the build acceptance criteria. [Xcode requirements](https://developer.apple.com/xcode/system-requirements/) |

**FACT — submission threshold effective April 28, 2026:** App Store Connect submissions require Xcode 26 or later, using the iOS/iPadOS 26 SDK for iOS and iPadOS apps, and the corresponding version 26 SDK for watchOS, visionOS, and tvOS. [Apple’s SDK requirements](https://developer.apple.com/news/?id=ueeok6yw)

**FACT — upcoming threshold starting April 2027:** iOS and iPadOS submissions must use the iOS/iPadOS 27 SDK or later and target iOS 15 or later. watchOS and visionOS submissions must use their version 27 SDK or later. Apple’s published threshold does not state a macOS SDK or deployment-target minimum. [Apple submission requirements](https://developer.apple.com/app-store/submitting/)

**FACT — Xcode 27.1 SDK nuance:** App Store Connect accepted Xcode 27.1 RC uploads from October 5 and the final release from October 15 **[FC]**. Xcode 27.2 RC is listed for October 19 **[FC]**. The April 2027 rule says **27 SDK or later**; it does not specifically require iOS 27.1. [App Store Connect release notes](https://developer.apple.com/help/app-store-connect/release-notes/)

## Recommended deployment targets

| Target | Recommendation | Basis and limits |
|---|---|---|
| iPhone and iPad | **INFERENCE: iOS/iPadOS 18** | A reasonable baseline for a new app that wants modern WidgetKit controls and SwiftData while avoiding an iOS 27-only audience. Keep version 27 APIs behind availability checks. |
| Mac | **INFERENCE: macOS 15** | A practical baseline for a new native Mac app using current SwiftUI and system capabilities. Keep version 27 behavior optional. |
| Apple Watch | **INFERENCE: watchOS 11** | A reasonable baseline for interactive widgets and controls. Keep the watch app focused on short, glanceable tasks and background-limited work. |
| visionOS | **INFERENCE: no target in the first build** | The owner’s first platform set does not include a visionOS app. Add one when the product has a defined spatial use case; the current shipping OS alone is not a reason to create a target. |

**FACT — adoption evidence:** Apple reported that, by February 2026, more than 74% of iPhones introduced in the previous four years had updated to iOS 26, and over 66% of iPads introduced in that period had updated to iPadOS 26. This is **not** adoption across all active devices and does not establish a deployment-target threshold. Apple’s source does not provide comparable current macOS or watchOS adoption data here. [Apple Environmental Progress Report 2026](https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2026.pdf)

**UNKNOWN:** I could not confirm an October 2026 Apple-published, all-device OS adoption breakdown suitable for choosing minimum deployment targets across iOS, macOS, and watchOS. The target versions above are engineering recommendations, not Apple requirements or a market-share forecast.

## Generated target and extension structure

| Surface | Recommendation |
|---|---|
| iOS and iPadOS app | **INFERENCE:** One iOS app target serves both iPhone and iPad. Derive layout from the current scene/container size, not device-name assumptions. |
| macOS app | **INFERENCE:** Use a separate native macOS target sharing domain and data packages. This keeps Mac windows, menus, settings, keyboard behavior, and sandbox decisions explicit. A single multiplatform target is possible, but is a poorer default when the product needs distinct Mac behavior. |
| Watch app | **FACT:** Use a watchOS app target. For a companion watch app, Apple’s sample uses bundle IDs derived from the iOS app bundle ID and a `WKCompanionAppBundleIdentifier`. **INFERENCE:** Keep shared business logic in a package; do not make Watch UI or background behavior depend on the phone always being available. [Apple Watch Connectivity sample](https://developer.apple.com/documentation/watchconnectivity/transferring-data-with-watch-connectivity) |
| Widgets and complications | **INFERENCE:** Share WidgetKit source and data contracts, but build the extension targets needed by the iOS/iPadOS, macOS, and watchOS app bundles. WidgetKit supports widgets across these platforms; Watch complications and widgets have their own platform behavior. [Creating a WidgetKit extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension), [configurable widgets and complications](https://developer.apple.com/documentation/widgetkit/making-a-configurable-widget) |
| App Intents | **FACT:** Put intents in the app bundle when they need to bring the app forward. An App Intents extension is optional and runs intents in the background; it is not a mandatory companion target for Shortcuts, Spotlight, or Siri. **INFERENCE:** Start with intents in the app and widget targets, then add an App Intents extension only when the background execution need is clear. [Apple intent runtime guidance](https://developer.apple.com/documentation/appintents/configuring-the-runtime-behavior-of-your-app-intents), [App Intents extension](https://developer.apple.com/documentation/appintents/app-extension) |
| Live Activities | **FACT:** Live Activities use ActivityKit and WidgetKit, so their UI belongs in a widget extension. Active activities can appear on iPhone/iPad, the paired Watch Smart Stack, and the paired Mac menu bar. The Mac presentation launches iPhone Mirroring when selected. [ActivityKit](https://developer.apple.com/documentation/activitykit), [Live Activities HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities) |
| Control widgets | **FACT:** WidgetKit controls use App Intents to perform actions from places such as Control Center, Lock Screen, and the Action button. **INFERENCE:** Put a control in the appropriate platform’s widget extension and make its action finish and persist before returning. [Creating controls](https://developer.apple.com/documentation/widgetkit/creating-controls-to-perform-actions-across-the-system) |
| App Groups | **FACT:** App Groups provide a shared local container and IPC between entitled apps and extensions. Register a `group.` identifier and add the matching entitlement to every target that accesses it. **INFERENCE:** Use App Groups for small local handoff/cache data; they are not cross-device sync. [Configuring App Groups](https://developer.apple.com/documentation/xcode/configuring-app-groups), [WidgetKit shared-data guidance](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) |

**FACT:** Widgets, complications, and Live Activities run as separate processes from the host app. Their visible data must be prepared for system rendering, and sensitive content should be redacted appropriately. Widget and Live Activity actions should handle failure and stale data. [WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy), [interactive widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/adding-interactivity-to-widgets-and-live-activities)

## Data and sync

| Choice | Recommendation |
|---|---|
| SwiftData | **INFERENCE:** Default to SwiftData for a new, Apple-only productivity app with straightforward local models and CloudKit-compatible sync needs. It is the thinnest native starting point. |
| Core Data | **FACT:** Core Data supports local persistence, CloudKit mirroring, persistent history, conflict handling, and lightweight, staged, or manual migrations. **INFERENCE:** Prefer it where migration control, mature CloudKit behavior, or existing Core Data investment matters more than a simpler model layer. [Core Data](https://developer.apple.com/documentation/coredata/) |
| GRDB | **FACT:** GRDB is a third-party toolkit for SQLite application development. **INFERENCE:** Choose it when explicit SQL, relational queries, and database control are product requirements and the team accepts ownership of sync, migration, and integration. GRDB is not itself a CloudKit sync layer. [GRDB.swift](https://github.com/groue/GRDB.swift) |
| SwiftData with CloudKit | **FACT:** Automatic sync requires the iCloud capability and remote-notification background mode. CloudKit does not enforce SwiftData unique constraints and requires optional relationships; changes sync asynchronously. **INFERENCE:** Model for eventual sync, make identifiers conflict-safe in app logic, and avoid promising immediate cross-device consistency. [SwiftData CloudKit guidance](https://developer.apple.com/documentation/swiftdata/syncing-model-data-across-a-persons-devices) |
| Shared widget/Watch data | **FACT:** App Groups share data among entitled targets on the same device. **INFERENCE:** Keep this store small and define who writes each value; it is distinct from a CloudKit database and does not synchronize devices by itself. [App Groups](https://developer.apple.com/documentation/xcode/configuring-app-groups) |
| WatchConnectivity | **FACT:** Use `WCSession` for communication with the paired iPhone app: immediate messages when reachable, latest-value application context, or queued background transfers. Background delivery is not instantaneous; Apple says to test transfers on paired hardware because Simulator does not support `transferUserInfo`. [WatchConnectivity](https://developer.apple.com/documentation/watchconnectivity/wcsession), [transferUserInfo](https://developer.apple.com/documentation/watchconnectivity/wcsession/transferuserinfo%28_%3A%29) |
| Watch CloudKit | **INFERENCE:** Use CloudKit as the shared data source when iPhone, iPad, Mac, and Watch need independently available copies under the person’s iCloud account. Use WatchConnectivity for prompt pair-specific handoff. Do not make both systems competing authorities for the same mutable record. |

## WWDC 2026 changes that affect a productivity app

### Adaptive layout and iPhone Duo

**FACT:** Apple announced iPhone Duo availability for October 23, 2026; as of October 19, it is not yet available to customers. App submissions are open. Apple says apps built with the iOS 27 SDK resize dynamically on Duo. Apps built with iOS 26 or earlier still run, but do not adapt to all layouts. [Prepare and submit for iPhone Duo](https://developer.apple.com/news/?id=kkphp5qo), [iPhone Duo preparation](https://developer.apple.com/iphone-duo/prepare/)

**FACT:** The **iOS 27.1 SDK** enables the full-screen edge-to-edge presentation on Duo and vertical placement of standard navigation and toolbar buttons. iOS 27 already provides dynamic resizing, but the 27.1 presentation uses more of the display. Apple’s guidance calls out hardcoded screen sizes, fixed orientations, and assumptions based on device type as layout risks. [Apple iPhone Duo Tech Talk](https://developer.apple.com/videos/play/tech-talks/111461/)

**FACT:** Apple says Duo screenshots become required for app submissions beginning April 2027. [App Store Connect release notes](https://developer.apple.com/help/app-store-connect/release-notes/)

**INFERENCE:** Make scene/container size the layout input. Audit `UIScreen.main`, fixed orientations, and idiom-based layout decisions. For SwiftUI, use container-aware layout tools such as `GeometryReader` or `onGeometryChange`; verify folded, unfolded, rotated, and resized states. The new `ReservedRegion` API is relevant when custom controls need safe placement near system interface areas; it is not required for ordinary adaptive SwiftUI layouts. [iPhone Duo preparation](https://developer.apple.com/iphone-duo/prepare/)

### Liquid Glass

**FACT:** Apple’s version 27 refinements improve readability by diffusing content behind Liquid Glass, add stronger edge separation and specular highlights, and let people adjust the material’s appearance. Standard SwiftUI, UIKit, and AppKit controls receive system updates; macOS 27 also adds support for the “show borders” environment value. [WWDC26 Platforms State of the Union](https://developer.apple.com/videos/wwdc2026/102/), [WWDC26 design guide](https://developer.apple.com/wwdc26/guides/design/)

**INFERENCE:** Use standard navigation, toolbars, and controls first. Keep custom glass limited to functional controls and test contrast, increased contrast, and reduced transparency. A productivity app should preserve clear content hierarchy when users personalize the material.

### App Intents, Spotlight, Siri, and Visual Intelligence

**FACT:** WWDC26 emphasizes App Intents schemas for making app content and actions understandable to Siri and Apple Intelligence. Entity schemas can contribute content to Spotlight’s semantic index; intent schemas expose actions. The new View Annotations API can connect visible UI content with entities. [WWDC26 Apple Intelligence guide](https://developer.apple.com/wwdc26/guides/apple-intelligence/)

**FACT:** App Intents can return interactive snippets so a person can review a result and take a follow-up action without leaving the current context. Intents invoked from Control Center cannot show snippets. [Interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets)

**FACT:** Visual Intelligence now supports app integrations on iPad and Mac as well as iPhone. Apps can receive a semantic content descriptor, query their entities, and return relevant results. [Visual Intelligence](https://developer.apple.com/documentation/visualintelligence/), [WWDC26 Visual Intelligence session](https://developer.apple.com/videos/play/wwdc2026/297/)

**INFERENCE:** Model a productivity app’s core nouns (such as task, project, note, or timer) as App Entities, and expose common actions as intents. Add semantic Spotlight indexing and Visual Intelligence queries when the app has content a person can meaningfully find that way; these capabilities should not be generated as empty boilerplate.

### Foundation Models and other relevant changes

**FACT:** The Foundation Models framework now supports the on-device Apple model, Private Cloud Compute models, and other providers that conform to Apple’s `LanguageModel` protocol. WWDC26 adds multimodal image prompts, Vision tools such as OCR and barcode readers, Dynamic Profiles, and an Evaluations framework. Apple says model access depends on device and region support for Apple Intelligence; code must check availability and provide a fallback. [Foundation Models](https://developer.apple.com/documentation/foundationmodels), [model availability guidance](https://developer.apple.com/documentation/foundationmodels/generating-content-and-performing-tasks-with-foundation-models), [WWDC26 Foundation Models updates](https://developer.apple.com/documentation/updates/foundationmodels)

**FACT:** Apple documents model guardrails and acceptable-use requirements, but also says safety systems may miss context-specific harm. **INFERENCE:** Treat model output as untrusted, keep consequential edits under user control, and test refusals, unavailable models, and incorrect output. Do not make local user data depend on Apple Intelligence being enabled. [Foundation Models safety](https://developer.apple.com/documentation/foundationmodels/improving-the-safety-of-generative-model-output), [acceptable-use requirements](https://developer.apple.com/support/terms/acceptable-use-requirements-for-the-foundation-models-framework/)

**FACT:** UIKit apps built with the latest SDK must use the UIScene lifecycle or they will not launch. WWDC26 also highlights that iPhone apps can be resized in iPhone Mirroring on Mac and moved to an external display on iPad. [WWDC26 UIKit modernization](https://developer.apple.com/videos/play/wwdc2026/278/)

**INFERENCE:** A new SwiftUI starter already uses scene-based app structure; keep it that way and avoid generating UIKit lifecycle assumptions that bypass scenes. Treat Foundation Models, Visual Intelligence, and advanced App Intents as optional modules driven by the product brief.

## Build and review pitfalls

- **FACT:** Entitlements must be configured for the target that uses the capability. App Group identifiers must match across participating targets, and restricted entitlements must be authorized by provisioning profiles. **INFERENCE:** Generate and inspect signing settings per target; do not assume the host app’s capability automatically applies to extensions. [App Groups](https://developer.apple.com/documentation/xcode/configuring-app-groups), [Apple capability configuration](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app)

- **FACT:** Apple’s watch connectivity sample derives Watch and widget bundle identifiers from the iOS app identifier and configures `WKCompanionAppBundleIdentifier`. **INFERENCE:** Generate the watch bundle metadata and target nesting from Xcode’s current Watch template; avoid hand-assembling identifiers from an unrelated prefix. [Apple WatchConnectivity sample](https://developer.apple.com/documentation/watchconnectivity/transferring-data-with-watch-connectivity), [changing bundle identifiers](https://developer.apple.com/documentation/xcode/changing-the-bundle-identifier)

- **FACT:** Privacy manifests describe collected data and required-reason API use for apps and third-party SDKs, and Xcode uses target membership when bundling them. **INFERENCE:** Audit the built app and each embedded extension or SDK bundle; a manifest in the repository is not proof that the relevant built bundle contains it. [Privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files)

- **FACT:** Apple requires a privacy manifest and signature for SDKs on its listed third-party SDK requirements page when included in an applicable submission. **INFERENCE:** Because RevenueCat is the selected default purchase layer, verify the exact SDK version, signature, manifest, declared data collection, and target inclusion for every release. [Third-party SDK requirements](https://developer.apple.com/support/third-party-SDK-requirements/)

- **FACT:** App Review evaluates apps, extensions, and submitted metadata; extension targets have their own entitlements, bundle identifiers, and runtime constraints. [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [Apple extension and bundle documentation](https://developer.apple.com/documentation/xcode/changing-the-bundle-identifier)

- **INFERENCE:** Make restore, subscription management/cancellation guidance, refund/support routing, and account deletion part of the customer-facing flow where applicable. Keep the creator’s revenue, crash, review, and release tools in an operator-facing console; they are not customer account features. The factory’s existing commerce contract already calls out purchase/restore entry points, entitlement ownership, refunds, billing issues, and support.

## Unknowns and scope

**UNKNOWN:** The exact Apple App Review interpretation of any future iPhone Duo screenshot or layout dispute cannot be established from launch guidance alone; recheck the live guidelines and review feedback when the product is submitted.

**UNKNOWN:** This research did not validate a generated Xcode project, physical Watch transfer, CloudKit behavior across real accounts, or an App Store submission. Those need separate implementation and device evidence.

**Not checked:** I did not investigate third-party OS adoption estimates, pricing estimates, or non-Apple claims that are unnecessary to this decision. No repository files were changed.

