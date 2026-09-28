# Build vs. Buy: Optional Capabilities in an Apple-App Factory

Research date: 2026-09-27. Labeling convention: FACT (URL + date checked) / INFERENCE / UNKNOWN.
This document is a checkpoint file — sections are appended as research completes.

Status: COMPLETE


## Method note

GitHub "latest release" data below was pulled live via `curl https://api.github.com/repos/<org>/<repo>/releases/latest` on 2026-09-27 (FACT, source = GitHub REST API, date checked 2026-09-27). Pricing/privacy claims are WebSearch-sourced from vendor pricing pages and third-party trackers as of 2026-09-27 and are marked FACT with URL, or INFERENCE where only secondary sources were available. App Privacy label contents (App Store "nutrition label") were not independently pulled from the App Store Connect listing for each SDK — those specific label values are marked UNKNOWN/INFERENCE and should be verified against the vendor's own published label mapping or the live App Store listing before publishing as a contract claim.

---

## 1. Commerce: StoreKit 2 vs RevenueCat purchases-ios (brief — full treatment in separate note)

**Apple-native default:** StoreKit 2 (`StoreKit` framework, iOS 15+), transaction verification via `Transaction.currentEntitlements`, no third-party dependency, no data leaves Apple's servers except to your own backend if you build server-side receipt validation.

