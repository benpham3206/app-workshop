# Productivity platform: research report

Research date: 2026-10-19. Status: research only. Nothing here is built. Each recommendation needs Ben's yes before a build lane starts.

Sources: research lanes on `gpt-6-luna` (`01`–`05`, `07_website.md`, `08_little_things.md`, `09_gaps.md`) and one independent fact-check lane on `gpt-6.1-sol`, high effort (`06_factcheck.md`, covering 01–05). Labels follow the lanes: FACT has a URL and a check date; ESTIMATE is a named third-party figure; INFERENCE is a judgment. Change proposals are in [`LEDGER.md`](LEDGER.md). Follow-up sessions added a measured visual teardown of 16 premium app sites ([`10_visual_teardown.md`](10_visual_teardown.md): only tldraw shows the live product as its hero; default site tokens in §5) and a review-mined trade-tool validation ([`11_trade_tools.md`](11_trade_tools.md) with [`11_trade_tools_evidence.csv`](11_trade_tools_evidence.csv): a one-time-purchase pipe-trades calculator scores 80).

## Verdict

**The point:** read a market, find what is missing, then use App Workshop and the principles skills to build fast, with the polish already built in. The factory is the second half of that loop. The first half, market → gap, has no method in the factory yet: the `problem` phase in `config/process.json` has three generic actions. The proposed fix and a first scored gap scan are in [`09_gaps.md`](09_gaps.md): a free-data method (iTunes Search API, the 500-review feed, category charts, Reddit, Trends), a weighted 0–100 rubric with a 70 gate, and 10 scored candidates.

**The best gap found so far is not a planner.** At least 12 of the US top 50 *paid* productivity apps are trade and field tools, and several sell while stale and poorly rated (Pipe Fitter Calculator: 3.6 stars, last updated 2017; Easy Offset: 2018). People already pay for these tools, and the quality gap is exactly what the factory's built-in polish fixes. It also fits Ben's mechanical engineering domain. The lane's own top three (low-setup ADHD planning, a routine overrun timer, a student study planner) form one cluster against a strong incumbent (Tiimo), so treat them as one bet.

**The timing:** iPhone Duo goes on sale on **2026-10-23**. Apps built with the iOS 27.1 SDK fill the whole display (FACT, `05_platforms_2026.md`). How many incumbents have adapted is not measured (UNKNOWN); the gap lane checks it. A new form factor is the cheapest gap window there is, and the factory already has the Duo layout contract (`platforms/ios/ADAPTIVE-LAYOUT.md`).