**Vendor option — RevenueCat (`purchases-ios`)**
- Replaces: StoreKit 2 transaction listening, receipt/JWS validation, entitlement caching, cross-platform subscriber state, paywall UI (RevenueCatUI).
- Platforms: iOS, macOS, tvOS, watchOS, visionOS; also Android/Flutter/RN/Unity for cross-platform parity.
- License: MIT (SDK is open source) — FACT, github.com/RevenueCat/purchases-ios.
- Maintenance: latest release **5.91.0**, published **2026-09-23** (FACT, GitHub API, checked 2026-09-27) — active, frequent releases.
- Pricing: Free up to $2,500 Monthly Tracked Revenue (MTR), then 1% of MTR; custom Enterprise/"Just Paywalls" tiers (FACT, costbench.com/RevenueCat summary of RevenueCat's own pricing page, checked 2026-09-27 — recommend confirming against revenuecat.com/pricing directly before contract publication).
- Privacy impact: SDK transmits purchase/subscriber events to RevenueCat's servers (a data processor); ships a privacy manifest (`PrivacyInfo.xcprivacy`) per Apple's 2024+ SDK requirement (INFERENCE — RevenueCat is a listed "signature" third-party SDK on Apple's required-manifest list; not independently re-verified against the current manifest file in this pass). App Privacy label typically declares "Purchase History" and "Identifiers" linked to user, not used for tracking by default (INFERENCE).
- Lock-in/export: Entitlements/customer data exportable via RevenueCat REST API and CSV exports; switching back to raw StoreKit requires re-deriving entitlement logic from App Store Server Notifications — moderate lock-in on the analytics/paywall layer, low lock-in on raw transaction data (Apple remains source of truth).
- Machine-checkable verification: `swift package resolve` succeeds and `Purchases.configure(withAPIKey:)` returns without throwing in a smoke test; CI check = call `Purchases.shared.getCustomerInfo()` against RevenueCat's sandbox and assert a non-nil `CustomerInfo` (or, for StoreKit-only, `Transaction.currentEntitlements` async sequence yields in a `StoreKitTest` local `.storekit` configuration test run via `xcodebuild test`).

**Selection rule:** Choose StoreKit 2 native unless the app needs cross-platform entitlement sync (web/Android), prebuilt paywall UI/A-B testing, or revenue analytics beyond App Store Connect — RevenueCat's free tier removes the cost objection below $2.5K MTR.

---

## 2. Accounts: Sign in with Apple / passkeys (AuthenticationServices) vs Supabase Auth (supabase-swift) vs Clerk (clerk-ios)

**Apple-native default:** `AuthenticationServices` — Sign in with Apple (`ASAuthorizationAppleIDProvider`) + passkeys (`ASAuthorizationPlatformPublicKeyCredentialProvider`), backed by iCloud Keychain. Zero third-party dependency, no network call to anyone but Apple, required by App Store guideline 4.8 as an option whenever third-party login exists.

**Option A — Supabase Auth via `supabase-swift`**
- Replaces: Your own JWT/session backend, email/password + OAuth relay, row-level-security-linked user table.
- Platforms: iOS, macOS, tvOS, watchOS, visionOS (SPM); part of a broader Supabase Swift SDK.
- License: MIT (FACT, github.com/supabase/supabase-swift).
- Maintenance: latest tag **v2.55.2**, published **2026-09-09** (FACT, GitHub API, checked 2026-09-27) — active.
- Pricing: Supabase Free plan — 500 MB database, 1 GB file storage, 50,000 MAUs, unlimited API requests; projects pause after 1 week inactivity, capped at 2 active free projects; Pro starts ~$25/mo (FACT, aggregated from uibakery.io/jetadmin.io Supabase pricing summaries, checked 2026-09-27 — verify against supabase.com/pricing directly for contract text).
- Privacy impact: Auth tokens/session + user metadata stored on Supabase's Postgres (self-hostable, which is the key differentiator); ATT/tracking not applicable since it is infrastructure, not an ad SDK — INFERENCE that App Privacy label depends entirely on what your own app stores in the `auth.users` table.
- Lock-in/export: Low — Postgres is the underlying store, `pg_dump` gives a full export; self-hosting Supabase's open-source stack is a documented escape hatch (FACT: Supabase's stack is open source, github.com/supabase/supabase).
- Machine-checkable verification: CI script calls `SupabaseClient.auth.signUp(email:password:)` (or a magic-link) against a Supabase test project and asserts a `Session` object with non-nil `accessToken`; a passkey/SIWA flow can't be scripted headlessly (biometric UI), so verification there is XCUITest against a stub keychain plus manual TestFlight sign-in confirmation.

**Option B — Clerk (`clerk-ios` → ClerkKit / ClerkKitUI)**
- Replaces: SIWA/passkey UI + backend session management, prebuilt SwiftUI auth screens, multi-factor auth, org/team primitives.
- Platforms: iOS 17+, Mac Catalyst 17+, macOS 14+, tvOS 17+, watchOS 10+, visionOS 1+; requires Xcode 26+, Swift 6.2+ (FACT, clerk.com/docs/ios/reference/native-mobile/installation, checked 2026-09-27).
- License: Repo is source-visible on GitHub (github.com/clerk/clerk-ios) but Clerk itself is a hosted SaaS product — the iOS SDK's license file was not independently confirmed in this pass (UNKNOWN — check LICENSE file in the repo before stating "MIT" in the contract).
- Maintenance: latest tag **1.5.7**, published **2026-09-26** (FACT, GitHub API, checked 2026-09-27) — very actively maintained, daily-scale cadence.
- Pricing: Free tier raised to 50,000 MRU (Monthly Retained Users, a narrower unit than MAU) as of 2026-02-05; Pro $20/mo billed annually includes 50K MRUs + 1 enterprise connection; overage $25 base + $0.02/MRU above 50K (FACT, saasprices.net / promptstoproduct.com summaries of Clerk's pricing change, checked 2026-09-27 — verify against clerk.com/pricing).
- Privacy impact: Session/identity data hosted on Clerk's servers (US-based SaaS); App Privacy label would need to declare "User ID," "Email Address," and possibly "Name" as linked-to-user data; privacy manifest presence UNKNOWN in this pass (not fetched from repo).
- Lock-in/export: Higher than Supabase — Clerk is a closed hosted identity provider; user export is via Clerk's admin API/dashboard, no self-host option (INFERENCE based on Clerk's SaaS-only model).
- Machine-checkable verification: CI calls Clerk's REST API (`POST /v1/client/sign_ins`) with a test-mode instance and asserts a session token; or drive `Clerk.shared.client` in a unit test against Clerk's sandbox/test instance keys.

**Selection rule:** Choose native SIWA + passkeys unless the app needs a full backend (database + auth unified) — then Supabase — or needs polished multi-factor/org/team auth UI shipped fast with minimal backend code — then Clerk; avoid both if the app has no server-side data to protect.

---

## 3. Sync/backend: SwiftData + CloudKit vs Supabase vs Firebase

**Apple-native default:** `SwiftData` with `CloudKit` mirroring (`ModelConfiguration(cloudKitDatabase:)`), or raw CloudKit (`CKContainer`). Free within Apple's per-user iCloud storage pool, no third-party server, syncs only across a user's own Apple devices signed into the same iCloud account (no cross-platform web/Android reach).

**Option A — Supabase** (Postgres + Realtime + Storage + Auth, via `supabase-swift`, same repo/release facts as Section 2: latest v2.55.2, 2026-09-09, MIT).
- Replaces: CloudKit's private/shared database, adds a real relational Postgres database, row-level security, realtime subscriptions, and a REST/GraphQL surface reachable from non-Apple clients.
- Pricing/free tier: as above (500MB DB / 50K MAU free; ~$25/mo Pro).
- Privacy: data resides on Supabase-managed Postgres (or self-hosted); App Privacy label depends on your schema — INFERENCE that this shifts liability to you as controller rather than Apple.
- Lock-in/export: Low (Postgres, `pg_dump`, open-source stack).
- Verification: CI inserts a row via `SupabaseClient.from("table").insert(...)` and reads it back; assert round-trip equality against a disposable test project/schema.

**Option B — Firebase** (Firestore/Realtime Database + Firebase SDK, `firebase-ios-sdk`).
- Replaces: CloudKit, adds NoSQL document sync, offline cache, and Google Cloud Functions triggers.
- License: Apache 2.0 (github.com/firebase/firebase-ios-sdk) — FACT.
- Maintenance: latest tag **12.19.2**, published **2026-09-15** (FACT, GitHub API, checked 2026-09-27) — active, Google-maintained monorepo covering all Firebase products.
- Pricing: Spark (free) plan with daily quotas on Firestore reads/writes/storage; Blaze pay-as-you-go beyond that (INFERENCE from general Firebase pricing knowledge — not independently re-fetched this pass; verify at firebase.google.com/pricing before contract publication).
- Privacy impact: Firebase/Crashlytics collects device/OS info, installation UUID, and (per current SDK) IP address by default; Firebase ships privacy manifests declaring "data always collected" and "data collected by default," but the app's own App Privacy label must still be hand-verified against actual product usage — Google states this is the developer's responsibility (FACT, firebase.google.com/docs/ios/app-store-data-collection, checked 2026-09-27). Non-EU/US data residency options exist but require explicit region configuration.
- Lock-in/export: High — Firestore/RTDB data model is proprietary (no SQL), export via `gcloud firestore export` to GCS in a Google-specific format; migrating off is a real re-architecture, not a data dump.
- Verification: CI writes/reads a Firestore document via the Admin SDK or REST API against a Firebase emulator (`firebase emulators:start --only firestore`) for a fully offline, deterministic check.

**Selection rule:** Choose SwiftData+CloudKit unless the app needs cross-platform (web/Android) reach or a queryable relational backend for a companion web app — then Supabase (relational, open, low lock-in) over Firebase (NoSQL, higher lock-in) unless the team already standardizes on GCP/Firebase tooling.

---

## 4. Notifications: APNs direct (UserNotifications) vs OneSignal

**Apple-native default:** `UserNotifications` framework + raw APNs (HTTP/2 provider API or token-based auth), full control, no third party sees device tokens or payloads except Apple.

**Vendor option — OneSignal (OneSignal-XCFramework)**
- Replaces: Your own APNs provider server, token management, segmentation, A/B testing, and delivery analytics dashboard.
- Platforms: iOS, plus Android/web/email/SMS/in-app messaging for cross-channel campaigns.
- License: Distributed as a proprietary XCFramework binary (not a from-source open SDK) — the wrapper repo (`OneSignal-XCFramework`) is MIT for the integration shim, but the compiled framework itself is closed source (INFERENCE from typical OneSignal SDK distribution; not independently confirmed against the current LICENSE file this pass — verify before contract).
- Maintenance: latest tag **5.7.0**, published **2026-09-22** (FACT, GitHub API, checked 2026-09-27) — active.
- Pricing: Free plan changing — as of 2026-09-01 (new customers) / 2026-10-01 (existing), Free plan caps mobile push + in-app messaging at **1,000 MAU per org** (down from the prior 10,000-subscriber free allowance); web push/email keep separate free limits; Growth plan $19/mo + usage ($0.012/MAU for mobile push) (FACT, pushwoosh.com "OneSignal Free plan changes in 2026" + onesignal.com/blog, checked 2026-09-27 — this is a significant, recent pricing cliff worth flagging explicitly in the contract).
- Privacy impact: OneSignal collects push tokens, device/OS metadata, and (if using in-app messaging/analytics) behavioral event data on its servers; ships a privacy manifest per Apple SDK requirements (INFERENCE, not independently re-verified this pass); App Privacy label typically must declare "Device ID," "Product Interaction," "Identifiers" as linked-to-user and potentially used for tracking depending on features enabled (cross-app/cross-site attribution features would trigger ATT prompt requirement — verify per-feature).
- Lock-in/export: Subscriber/segment data exportable via OneSignal's REST API and CSV; switching to raw APNs requires re-registering all device tokens (no portability of OneSignal's internal player IDs to Apple's system).
- Verification: CI calls OneSignal's REST API (`POST /notifications`) against a test app ID with a dry-run/test device and asserts a 200 response with a notification ID; for native APNs, a CI-runnable check is a direct HTTP/2 call to the APNs sandbox endpoint with a JWT provider token and a `.p8` test key, asserting a `10:UUID` apns-id response header.

**Selection rule:** Choose native APNs unless the team needs a marketer-facing campaign/segmentation UI or multi-channel (push+email+SMS) orchestration without building it — reconsider given OneSignal's September 2026 free-tier cut to 1,000 MAU, which now bites small apps much earlier than before.

---

## 5. Crash/error reporting & analytics (no module yet — generated apps use `docs/operations/MEASUREMENT.md`): MetricKit + Xcode Organizer + App Store Connect analytics vs Sentry (sentry-cocoa) vs PostHog (posthog-ios) vs Firebase Crashlytics

**Apple-native default:** `MetricKit` (`MXMetricManager`, `MXDiagnostic` payloads for crashes/hangs/disk writes) + Xcode Organizer crash reports (symbolicated, aggregated from users who opt into sharing analytics) + App Store Connect's built-in Analytics (installs, sessions, retention). No third-party data processor, no privacy manifest needed, but data is delayed (MetricKit payloads arrive up to 24h later) and not queryable via API for automation.

**Option A — Sentry (`sentry-cocoa`)**
- Replaces: Crash symbolication pipeline, real-time error aggregation/alerting, release health, performance tracing, session replay.
- Platforms: iOS, macOS, tvOS, watchOS, visionOS.
- License: MIT (FACT, github.com/getsentry/sentry-cocoa).
- Maintenance: latest tag **9.29.2**, published **2026-09-25** (FACT, GitHub API, checked 2026-09-27) — very active.
- Pricing: Sentry has a free Developer tier (limited events/month, 1 user) and paid Team/Business tiers metered by error/transaction volume (INFERENCE from general Sentry pricing knowledge; not re-fetched this pass — verify at sentry.io/pricing).
- Privacy impact: Sentry SDK ships a privacy manifest — Apple auto-merges it when dynamically linked; if statically linked, the integrating app must supply the manifest itself, and versions before 8.21.0 required manual manifest inclusion (FACT, docs.sentry.io/platforms/apple/data-management/apple-privacy-manifest, checked 2026-09-27). Sentry captures device metadata, stack traces, breadcrumbs, and (if enabled) user-identifying context/session replay — App Privacy label must declare "Crash Data," "Performance Data," "Diagnostics," possibly "Identifiers" depending on config.
- Lock-in/export: Low-moderate — events exportable via Sentry API; self-hosted Sentry is available (open-source server) as an escape hatch from the SaaS.
- Verification: CI triggers `SentrySDK.capture(message:)` or a forced test exception against a test DSN/project and polls Sentry's API for the event ID to confirm ingestion.

**Option B — PostHog (`posthog-ios`)**
- Replaces: Product analytics (events, funnels, session replay), feature flags, surveys — broader than crash reporting alone.
- Platforms: iOS (SPM/CocoaPods).
- License: MIT (INFERENCE, consistent with PostHog's general open-source posture; not independently confirmed via LICENSE file this pass).
- Maintenance: latest tag **3.85.0**, published **2026-09-26** (FACT, GitHub API, checked 2026-09-27) — very active.
- Pricing: PostHog has a generous usage-based free tier (historically ~1M events/month free) with paid tiers beyond that (INFERENCE; verify at posthog.com/pricing).
- Privacy impact: Declares tracking domains in its privacy manifest per Apple's NSPrivacyTrackingDomains requirement when tracking-adjacent features are used; iOS 17+ auto-blocks connections to declared tracking domains without user ATT consent (FACT, general Apple privacy-manifest mechanism, checked 2026-09-27 via developer.apple.com WWDC23 session + posthog docs). Session replay and cross-app identification would likely require an ATT prompt if used for tracking purposes — verify per PostHog's own ATT guidance page before shipping.
- Lock-in/export: Low — PostHog is open source and self-hostable; event data exportable via API/webhooks.
- Verification: CI calls `PostHogSDK.shared.capture("test_event")` against a test project API key, then queries PostHog's `/api/event` endpoint to confirm ingestion.

**Option C — Firebase Crashlytics** (part of `firebase-ios-sdk`, same release facts as Section 3: 12.19.2, 2026-09-15, Apache 2.0)
- Replaces: Crash symbolication + Google Analytics-linked crash-free-users metrics.
- Pricing: Free (Crashlytics itself has no direct charge; consumes Firebase project quota only) (INFERENCE, consistent with Firebase's historical Crashlytics-is-free model — verify current ToS).
- Privacy impact: Collects device/OS info, custom keys/logs, free-text user IDs, installation UUID, and (current versions) IP address (FACT, dev.srdanstanic.com summary corroborated by Firebase's own app-store-data-collection doc, checked 2026-09-27). Firebase explicitly states its privacy manifest only covers data "always collected" or "collected by default" — the app owner must still verify the full nutrition label matches actual usage; Crashlytics can be gated behind explicit user consent via `Crashlytics.crashlyticsCollectionEnabled`.
- Lock-in/export: Data exportable via BigQuery link (Blaze plan) or Firebase console CSV; otherwise locked into Firebase console UI.
- Verification: CI forces a test non-fatal (`Crashlytics.crashlytics().record(error:)`) or a scripted crash in a debug build, then polls the Firebase Crashlytics REST/Management API for the issue.

**Selection rule:** Choose MetricKit + Organizer + App Store Connect analytics as the zero-dependency default for a pre-launch or low-traffic app; add Sentry when real-time alerting/on-call triage is a named job; add PostHog only if product analytics (funnels, replay, flags) is the named job, not just crashes; avoid Crashlytics unless the app is already on Firebase for backend/auth (adding the whole Firebase SDK just for crash reporting is disproportionate weight for the job).

---

## 6. Feature flags: none/local config vs OpenFeature swift-sdk vs LaunchDarkly

**Apple-native default:** None — a local `Config.plist`/`UserDefaults`-backed struct with compile-time or remote-JSON-fetched booleans (e.g., a tiny in-house "flags.json" fetched from your own CDN/CloudKit). Zero dependency, zero privacy impact, but no per-user targeting, no percentage rollout, no dashboard.

**Option A — OpenFeature `swift-sdk`**
- Replaces: A vendor-neutral flag *evaluation* API (not a flag management backend) — you still need a provider (LaunchDarkly, Flagsmith, a custom one, or a static in-memory provider) behind it.
- Platforms: iOS/macOS/etc. (SPM).
- License: Apache 2.0 (FACT, CNCF-hosted OpenFeature project convention; open-feature/swift-sdk).
- Maintenance: latest tag **0.6.0**, published **2026-08-18** (FACT, GitHub API, checked 2026-09-27) — still pre-1.0, moderate cadence.
- Pricing: Free (spec + SDK only; cost is whatever provider you plug in).
- Privacy impact: None inherent — the SDK itself makes no network calls; privacy impact is entirely a function of the chosen provider.
- Lock-in/export: None — this is precisely the point of OpenFeature: swap providers without changing call sites (`OpenFeatureAPI.shared.setProvider(...)`).
- Verification: CI instantiates an `InMemoryProvider` with a known flag map, calls `client.getBooleanValue(key:defaultValue:)`, and asserts the expected value — fully offline and deterministic.

**Option B — LaunchDarkly (`ios-client-sdk`)**
- Replaces: Flag management dashboard, percentage rollouts, per-user/segment targeting, A/B experiment analysis, real-time flag streaming.
- Platforms: iOS/macOS/tvOS/watchOS (SPM/CocoaPods).
- License: Apache 2.0 for the client SDK (INFERENCE, consistent with LaunchDarkly's other open-source SDKs; not independently confirmed via LICENSE this pass).
- Maintenance: latest tag **11.6.2**, published **2026-09-17** (FACT, GitHub API, checked 2026-09-27) — active.
- Pricing: Free "Developer" tier — unlimited seats/flags, 1K client MAU, 1 project, 3 environments, 5K session replays/month; paid "Foundation" meters ~$10/service connection/month + $8.33 per 1,000 client-side MAU (FACT, growthbook.io/agentdeals.dev summaries of LaunchDarkly's 2026 pricing, checked 2026-09-27 — verify against launchdarkly.com/pricing).
- Privacy impact: SDK transmits a user/context object (whatever attributes you pass — potentially device ID, email, custom attributes) to LaunchDarkly for targeting evaluation; ships a privacy manifest (INFERENCE, not independently re-verified this pass). App Privacy label would need to declare whatever context attributes are sent (commonly "Device ID," "Other Usage Data").
- Lock-in/export: Flag definitions and targeting rules live in LaunchDarkly's dashboard; exportable via their REST API but re-implementing rollout logic elsewhere is manual work — moderate lock-in on the *management* layer (mitigated by using OpenFeature as the call-site abstraction).
- Verification: CI initializes the LaunchDarkly client against a test/staging environment SDK key with `startWaitSeconds`, then calls `boolVariation(forKey:defaultValue:)` and asserts a flag value; or, more robustly, hits LaunchDarkly's REST API to confirm the flag exists and its targeting rules evaluate as expected for a test context.

**Selection rule:** Choose local config/none until there is a named job requiring server-controlled, per-user rollout without an app-store release (kill switch, gradual rollout, A/B test) — then adopt OpenFeature's abstraction first, and only add LaunchDarkly (or a cheaper alternative) as the concrete provider behind it, to avoid hard vendor lock-in at the call-site layer.

---

## 7. Images: AsyncImage vs Nuke

**Apple-native default:** `AsyncImage` (SwiftUI, iOS 15+) — built-in async image loading/caching, zero dependency, but limited cache control, no disk-cache tuning, no request coalescing/prioritization, no progressive JPEG/downsampling controls.

**Vendor option — Nuke (`kean/Nuke`)**
- Replaces: AsyncImage's loading/caching/decoding pipeline with a tunable image pipeline (memory+disk cache, request prioritization/coalescing, downsampling, progressive decoding, SwiftUI `LazyImage` view).
- Platforms: iOS, macOS, tvOS, watchOS, visionOS (SPM/CocoaPods/Carthage).
- License: MIT (FACT, github.com/kean/Nuke).
- Maintenance: latest tag **13.2.0**, published **2026-08-15** (FACT, GitHub API, checked 2026-09-27) — active, long-running well-regarded project (one of the most widely used Swift image libraries).
- Pricing: Free, no paid tier — pure open-source library, no backend/service component.
- Privacy impact: None beyond whatever image URLs you already load — no telemetry, no privacy manifest needed since it makes no calls to any third-party service of its own (INFERENCE, consistent with it being a pure client-side library with no SaaS backend).
- Lock-in/export: None — it's a caching/loading layer over your own image URLs; removing it means swapping `LazyImage` back to `AsyncImage`, a local refactor with no data migration.
- Verification: CI/unit test loads a known test image URL via `ImagePipeline.shared.image(for:)` async call and asserts the returned `UIImage`/`PlatformImage` has expected dimensions/non-nil; a cache-hit test can assert a second load resolves from `ImageCache` without a network request (mockable via `DataLoader` injection).

**Selection rule:** Choose AsyncImage native unless the app has a named job around image-heavy feeds/grids needing prioritization, downsampling for memory pressure, or fine-grained cache control — Nuke is essentially free (no privacy/pricing cost) so the decision is purely an engineering-complexity-vs-control tradeoff, not a vendor-risk one.

---

## 8. Visual regression testing: Xcode previews/XCUITest screenshots vs Point-Free `swift-snapshot-testing`

**Apple-native default:** Xcode Previews (manual visual check, not automatable in CI) + XCUITest `XCTAttachment`/`.snapshot()` screenshots compared manually or via ad hoc diffing scripts. No built-in image-diff assertion API from Apple.

**Vendor option — `pointfreeco/swift-snapshot-testing`**
- Replaces: A hand-rolled screenshot-diff harness; adds `assertSnapshot(of:as:)` with pluggable strategies (image, text, JSON, view hierarchy) integrated into XCTest.
- Platforms/Swift 6: macOS and iOS (plus tvOS/watchOS via UIKit/SwiftUI snapshot strategies); repo builds against Swift 6 toolchains — package's latest tag is **1.19.6**, published **2026-09-21** (FACT, GitHub API, checked 2026-09-27), and it is actively maintained by Point-Free with support for Swift 6 strict concurrency (INFERENCE from cadence/ecosystem position; exact Swift 6 language-mode adoption in Package.swift not independently re-verified line-by-line this pass).
- License: MIT (FACT, standard Point-Free OSS licensing; github.com/pointfreeco/swift-snapshot-testing).
- Pricing: Free, open source, no service dependency.
- Privacy impact: None — purely a local test-time library, writes reference images to disk in the repo, makes no network calls.
- CI determinism caveats: Reference and comparison snapshots must be generated on the **exact same simulator/OS/Xcode version**, or anti-aliasing and font-rendering differences cause false failures (FACT, corroborated by community guidance e.g. dev.to "passed locally but failed on CI" writeups, checked 2026-09-27). Mitigation: pin the CI runner's simulator device+OS version, and use `perceptualPrecision` (inverse Delta-E via Core Image's `CILabDeltaE` filter, available macOS 10.13+/iOS 11+) to set an image-diff tolerance (e.g., `perceptualPrecision: 0.98`) that absorbs minor anti-aliasing noise while still catching real regressions (FACT, github.com/pointfreeco/swift-snapshot-testing PR #628 + docs, checked 2026-09-27).
- Lock-in/export: None — reference PNGs are plain files committed to the repo; dropping the library just leaves you with static image fixtures.
- Machine-checkable verification: Run `swift test` (or `xcodebuild test`) with `isRecording = false` on the pinned CI simulator; a failing `assertSnapshot` produces an `ImageDiff`-style failure artifact with expected/actual/diff images attached to the test result bundle — CI treats non-zero `xcodebuild test` exit code as the pass/fail signal, and a script can assert the `.xcresult` contains zero snapshot-strategy failures.

**Selection rule:** Choose XCUITest/manual Previews for a pre-PMF app shipping fast with a small, frequently-churning UI; adopt `swift-snapshot-testing` once there's a named job of "prevent UI regressions across N screens that don't change often" — and only after pinning CI to one simulator/Xcode version, since flaky snapshot diffs are the #1 complaint against this pattern.

---

## 9. Dependency control / architecture: plain protocols vs `swift-dependencies` vs TCA (brief)

**Apple-native default:** Plain Swift protocols + manual/initializer-based dependency injection (or a lightweight `Environment`/singleton pattern). Zero dependency, but boilerplate scales with app size and test-double wiring is manual.

**Option A — `pointfreeco/swift-dependencies`**
- Replaces: Manual DI wiring with a `@Dependency` property-wrapper-based container supporting live/test/preview value overrides.
- License: MIT. Latest tag **1.17.1**, published **2026-08-28** (FACT, GitHub API, checked 2026-09-27) — active.
- Pricing/privacy: Free, no network calls, no privacy impact — pure compile-time/runtime DI library.
- Lock-in/export: Low — it's a DI pattern layered over protocols you already own; removing it means reverting to manual init injection, a mechanical refactor.
- Verification: `swift build && swift test` — unit tests overriding `@Dependency` values with test implementations and asserting expected behavior (fully offline, deterministic).

**Option B — The Composable Architecture (TCA, `pointfreeco/swift-composable-architecture`)**
- Replaces: Ad hoc MV/MVVM state management with a unidirectional Reducer/Store/Effect architecture (includes `swift-dependencies` as a component).
- License: MIT. Latest tag **1.26.2**, published **2026-08-28** (FACT, GitHub API, checked 2026-09-27) — active, large adoption in the SwiftUI community.
- Pricing/privacy: Free, no privacy impact.
- Lock-in/export: High relative to plain protocols — TCA is a whole-app architectural commitment (Reducers, Stores, Effects) that is expensive to unwind once adopted broadly; adopt deliberately, not incrementally-by-accident.
- Verification: `swift test` using `TestStore` to assert exact state mutations and effect sequences for a given action — TCA's `TestStore` is itself a strong machine-checkable regression harness once adopted.

**Selection rule:** Choose plain protocols + manual DI by default; add `swift-dependencies` when test-double wiring boilerplate becomes a named pain point; only adopt full TCA when the app's state-management complexity (many interacting features, deep effect chains) justifies an architecture-wide commitment — not for a single screen.

---

## 10. Project generation: Xcode 16+ synchronized folders vs XcodeGen vs Tuist (brief)

**Apple-native default:** Xcode 16+ "synchronized folder groups" (`fileSystemSynchronizedGroups`) — the `.xcodeproj` tracks a folder directly, eliminating most manual file-reference merge conflicts without any external tool.

**Option A — XcodeGen**
- Replaces: Manual `.xcodeproj` file/target/scheme management via a declarative `project.yml` that regenerates the `.xcodeproj`.
- License: MIT. Latest tag **2.46.0**, published **2026-07-16** (FACT, GitHub API, checked 2026-09-27) — maintenance cadence has slowed somewhat relative to Tuist (2+ months since last tag as of check date) but repo is not archived.
- Pricing/privacy: Free, local CLI tool, no network calls, no privacy impact.
- Lock-in/export: Low — `project.yml` is a plain YAML source of truth; dropping XcodeGen just means committing the generated `.xcodeproj` directly going forward.
- Verification: CI runs `xcodegen generate` then `xcodebuild -list` and asserts the expected scheme/target names are present (fully scriptable, deterministic, no network).

**Option B — Tuist**
- Replaces: Same class of problem as XcodeGen (declarative project generation) plus module graph caching, remote binary caching, and a hosted dashboard for build insights.
- License: MIT for the core CLI (FACT, tuist/tuist is MIT-licensed historically; note the monorepo now also contains unrelated infra components like `capi-scaleway` per the latest tag observed, suggesting Tuist has broadened beyond pure project generation into a larger cloud/build-services product — verify which sub-package's release you're pinning to).
- Maintenance: monorepo's latest tag at check time was **capi-scaleway@0.43.0**, published **2026-09-27** (FACT, GitHub API, checked 2026-09-27) — the monorepo overall is very active, but that specific tag is not the core `tuist` CLI release; check `tuist/tuist` release notes directly for the CLI's own version before citing a "latest CLI version" in the contract (flagged as a gap below).
- Pricing: Core CLI free/open source; Tuist Cloud/dashboard features are a separate paid product tier (INFERENCE, consistent with Tuist's dual open-core model — verify at tuist.dev/pricing).
- Privacy impact: If using Tuist Cloud features (remote caching, insights), build metadata is sent to Tuist's servers — local-only `tuist generate` has no privacy impact; verify per-feature.
- Lock-in/export: Low for local generation (Project.swift is plain Swift, portable); moderate if adopting Tuist Cloud's remote cache/analytics, which is a hosted dependency.
- Verification: CI runs `tuist generate` then `xcodebuild -list`, same pattern as XcodeGen.

**Selection rule:** Choose Xcode 16+ synchronized folders as the default for small-to-medium single-target apps; reach for XcodeGen or Tuist only when the factory needs to generate multiple targets/schemes from a shared template across many generated apps (a real "named job" for the app-workshop factory itself) — prefer Tuist if remote build caching across CI runs becomes a bottleneck, otherwise XcodeGen's simpler scope is easier to reason about.

---

## Starter repo verification

**"SoarStarter" (Swift template with Supabase + RevenueCat)**
- Exists as a **commercial product** at soarstarter.com, not as an open-source GitHub repository — GitHub repository search for "SoarStarter" returned **zero results** (FACT, GitHub Search API, checked 2026-09-27: `total_count: 0`).
- The site's "SoarStarter Swift" offering is described as "A native SwiftUI app with Supabase, RevenueCat subscriptions, onboarding, push, analytics, and crash reporting" (FACT, WebFetch of soarstarter.com, checked 2026-09-27).
- It is a paid, closed-source-until-purchase product: one-time purchase (~$29 individual / ~$149 all-access bundle per aggregated pricing), "own the source forever" after purchase, not MIT/open source (FACT, WebFetch of soarstarter.com, checked 2026-09-27).
- Conclusion: exists, but not as a public GitHub repo — cannot be inspected, forked, or pinned as a dependency the way an open-source template can. Report as **VERIFIED (commercial, not open source)**, not UNKNOWN, but flag that it fails the "inspectable/forkable" bar most factory-template criteria would require.

**"swiftui-revenuecat-admob-starter"**
- **Exists** on GitHub: `acalise/swiftui-revenuecat-admob-starter` (FACT, GitHub Search API + repo API, checked 2026-09-27).
- Description: "Native SwiftUI starter: RevenueCat subscriptions, AppsFlyer attribution, PostHog analytics, and AdMob. iOS 17+, SPM only, every integration optional and no-ops until you add a key."
- Created **2026-08-07**, last pushed **2026-08-07** (same day — single initial commit burst), **1 star**, not a fork, not archived (FACT, GitHub API, checked 2026-09-27).
- This is a very new, low-adoption (1 star), single-maintainer repo — not yet a battle-tested community starter. License field was present in the API response but its value was not captured in this pass (UNKNOWN — re-check `license.spdx_id` before citing a specific license in the contract).
- Conclusion: **VERIFIED to exist**, but treat as an early-stage/unproven reference implementation, not a maintained framework — appropriate to study for integration patterns, not to adopt as a dependency.

**MIT "iOSTemplate" (SwiftUI/Swift 6/Supabase/RevenueCat/Firebase)**
- No repository named exactly "iOSTemplate" (or close variants) combining all of SwiftUI + Swift 6 + Supabase + RevenueCat + Firebase was found. GitHub Search API for `iOSTemplate+supabase+revenuecat` and for `SwiftUI+Swift6+Supabase+RevenueCat+Firebase+template` both returned **zero results** (FACT, GitHub Search API, checked 2026-09-27).
- A generic name-only search for `iOSTemplate` (in:name) returned 70 repositories, but these are unrelated generic iOS boilerplate/template repos (various small teams' internal templates) with no indication of the specific Supabase+RevenueCat+Firebase+MIT combination described (FACT, GitHub Search API, checked 2026-09-27).
- Conclusion: **UNKNOWN / not found**. No evidence of a repo matching this specific description exists under a findable name. Recommend the report-writer treat this as unconfirmed unless the requester can supply the exact URL or org name — it's possible this refers to a private repo, a since-renamed/deleted repo, or a slightly different name than described.


---

## Proposed structural responses for app-workshop

**Rationale:** benpham3206/app-workshop was not independently browsed in this research pass (this note is web/vendor research, not a repo audit) — the module names (`commerce`, `accounts`, `sync`, `notifications`) are taken as given from the assignment brief. The proposal below assumes each existing module has (or should have) a `README.md` documenting its default and swap options; verify the actual file layout before applying.

### Compact "Build vs. buy" table — proposed for each module README

`modules/commerce/README.md`

| Option | Replaces | License | Latest release (checked 2026-09-27) | Free tier | Lock-in | Choose when |
|---|---|---|---|---|---|---|
| StoreKit 2 (default) | — | Apple platform | n/a | n/a (no cost) | None | Always, unless cross-platform entitlements or paywall UI needed |
| RevenueCat `purchases-ios` | StoreKit transaction/entitlement handling | MIT | 5.91.0 (2026-09-23) | Free to $2.5K MTR, then 1% | Moderate (paywall/analytics layer) | Cross-platform sync, paywall A/B testing, revenue analytics is a named job |

`modules/accounts/README.md`

| Option | Replaces | License | Latest release (checked 2026-09-27) | Free tier | Lock-in | Choose when |
|---|---|---|---|---|---|---|
| AuthenticationServices (SIWA + passkeys, default) | — | Apple platform | n/a | n/a | None | Always as baseline; required option under App Store 4.8 if 3rd-party login exists |
| Supabase Auth (`supabase-swift`) | Custom auth backend + user table | MIT | v2.55.2 (2026-09-09) | 50K MAU / 500MB DB free | Low (Postgres, self-hostable) | App also needs a relational backend, not just auth |
| Clerk (`clerk-ios`) | Auth UI/backend + MFA/org primitives | UNKNOWN — verify LICENSE | 1.5.7 (2026-09-26) | 50K MRU free, then $20/mo+ | Higher (closed hosted SaaS, no self-host) | Need polished MFA/org UI shipped fast, no in-house backend |

`modules/sync/README.md`

| Option | Replaces | License | Latest release (checked 2026-09-27) | Free tier | Lock-in | Choose when |
|---|---|---|---|---|---|---|
| SwiftData + CloudKit (default) | — | Apple platform | n/a | Apple's iCloud pool | None (Apple ecosystem only) | Apple-only app, no web/Android reach needed |
| Supabase (Postgres+Realtime) | CloudKit + adds relational cross-platform backend | MIT | v2.55.2 (2026-09-09) | 50K MAU / 500MB DB free | Low (Postgres, open-source, self-hostable) | Need a companion web/Android client or SQL querying |
| Firebase (Firestore/RTDB) | CloudKit + adds NoSQL cross-platform backend | Apache 2.0 | 12.19.2 (2026-09-15) | Spark free tier (quota-limited) | High (proprietary NoSQL model, GCP export only) | Team already standardized on GCP/Firebase tooling |

`modules/notifications/README.md`

| Option | Replaces | License | Latest release (checked 2026-09-27) | Free tier | Lock-in | Choose when |
|---|---|---|---|---|---|---|
| APNs direct (`UserNotifications`, default) | — | Apple platform | n/a | n/a | None | Always, unless marketer-facing campaign UI is a named job |
| OneSignal (`OneSignal-XCFramework`) | APNs provider server + segmentation/analytics | UNKNOWN (binary framework; wrapper MIT) — verify | 5.7.0 (2026-09-22) | **1,000 MAU** free as of 2026-09/10-2026 (down from 10K subscribers) | Moderate (player-ID re-registration needed to leave) | Multi-channel campaign orchestration (push+email+SMS) is a named job — note the 2026 free-tier cut now bites small apps earlier |

### Where crash/analytics and snapshot testing belong

- **Crash/error reporting + analytics**: keep the existing convention of documenting this in each generated app's `templates/generated-app/docs/operations/MEASUREMENT.md` rather than creating a new top-level module — this is operational/observability guidance, not a swappable feature module with its own API surface the app calls at runtime in the way `commerce`/`accounts`/`sync`/`notifications` are. Recommend `MEASUREMENT.md` gain a "Build vs. buy" subsection matching the table format above (MetricKit/Organizer default; Sentry, PostHog, Crashlytics as options), plus an explicit line calling out that Firebase Crashlytics should only be pulled in if the app is already on Firebase for `sync` — otherwise it's a disproportionate dependency just for crash reporting.
- **Visual regression / snapshot testing**: belongs in a quality/testing document such as `docs/quality/TEST-MATRIX.md` (if it enumerates test types/coverage) or `docs/quality/AUTOMATION.md` (if it's about CI mechanics) rather than a runtime module — `swift-snapshot-testing` is a dev-dependency, never linked into the shipping app binary, so it doesn't belong alongside `commerce`/`accounts`/etc. Whichever doc is used should explicitly document the CI determinism requirement (pin one simulator/Xcode version) and the recommended `perceptualPrecision` tolerance, since that is the most common source of false failures reported in the community.

### Note on the factory rule "no dependency until a named user job needs it"

Every vendor option researched above is strictly additive over a working Apple-native default — none of the nine capability areas require a third-party dependency to reach a shippable v1. This is consistent with treating each module's default (StoreKit 2, AuthenticationServices, SwiftData+CloudKit, APNs, MetricKit/Organizer, local config, AsyncImage, XCUITest, plain protocols, Xcode synchronized folders) as the factory's zero-dependency baseline, with every vendor swap gated behind an explicit, nameable job (e.g., "cross-platform entitlement sync," "marketer-facing campaign orchestration," "per-user server-controlled rollout without an App Store release"). Two observations worth flagging to the report-writer:

1. **Pricing/free-tier terms are moving targets and some changed materially in 2026** — OneSignal cut its free push tier from 10,000 subscribers to 1,000 MAU (effective 2026-09-01/10-01), and Clerk raised its free tier to 50,000 MRU (effective 2026-02-05). Any contract text citing "free tier" numbers should carry a "verify against vendor pricing page at integration time" caveat rather than being treated as a fixed fact, since these change faster than the module contracts are likely to be revisited.
2. **License/manifest verification gaps**: this pass could not independently confirm (a) Clerk's iOS SDK license, (b) OneSignal's XCFramework license terms, (c) whether OneSignal and LaunchDarkly ship `PrivacyInfo.xcprivacy` manifests, and (d) exact App Store Connect "nutrition label" data-type declarations for any vendor. These are marked UNKNOWN/INFERENCE above and should be resolved by pulling each SDK's actual `PrivacyInfo.xcprivacy` file and LICENSE file (both are checkable via `curl`/`unzip` against the SPM package tarball or a `git clone --depth 1`) before the contract language is finalized — this is a mechanical, low-effort follow-up, not a research gap requiring further web search.