1. **The market does not give a clean "top 20 by revenue" list, and we do not need one.** Public data separates downloads (AppTweak, both stores) from grossing rank (Appfigures, US iPhone). Productivity grossing is now led by AI assistants and cloud/office bundles (ChatGPT, Claude, Gemini, Google One, Dropbox, Microsoft 365). The useful benchmark for a solo-built app is the indie tier: Things, Todoist, TickTick, Fantastical, Goodnotes, Bear, Day One, Structured, Tiimo, Streaks, Drafts, Flighty. They share one shape: **one dependable core job, many quick ways into it across iPhone, iPad, Mac, and Watch, and a subscription or one-time purchase tied to continuing value.** See [`01_market.md`](01_market.md).
2. **The boilerplate should cover three sides, and the factory already owns two of them as written contracts.** The work is to turn the contracts into working, selectable code and to add the creator side. See [the three-sided map](#the-three-sided-map).
3. **Do not compete with Bitrig on the build loop.** Bitrig already does plain words → Xcode project → Simulator → App Store Connect upload, with RevenueCat setup. Its Pro plan is $15/month. App Workshop should win on what Bitrig does not show: **evidence gates, honest release states, a creator console, and a clean operator-to-client handoff.** See [`03_bitrig_and_peers.md`](03_bitrig_and_peers.md).
4. **RevenueCat works as the default, with a per-platform gap.** Its Paywalls and Customer Center do not cover every Apple platform (see [platform gaps](#revenuecat-platform-gaps)). The Mac and Watch targets need native StoreKit fallbacks for manage, cancel, and refund.
5. **The creator console is feasible as read-only first.** RevenueCat API v2 and the App Store Connect API expose revenue, customers, builds, TestFlight, reviews, analytics, and performance data. Grow the console from the factory's existing Mac app (`dogfood/app-workshop`), not as a new product.

## The three-sided map

**Tier** means: **Core** (every generated app gets it), **Module** (generated when the selection or preset names it), **Switch** (a small opt-in feature inside a module, off by default, set in `project.json`), **Later** (do not build until a product needs it). Evidence for each surface, its App Review rules, and its acceptance test is in [`02_surfaces.md`](02_surfaces.md).

### User: the person using the app

| Surface | Tier | Native implementation |
| --- | --- | --- |
| Core list / detail / editor, empty and error states | Core | SwiftUI, `NavigationSplitView`, SwiftData |
| First run reaches one useful result, no account wall | Core | SwiftUI + TipKit |
| Local persistence, offline-safe, undo | Core | SwiftData, `UndoManager` |
| Accessibility, Dynamic Type, Reduce Motion, localization | Core | SwiftUI modifiers, String Catalogs |
| Adaptive layout (iPhone, iPad, iPhone Duo) | Core | Scene/container size, never device model |
| In-app search | Core | SwiftUI `.searchable` |
| Import / export (user owns the data) | Core | `FileExporter`, `Transferable`, stable JSON |
| App Intents for capture and lookup; Shortcuts; Spotlight | Module `app-intents` (default on in productivity presets) | `AppIntent`, `AppEntity`, `AppShortcutsProvider`, Core Spotlight |
| Widgets (Home, Lock, Mac, StandBy), Controls, Action button | Module `widgets` | WidgetKit, `ControlWidget` |
| Live Activities (Lock Screen, Dynamic Island, Watch Smart Stack, Mac menu bar) | Module `active-activity` | ActivityKit |
| Reminders and notifications | Module `notifications` | UserNotifications |
| Share extension quick capture | Module `share` | Share extension + App Group |
| iCloud sync | Module `sync` | SwiftData + CloudKit (optional relationships, no unique constraints) |
| Mac: menus, keyboard, windows, menu-bar quick entry | Core when Mac is selected | `Commands`, `MenuBarExtra` |
| Watch: capture, view, complete; complication | Core when Watch is selected | watchOS target, WidgetKit accessory families |
| Foundation Models, Visual Intelligence, Writing Tools | Later (new module `intelligence` when a product needs it) | FoundationModels with availability check and fallback |
| Collaboration, version history, Focus filters, themes | Later | CloudKit sharing, etc. |

### Customer: the person paying or needing help

| Surface | Tier | Implementation |
| --- | --- | --- |
| Paywall with honest terms (price, period, trial end, Terms, Privacy) | Module `commerce` | RevenueCat `PaywallView`; iPad uses `PaywallView`, not `presentPaywallIfNeeded` |
| Entitlement gate (gate features, never the user's own data) | Module `commerce` | `CustomerInfo.entitlements[id].isActive` + the existing offline grace policy |
| Restore | Module `commerce` | `Purchases.shared.restorePurchases()` |
| Manage, cancel, refund, retention offer | Module `commerce` | iOS: RevenueCat `CustomerCenterView`. Mac and Watch: StoreKit `manageSubscriptionsSheet` / refund request, or "manage on iPhone" |
| "Before you delete" Home Screen quick action: feedback for everyone, a discount for subscribers | Switch, off by default | Dynamic `UIApplicationShortcutItem` + scene-delegate bridge → feedback sheet or promotional-offer paywall; Mac: Dock menu |
| Cancel-time survey + retention discount, in the app | Switch, off by default | Customer Center survey with a promotional offer per reason (iOS, Catalyst) |
| Retention message or discount on Apple's own cancel sheet in Settings | Switch, off by default | Apple Retention Messaging API (pre-release; needs Apple approval; endpoint answers within 700 ms; RevenueCat can run it; not on Watch) |
| Billing failure and price-increase messages ("your data is safe") | Core when `commerce` is selected | StoreKit `Message` API + billing grace period |
| Win-back offer after lapse, offer codes | Switch, off by default | App Store Connect + RevenueCat |
| Support: help page, contact, feedback with consent preview | Core | Support URL + native mail compose; shows what will be sent |
| Privacy manifest, SDK inventory, privacy answers | Core | `PrivacyInfo.xcprivacy` per target; check the built bundle |
| Account + Sign in with Apple, in-app account deletion | Module `accounts` | AuthenticationServices; §5.1.1(v) deletion and token revocation |
| Review prompt after a success moment | Core (small) | `RequestReviewAction`, never on a button tap |

### Creator: the person who made and runs the app

| Surface | Where it lives | Data source |
| --- | --- | --- |
| Revenue, MRR, trials, churn, refunds | Console | RevenueCat API v2 `metrics/overview`, `charts/*` |
| Customer lookup for support | Console | RevenueCat `customers`, `subscriptions`, `transactions` (read scopes) |
| Builds, TestFlight, review status, phased release | Console | App Store Connect API |
| Ratings, reviews, reply drafts | Console (reply needs a human click) | App Store Connect `customerReviews` |
| Crashes, hangs, launch time, energy | Console + app | App Store Connect `perfPowerMetrics`; MetricKit in the app |
| Store analytics (impressions, downloads, conversion) | Console | App Store Connect Analytics Reports (24–48 h lag, privacy thresholds) |
| Sales and finance | Console (optional) | Sales/Finance reports; **needs a Team key that covers all apps** |
| Product analytics | Later | None by default; then TelemetryDeck or Aptabase with a fixed event schema |
| Remote config | App | Bundled JSON; RevenueCat offering metadata for paywall copy |
| Release pipeline | Factory `make` targets | `xcodebuild archive`, App Store Connect upload; submission stays a human action |

## RevenueCat platform gaps

| Platform | Purchase SDK | Paywalls UI | Customer Center | Fallback to generate |
| --- | --- | --- | --- | --- |
| iPhone, iPad | Yes | Yes | Yes | — |
| Mac (native AppKit/SwiftUI) | Yes | Yes (5.39.0+, editor-built paywalls only) | **No** | StoreKit `manageSubscriptionsSheet`, link to Apple refund request, restore button |
| Mac (Catalyst) | Yes | Yes | Yes (15+), but refund and plan change are iOS-only | Same as iOS, minus refund |
| Watch | Yes | **No** | **No** | Show entitlement status; "Manage on iPhone" |
| Vision | Yes | **No** | **No** | Not in the first build |

Source: [`04_customer_creator_stack.md`](04_customer_creator_stack.md) §1, checked against the fact-check lane.

The full list of small opt-in features (support, feedback, cancel survey, retention, win-back, billing messages, What's New, review prompt), with the 16 proposed `project.json` switches, is in [`08_little_things.md`](08_little_things.md).

## Proposed generated app shape

This is a proposal for the next build run. It follows `AGENTS.md`: separate platform behavior, shared meaning and state.

```text
MyApp/
  Packages/AppCore/            shared Swift package
    Model/                     SwiftData models + export format
    Features/                  the one core job: state + actions, no views
    Commerce/                  RevenueCat wrapper, entitlement policy, fallbacks   (commerce)
    Support/                   help, feedback composer, review prompt
    Intents/                   AppEntity + AppIntent for capture and lookup         (app-intents)
  iOS/                         iPhone + iPad + Duo target (one target)
  macOS/                       native Mac target: menus, windows, MenuBarExtra
  watchOS/                     Watch app target
  Widgets/                     one widget extension per platform host               (widgets, active-activity)
  Config/                      xcconfig per target, entitlements, PrivacyInfo.xcprivacy per bundle
  AppTests/                    Swift Testing + StoreKit test session scenarios
```

Rules:
- Only the RevenueCat **public** SDK key goes in the app, through an xcconfig value. The creator's secret keys never reach a generated app.
- Only the selected modules are generated. This keeps factory invariant 6.
- Deployment targets: iOS 18, macOS 15, watchOS 11. Build with Xcode 27.1, Swift 6 language mode.
- Generate the Xcode project. Do not hand-edit `project.pbxproj` for multi-target apps. The choice between XcodeGen, Tuist, and the Xcode 27 template is an open decision (see below).

## Creator console (proposed)

Grow `dogfood/app-workshop` (a native Mac app) from "process guide" into "studio console":

1. **Portfolio**: one row per client app. Shows phase, last build, review state, MRR, rating, and crash-free rate, each with a "data as of" time and a source label.
2. **App detail**: revenue (RevenueCat), releases and TestFlight (App Store Connect), reviews, performance, and the gates from the app's `docs/quality/gates.json`.
3. **Support desk**: look up a customer by App User ID. Show entitlements and transactions. Grant or refund actions are hidden behind a confirmation and written to an audit log.
4. **Credentials**: per-client RevenueCat v2 read key and App Store Connect key, stored in the macOS Keychain. The console never writes them to disk, logs, or exports.
5. **Process**: the existing 13-phase guide, now per client app.

Start read-only. Add each write action as its own reviewed step.

## Website: the function is the form

Ben's rule (2026-10-19): what the app does is how the site looks and feels to use. The site is not a marketing template with the app's name in it. It is the app's core job, shown working. This follows `principles-visual`: honest materials (a surface looks and behaves like what it is), one subject first, and motion only where something matters.

Rules for the generated `site/`:

1. **The hero is the product working.** The first screen runs the app's one useful result from `docs/product/BRIEF.md`, live and in the browser: a timer that counts, a task you can check off, a note you can type into. No screenshot carousel and no device mockup in its place.
2. **Page order follows the user's journey in the app** (capture → organize → done → return), not the template order (hero, features, testimonials, pricing).
3. **One design source.** The app's identity tokens (color, type scale, spacing, corner radius, motion curves) generate both the SwiftUI values and the CSS custom properties. A change in the app changes the site.
4. **Same materials, same motion.** Glass only where the app uses glass, over content worth seeing through. The site animates only what the app animates, with the app's curves. `prefers-reduced-motion` gets the app's Reduce Motion alternative.
5. **The call to action continues the same job.** "Continue this in the app": a Universal Link can carry the demo's state (for example, the task the visitor just typed) into the installed app. It stays local, with no account and no tracking.
6. **Proof is real output.** Show the actual result the app produces, real reviews, and real numbers with their source and date. No stock imagery, no invented counts.
7. **Function first in the checks.** The hero demo must work with the keyboard and a screen reader and meet the Core Web Vitals "good" thresholds from `benpham3206/distribution` (LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1). A beautiful site that fails these fails.

The website lane's findings are in [`07_website.md`](07_website.md), filtered through these rules; its header lists what was kept and what was rejected. Defaults kept: static HTML/CSS, no framework, Cloudflare Pages, official App Store badge, Smart App Banner, Universal Links, Buttondown waitlist before launch, and the CI checks (Lighthouse budget, axe, HTML validation, link check, AASA check, no tracking without consent).

## Dogfood: App Workshop's own site and app set the bar

Ben's rule (2026-10-19): App Workshop uses itself. Its website and its Mac app must look and feel like the best product in the category. They are the factory's proof: a client judges the generated apps by these two things first.

**What App Workshop does** is turn a plain-words idea into a shipped app: market → gap → brief → generated app → evidence → release → operate. By the function-is-form rule, both surfaces show that transformation happening.

**Website (`dogfood/app-workshop/site/`, generated by the factory's own `site` template):**
- **Hero:** a visitor types an idea in one line. The page runs the real pipeline on it and shows the result building in place: the brief, the chosen preset, the three-sided map (user, customer, creator), the generated file tree, and the release gates, each one arriving in order. It uses the real generator output, not an illustration. (How: the generator is deterministic Python, so the demo either runs it in the browser through Pyodide or replays recorded outputs for a fixed set of ideas. That is an open decision, below.)
- **Second screen:** the gap scan from `09_gaps.md` as a live, sortable scorecard. This is the market → gap step shown working.
- **Third screen:** a generated app running: Simulator recordings of the iPhone, iPhone Duo, iPad, Mac, and Watch targets from one selection, with the widgets and the paywall.
- **Proof:** the evidence ledger, with real `make verify` results, build times, and the gates each app passed, all dated. No testimonials until there are real clients.
- **Call to action:** "Start an app" opens the intake interview, which is the same one the Mac app uses.

**Mac app (the studio console, grown from `dogfood/app-workshop`):** the same pipeline as a native tool. Portfolio, per-app detail with RevenueCat and App Store Connect data, the support desk, gates, and the 13-phase guide (14 with `market`). The bar: native Mac menus, windows, keyboard, Liquid Glass only on system chrome, and measured launch and response times. It should feel like Things or Fantastical, not like a dashboard template.

**One identity for both.** App Workshop's identity tokens generate the site's CSS and the app's SwiftUI values. It is the first real use of the shared `design/tokens/` source (ledger row 28).

**Spec:** Can a visitor go from typing an idea to seeing their own generated brief and file tree in **under 10 seconds**, on a mid-range phone, with Core Web Vitals "good"?
**Kill criteria:** if the in-browser pipeline cannot meet 10 seconds or LCP ≤ 2.5 s on a mid-range phone, replay recorded outputs instead of running live. If neither feels premium in a cold review by 3 people outside the project, cut the site to one screen until it does.

## Apple's documentation as the source of the architecture

Ben's idea (2026-10-19): Apple's own documentation, distilled, is the boilerplate's set of principles. The factory already points this way: most of its rules carry an "Apple source checked <date>" link. The proposal makes it systematic and checkable.

**Four layers, each traceable to the one above:**

| Layer | What it is | Where it lives |
| --- | --- | --- |
| 1. Axioms | Ben's universal principles (form, material, energy, observer, composition, time) | `principles` skills |
| 2. Apple canon | **HIG** = design intent; **App Review Guidelines** = what is enforced; **API docs** = how it works | developer.apple.com |
| 3. Factory rules | One distilled rule per Apple requirement, with source URL, check date, and the Apple change-log date | `core/`, `ux/`, `platforms/`, `modules/` |
| 4. Proof | Generated code and the test or gate that proves each rule | `templates/`, `tests/`, `docs/quality/gates.json` |

**The finding that makes it buildable (FACT, checked 2026-10-19):** Apple serves its docs as structured JSON at `https://developer.apple.com/tutorials/data/<path>.json`. Both an HIG page (`design/human-interface-guidelines/onboarding.json`) and an API page (`documentation/storekit/requestreviewaction.json`) return HTTP 200, with typed sections. HIG pages include *Best practices*, *Platform considerations*, and a *Change log*. The format is undocumented, so treat it as able to change.

**What that enables:** a small stdlib tool (proposed `tooling/apple_canon.py`) that:
1. Reads the list of Apple pages the factory cites. Today that is **335 distinct developer.apple.com links** across `core/`, `ux/`, `platforms/`, `modules/`, `design/`, `config/`, `docs/`, and `templates/` (counted 2026-10-19).
2. Fetches each page's JSON and records a content hash, the headings, and the change-log entries.
3. Compares them with the last snapshot and reports **which factory files cite a page that changed**.

That automates the rule `AGENTS.md` already gives by hand ("check current primary Apple documentation for any claim that may have changed"). The factory then stays current with each OS release without anyone re-reading the HIG.

**Limits:**
- **Distill, do not copy.** Apple's pages carry legal notices. Store our own one-line rule, the link, and a hash, never Apple's text.
- **The HIG is guidance, and the App Review Guidelines are enforcement.** A rule says which one it comes from, so a HIG preference never blocks a release the way a guideline violation does.
- **Apple is not the whole canon.** Taste, the market, and the customer side (RevenueCat, support, retention) come from layers 1 and the research here. Apple tells you how to build it right; it does not tell you what is worth building.

## Bitrig: copy and avoid

Copy: guided plain-words intake → editable brief → smallest native slice running in Simulator within the first session → visible release states → automated App Store Connect metadata and screenshots.

Avoid: calling "submitted" "approved"; trusting a pretty preview over a compiled build; turning on every module; mixing client credentials into prompts; treating a paywall as customer support.

Full list with sources: [`03_bitrig_and_peers.md`](03_bitrig_and_peers.md) §4–5.

## Think bigger: the studio, not the template

Ben runs this for people who want an app and do not know where to start. So the product is a **studio operating system**: intake → brief → preset → generated app → first slice → evidence → release → operate. The boilerplate is one stage. The parts that compound across clients are:

- **Presets** (`config/presets/`, empty today): tasks, notes, planner, focus timer, journal, habits. Each preset selects platforms, modules, an identity, and starter copy. These come from the indie tier in `01_market.md`.
- **Intake interview**: a headless script that writes `project.json` and the brief. It runs for Ben first and for a client later.
- **Handoff kit**: the client owns the Apple account, the RevenueCat project, the repo, and every key. Ben's access is a scoped key with a revoke date. This boundary is what makes self-serve possible later.
- **Portfolio console**: every client app in one place. Lessons from one app become gates in the factory.

## Spec for the next run

**Atomic question:** Can the factory take one client from a plain-words idea to an internal TestFlight build with a working RevenueCat paywall on iPhone, iPad, and Mac in **5 operator-days or fewer**?

**Kill criteria (write first):**
- The first client app takes more than **10 operator-days** to reach TestFlight. Then cut scope to iPhone + commerce only.
- Generated multi-target projects fail `make verify-xcode` on a clean checkout more than **1 time in 5**. Then stop adding targets and fix generation.
- Bitrig, or Xcode's own agents, reach the same TestFlight state for the same brief in under **1 day** with equal review readiness. Then narrow App Workshop to evidence gates and the console only.

**Build criteria:** iPhone + iPad + Mac + Watch targets build and launch from `make run`. StoreKit test session scenarios pass for purchase, restore, expiry, refund, and offline grace. The console shows live RevenueCat and App Store Connect data for one sandbox app. No secret appears in any generated file (`make check` secret scan).

## Open decisions for Ben

1. **Project generation tool** for multi-target apps: XcodeGen (one YAML, mature, a build-time dependency), Tuist (more power, more weight), or an Xcode 27 template plus a script. Recommendation: XcodeGen, pinned, used only by the factory, with the generated `.xcodeproj` committed so the client never needs it.
2. **Creator console scope gate**: confirm that it grows from `dogfood/app-workshop` and counts as part of the App Workshop product, not a fourth product. This needs a Decision Queue row.
3. **Sales/Finance**: these reports need an App Store Connect Team key that covers all of a client's apps. Accept that scope per client, or skip finance and use RevenueCat revenue only.
4. **Mac target: native or Catalyst.** Native gives real Mac menus, windows, and settings (the `AGENTS.md` default), but not Customer Center, so the Mac needs about one screen of StoreKit fallback. Catalyst gets Customer Center (without refund) at the cost of a less native Mac. Recommendation: native, with the fallback.
5. **Dogfood site demo:** run the real generator in the browser (Pyodide: honest and live, but heavier, and it must still pass the 2.5 s LCP budget) or replay recorded outputs for a fixed set of ideas (fast and simple, less alive). Recommendation: replay first, then live once it meets the budget.
6. **Dogfood site home:** its own domain on Cloudflare Pages. GitHub's terms exclude commercial services, and App Workshop is offered to clients, so `benpham3206.github.io` is not a fit (`07_website.md` §3).
7. **First client**: the spec above needs one real brief. Recommendation: use the trade-utility gap (`09_gaps.md`) as the first dogfood app. It is small, sold as a one-time purchase, offline, and in Ben's domain. First step: mine 500 reviews each for the three stale incumbents before choosing one tool.

## Evidence boundary

Nothing was built, run on a device, or submitted. Market figures are third-party estimates with mixed scopes. Vendor features and prices change; recheck before building. Fact-check: [`06_factcheck.md`](06_factcheck.md) confirmed 13 of 17 load-bearing claims. It corrected the RevenueCat SDK version (5.96.0), the Customer Center Mac scope (Catalyst yes, native no), Things sync (Things Cloud only), Todoist pricing (no conflict), and incoming share capture (needs a share extension). The corrections are applied in files 01–05 (marked [FC]) and in this report. The website and small-features lanes are not yet fact-checked. App icon conventions for Liquid Glass come straight from Apple's HIG and Icon Composer pages (read 2026-10-19): [`12_app_icon_liquid_glass.md`](12_app_icon_liquid_glass.md), LEDGER rows 37–39.
