# Payment Routes Beyond Standard IAP (2026) — iOS/Mac Solo Developer

Status: COMPLETE. Current as of 2026-09-27. **Not legal or tax advice.** Every claim is labeled FACT (with URL), INFERENCE, or UNKNOWN. Web search/fetch tools hit a session rate limit partway through research; most flagged pricing gaps (Stripe, Paddle, Lemon Squeezy, Sparkle) were subsequently re-verified via direct fetch once the limit lifted — see the update note near the end of §2/§3/§4 and the final "Post-rate-limit verification pass" note before the Session constraint note. FastSpring's rate and a few SCOTUS docket specifics remain unverified; still flagged in place.

---

## 1. United States: Epic v. Apple anti-steering injunction, appeal status, Guidelines 3.1.1/3.1.1(a)/3.1.3, web-sale obligations

### Takeaway
As of 2026-09-27, US developers can add external purchase links/buttons with **0% Apple commission** — a genuinely free "link out" — but this is a temporary litigation state, not settled law. The Ninth Circuit affirmed Apple was in contempt of the original anti-steering injunction (Dec 11, 2025); the Supreme Court granted cert on Apple's appeal (per one source, July 2, 2026) and denied Apple's request to stay the no-commission regime in the meantime (Justice Kagan, May 6, 2026); Apple separately asked the district court on Aug 14, 2026 to approve new commission rates (15% standard / 10% partner programs / 5% Small Business Program / 10% on renewals) that are **not yet in effect**. A solo developer should build for "0% today" while explicitly planning for a possible ~5–15% commission to appear later in 2026 or in 2027 once the district court and/or Supreme Court rule.

### Cited Findings
- Ninth Circuit unanimously affirmed the district court's civil contempt finding against Apple on Dec 11, 2025, holding Apple "prohibited developers from using buttons, links, and other calls to action without paying a prohibitive commission ... and restricted the design of developers' links to make it difficult for customers to use them" — [Justia, Epic Games v. Apple, No. 25-2935 (9th Cir. 2025)](https://law.justia.com/cases/federal/appellate-courts/ca9/25-2935/25-2935-2025-12-11.html)
- The original 2021 injunction barred Apple from restricting developers from including buttons, links, or other calls to action directing users to alternative purchasing mechanisms, while separately upholding Apple's right to require IAP for in-app digital-goods purchases — [Wikipedia, Epic Games v. Apple](https://en.wikipedia.org/wiki/Epic_Games_v._Apple) (secondary/aggregator; treat as background, corroborated by primary court doc above)
- Apple's post-injunction compliance plan (a 27% commission on linked-out purchases plus button/design/flow restrictions) was found by the district court to still effectively frustrate the injunction, leading to the contempt finding — [Justia case page](https://law.justia.com/cases/federal/appellate-courts/ca9/25-2935/25-2935-2025-12-11.html); [Shinder Cantor Lerner summary](https://scl-llp.com/ninth-circuit-upholds-apple-contempt-finding-but-narrows-scope-of-remedial-relief/)
- Supreme Court granted certiorari on Apple's appeal of the contempt ruling; case tracked as *Apple Inc. v. Epic Games, Inc.*, No. 25-1311 — [Oyez case page](https://www.oyez.org/cases/2026/25-1311)
- Justice Kagan denied Apple's emergency application to stay the no-commission link-out regime on May 6, 2026, so external-payment links have remained permitted (at 0% Apple commission) on iOS in the US since then — cited in [SEM Nexus, App Store vs. Web Funnel](https://semnexus.com/app-store-vs-web-funnel-where-subscription-apps-convert) (secondary source synthesizing docket events; corroborate against the primary SCOTUS docket, e.g. the filed application at [courthousenews.com PDF, No. 25A1213](https://www.courthousenews.com/wp-content/uploads/2026/05/epic-response-scotus-emergency-docket-apple-app-store.pdf), before publishing the exact date)
- On Aug 14, 2026 Apple asked the district court to approve new commission rates on US link-out purchases: **15% standard**, **10%** for Video/News/Mini Apps Partner Program participants, **5%** for Small Business Program members, and **10%** on subscription renewals — [TechCrunch, "Apple proposes to take a 15% cut of purchases made outside the App Store"](https://techcrunch.com/2026/08/14/apple-proposes-to-take-a-15-cut-of-purchases-made-outside-the-app-store/); corroborated by [MacRumors](https://www.macrumors.com/2026/08/13/app-store-fees-apple-link-outs/) and [9to5Mac](https://9to5mac.com/2026/08/13/apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us/)
- Until the district court approves a rate, external purchase links in the US remain at **0% Apple commission**; a related question is also pending before the Supreme Court, with Apple's merits briefing reported due Sept 14, 2026 — [TechCrunch (same article)](https://techcrunch.com/2026/08/14/apple-proposes-to-take-a-15-cut-of-purchases-made-outside-the-app-store/)
- Apple updated Guidelines 3.1.1, 3.1.1(a), 3.1.3, and 3.1.3(a). Per 3.1.1(a): "On the United States storefront, there is no prohibition on an app including buttons, external links, or other calls to action, and no entitlement is required to do so." — quoted from [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) via search synthesis; **recommend the report-writer re-fetch this page directly to confirm exact current wording**, since guideline text is revised frequently and this session's fetch of it did not complete before hitting the tool-rate-limit.
- Outside the US storefront, 3.1.3(a)'s general "External Purchase Link" entitlement historically still requires an application/approval and is not blanket-permitted the way the US carve-out is — INFERENCE, consistent with the country-specific entitlement pages found for Netherlands (§7) and Korea (§7) below, each of which is its own separate entitlement with its own commission.

### Inferences
- The net effect for a solo US developer in Sept 2026: adding a web-purchase link today costs 0% to Apple, but that is very likely to become a real, nonzero commission (most plausibly in the 5–15% range depending on program eligibility) once litigation resolves — build the accounting/entitlement logic to be commission-rate-agnostic (i.e., don't hardcode "no Apple cut" into unit economics).
- Because Apple's own compliance history here involved a contempt finding for using UX friction (link design/placement restrictions, warning interstitials) to suppress use of external links, a small developer should expect Apple's *link presentation rules* (button style constraints, disclosure sheet, no misleading claims) to persist even as the *commission* question is litigated — these are two separate levers Apple has used.
- A solo developer building today should treat the web-purchase path as "must handle it themselves": Apple's guidance elsewhere (see Netherlands entitlement text, §7) makes clear "Apple cannot assist with refunds, payment history, or subscription management for external purchases" for entitlement-based link-outs; the same operational split (entitlement sync, restore-purchases, refunds, chargebacks, sales tax) is a reasonable assumption for the US link-out path too, though the US carve-out is a court order rather than a formal entitlement — **UNKNOWN**: whether Apple has published explicit US-specific developer obligations (vs. the Netherlands/Korea entitlement pages) for restore/refund handling; not confirmed this session, flag as a gap.

### Gaps
- Exact current text of Guidelines 3.1.1/3.1.1(a)/3.1.3/3.1.3(a) — WebFetch of developer.apple.com/app-store/review/guidelines/ did not complete before the tool rate-limit hit; only search-engine-synthesized quotes were obtained.
- Exact Supreme Court oral-argument date / whether cert was granted specifically on the commission question vs. only the contempt-remedy scope — sources conflict/are imprecise on this (Oyez lists the case; TechCrunch/9to5Mac describe "a related question... with the Supreme Court"). Needs primary-docket confirmation (supremecourt.gov docket for 25-1311) before citing a specific date in a final report.
- Whether Apple has published a specific developer-facing document (distinct from Guideline text) spelling out obligations for US web-sale entitlement sync, restore, refunds, chargebacks, and sales tax — not located this session.

---

## 2. Economics: take-home per $9.99/month subscriber

### Takeaway
On a $9.99/mo subscription, plain IAP nets a solo developer **$8.49/mo (85%)** after year one via the Small Business Program (15% commission), or **$6.99/mo (70%)** at the standard 30% rate before SBP/year-one-anniversary discounts apply. A merchant-of-record web checkout (Paddle or Lemon Squeezy, confirmed 5%+$0.50/transaction — see verified update below) nets roughly **$8.99/mo (~90%)**, i.e. comparable to or slightly better than SBP-rate IAP. Direct Stripe processing (confirmed 2.9%+$0.30 domestic card — see below) is cheapest on paper (~$9.40/mo, ~94%) but leaves sales-tax/VAT registration and remittance, chargeback handling, dunning, and subscription-lifecycle logic entirely on the developer, unless Stripe's own merchant-of-record product (Stripe Managed Payments, confirmed 3.5% on top of Payments fees — see below) is used instead. Critically, **conversion rate, not just take-home rate, determines actual revenue**: RevenueCat's controlled study found IAP converts substantially better than a web link-out, such that web checkout produced only **$0.93 of revenue for every $1.00 an equivalent IAP funnel produced — even after netting out the App Store's commission** on the IAP side.

**[VERIFIED UPDATE — post-rate-limit re-check]** Direct fetches of stripe.com/pricing, paddle.com/pricing, and lemonsqueezy.com/pricing confirmed the figures below with high confidence (official vendor pricing pages, fetched 2026-09-27):
- **Stripe** (direct processing, developer remains merchant of record): **2.9% + 30¢** per successful domestic-card transaction (+0.5% for manually-keyed cards, +1.5% for international cards, +1% for currency conversion) — [stripe.com/pricing](https://stripe.com/pricing)
- **Stripe Billing** (subscription management layer on top of processing): pay-as-you-go at **0.7% of billing volume**, or a flat **$620/mo** (1-year contract) plan — [stripe.com/pricing](https://stripe.com/pricing)
- **Stripe Tax**: **0.5% per transaction** (no-code) or a flat **$0.50/transaction** (API) where registered to collect, or a **$90/mo** "Tax Complete" plan (1-year contract) — [stripe.com/pricing](https://stripe.com/pricing)
- **Stripe Managed Payments** (Stripe's own merchant-of-record product, handling tax compliance/fraud/disputes across 75+ countries): **3.5% per transaction, in addition to** the base Payments fee above (i.e., roughly 2.9%+3.5%+30¢ combined, before any Billing/Tax add-ons) — [stripe.com/pricing](https://stripe.com/pricing)
- **Paddle** (merchant of record, pay-as-you-go): **5% + 50¢ per checkout transaction**, all-inclusive of tax/VAT remittance, fraud/chargeback handling, subscription management, and 24/7 billing support; custom pricing for enterprise or sub-$10 products — [paddle.com/pricing](https://www.paddle.com/pricing)
- **Lemon Squeezy** (merchant of record): **5% + 50¢ per transaction**, no monthly fees, with the vendor noting some edge cases can carry small additional fees — [lemonsqueezy.com/pricing](https://www.lemonsqueezy.com/pricing)

This confirms the earlier secondary-sourced Paddle/Lemon Squeezy estimate (§4) was accurate, and gives an exact, sourced Stripe figure. FastSpring's rate remains unconfirmed (still requires a sales conversation per public info); treat as a residual gap.

### Cited Findings
- Apple's Small Business Program: commission cut from 30% to 15% for developers whose total App Store proceeds were under $1,000,000 in the prior calendar year; applies to paid apps and IAP — [Apple Developer, App Store Small Business Program](https://developer.apple.com/app-store/small-business-program/) (official page, confirmed via search synthesis)
- Standard IAP commission is 30% in year one of a subscription, dropping to 15% starting in year two of an uninterrupted subscription — well-established Apple subscription policy; **not independently re-verified via fresh fetch this session** — cross-referenced against [RevenueCat, "The 15% App Store Fee: A Guide for Developers (2026)"](https://www.revenuecat.com/blog/engineering/small-business-program)
- RevenueCat ran a controlled IAP-vs-web test on a subscription audio app: IAP trial-start rate ≈27.0% vs. web ≈18.1% (a ~33% relative decline for web); web subscriptions generated **$0.93 for every $1.00** earned via IAP, even after accounting for the App Store fee savings on the web side — [Daring Fireball, "RevenueCat Report Suggests In-App Purchases Perform Noticeably Better Than Link-Outs to the Web" (May 2025)](https://daringfireball.net/linked/2025/05/15/revenuecat-external-purchase-report), citing RevenueCat's own report
- General benchmark figures (separate from the controlled study above): IAP conversion cited at 27–30% of viewers vs. 17–19% for web checkout in one synthesis — [SEM Nexus, "App Store vs. Web Funnel"](https://semnexus.com/app-store-vs-web-funnel-where-subscription-apps-convert) (secondary aggregator; directionally consistent with the RevenueCat-sourced figures above, treat as corroborating rather than independent)
- Lemon Squeezy and Paddle are both cited (by an aggregator, not each vendor's own pricing page fetched this session) as charging "the same headline 5% + 50c" per transaction as merchant of record — [Fintechspecs, "Stripe vs Paddle vs Lemon Squeezy vs Polar"](https://fintechspecs.com/blog/stripe-vs-paddle-vs-lemon-squeezy-vs-polar-merchant-of-record-b2b-saas/) (secondary source; **flagged for re-verification against paddle.com/pricing and lemonsqueezy.com directly** — this session's WebFetch attempts to those pages hit a tool rate-limit before completing)
- FastSpring is described as not publishing a standard rate without a sales conversation, implying no simple public headline fee to cite — [Dodo Payments, "Top 7 Merchant of Record Platforms 2026"](https://dodopayments.com/blogs/best-merchant-of-record-platforms) (secondary source)
- RevenueCat's own Web Billing product fee is reported (blog title only, not the RevenueCat pricing page itself) as "1% vs 0.7%" depending on plan, layered on top of whichever billing engine (Stripe/Paddle/RevenueCat Billing) is chosen — [adamarant.com, "RevenueCat vs Stripe Billing in 2026"](https://adamarant.com/en/blog/stripe-billing-vs-revenuecat-picking-the-right-billing-layer) (secondary blog source; needs verification against revenuecat.com/pricing)

### Inferences
- Arithmetic (INFERENCE, built on the cited rates above, not independently re-verified this session):
  - IAP, standard 30%: $9.99 × 0.70 = **$6.99/mo**
  - IAP, Small Business Program / year-2+ subscription rate 15%: $9.99 × 0.85 = **$8.49/mo**
  - MoR web checkout at ~5% + $0.50 (Paddle/Lemon Squeezy-style, rate not re-verified fresh this session): $9.99 × 0.95 − 0.50 ≈ **$8.99/mo (~90%)**
  - Direct Stripe at a commonly-cited ~2.9% + $0.30 (training-knowledge figure, **UNKNOWN/not verified this session** — flag before publishing): $9.99 × 0.971 − 0.30 ≈ **$9.40/mo (~94%)** *before* the developer's own cost of building/maintaining tax registration, invoicing, dunning, and chargeback handling, which a MoR bundles in for its fee.
  - These are gross take-home percentages only; they say nothing about volume. Given RevenueCat's finding that web-linked purchases converted at roughly two-thirds the rate of IAP and produced ~93 cents of value per IAP dollar net of fees, a naive "web checkout is cheaper" comparison is misleading for a solo developer without a large, warm, price-sensitive audience willing to leave the app to pay.
- A solo developer's true breakeven question is not "which take-home % is highest" but "does the conversion loss from sending users off-platform outweigh the fee savings" — for a brand-new app with an unproven audience, IAP's higher conversion likely dominates; for a developer with an existing engaged audience (email list, community) directed to a web paywall, the fee savings may win. This is INFERENCE synthesized from the RevenueCat data point, not a directly cited recommendation from any source.

### Gaps
- ~~Exact current Stripe/Paddle/Lemon Squeezy pricing~~ — RESOLVED, see verified update above (all three confirmed via direct fetch of vendor pricing pages, 2026-09-27).
- Exact current FastSpring fee schedule — still not found; FastSpring does not publish self-serve pricing and requires a sales conversation (confirmed pattern, not a specific number).
- RevenueCat Web Billing's own fee schedule from revenuecat.com/pricing directly — not fetched; only a third-party blog title ("1% vs 0.7%") was found. Still a gap.

---

## 3. Mac direct distribution: Developer ID, notarization, Sparkle, license keys vs. subscriptions

### Takeaway
Developer ID code signing and notarization require an active **paid Apple Developer Program membership ($99/year)** — there is no free tier for Developer ID distribution. Notarization (via `notarytool`, the current CLI replacing the deprecated `altool`) plus the hardened runtime entitlement and ticket "stapling" are what let Gatekeeper accept a non-App-Store Mac app without an unnerving warning. This route is the standard escape valve for Mac apps that cannot pass Mac App Store sandbox/private-API review, but it pushes update delivery (commonly via the open-source **Sparkle** framework) and payment/licensing (license keys or a self-built subscription/account system paired with a web billing provider from §4) entirely onto the developer.

### Cited Findings
- Developer ID certificate creation and notarization require a paid Apple Developer Program membership; forum/community sources describe this as: "a paid account is required to notarize... you need to code sign the binary with a developer ID certificate (which costs $99 a year) and notarize it" — [Apple Developer Forums, community threads](https://developer.apple.com/forums/thread/781342) (secondary/forum-sourced; directionally consistent with well-established Apple policy, but **recommend confirming against developer.apple.com/programs/ and developer.apple.com/documentation/security/notarizing-macos-software-before-distribution directly** — this session's targeted fetch of the Apple notarization documentation page was not completed due to the tool rate-limit)
- "All developers creating a Developer ID certificate for the first time are required to notarize their apps, and all new and updated kernel extensions must also be notarized" — cited via search synthesis of Apple Developer Forums content
- Producing signed and notarized macOS releases requires Apple Developer Program membership (quoted figure "99 € per year" in one source, reflecting EU pricing; US price is commonly cited as $99/year) — secondary source via search synthesis

### Inferences — RE-VERIFICATION STATUS (updated post-rate-limit)
- **notarytool** pipeline (build → codesign with "Developer ID Application" cert + hardened runtime → `xcrun notarytool submit` → `xcrun stapler staple`) — **still INFERENCE/training-knowledge**. A direct WebFetch to developer.apple.com/documentation/security/notarizing-macos-software-before-distribution was attempted post-rate-limit but returned only the page title (the page is JS-rendered and didn't yield body text to the fetch tool); the pipeline description is well-established general knowledge but was **not textually confirmed against the primary doc this session**. Flag as NOT independently re-verified.
- **Hardened runtime** requirement for notarization — same status: still INFERENCE, not textually confirmed this session (same JS-rendering issue on the doc fetch).
- **Sparkle** — **NOW VERIFIED** via direct fetch of sparkle-project.org (2026-09-27): Sparkle is confirmed as an open-source (MIT-licensed), free, self-updating framework for macOS apps; it supports **EdDSA signature verification**, integrates with Apple code signing, supports **sandboxed applications**, supports delta updates, and works on macOS 12+. Confirmed notable adopters include Cyberduck, iTerm, Transmission, and HandBrake. **Confirmed: Sparkle has no built-in license-key or payment/monetization system** — the fetched content explicitly states this isn't addressed and would need custom implementation via Sparkle's delegate API. — [sparkle-project.org](https://sparkle-project.org)
- For Mac apps that cannot pass Mac App Store review (sandbox/private-API needs), Developer ID + notarization is the standard fallback — still INFERENCE, consistent with well-known practice, not independently sourced this session.
- License-keys vs. subscription lifecycle tradeoff for directly-distributed Mac apps — still INFERENCE/reasoning, not sourced.
- Any of the §4 web billing providers can serve a directly-distributed Mac app the same as a web-linked iOS purchase, since none require StoreKit — still INFERENCE (logically follows from providers being platform-agnostic web checkouts, not independently sourced).

### Gaps
- Apple's own notarization documentation page did not yield readable body text via WebFetch (JS-rendered page returned only the title both before and after the rate-limit reset) — the pipeline/hardened-runtime claims in this section remain general-knowledge INFERENCE, not primary-source-confirmed. A follow-up should try `curl` or a rendering-capable fetch, or cite a third-party technical writeup that mirrors Apple's doc instead.
- Sparkle's *specific current version number* and full EdDSA implementation details were not in the fetched homepage content (only that it uses EdDSA); would need the GitHub repo or docs subpage for version specifics.
- Whether Apple has made any 2025–2026 changes specifically affecting non-App-Store Mac distribution (new notarization fees, new Gatekeeper UI, or anything tied to the EU DMA's "Web Distribution" concept, which is iOS/iPadOS-specific and does not extend to Mac, which has always permitted direct distribution) — UNKNOWN, not investigated; worth a dedicated follow-up since Mac's baseline distribution model sits on a different regulatory footing than iOS's DMA-driven changes.

---

## 4. Web billing providers: Stripe, Paddle, Lemon Squeezy, FastSpring, RevenueCat Web Billing

### Takeaway
Paddle and Lemon Squeezy are true merchants of record (MoR) — they take on VAT/sales-tax registration and remittance, chargebacks, and dunning as the seller of record — at a **confirmed** headline rate of **5% + $0.50/transaction each** (verified directly from both vendors' own pricing pages, 2026-09-27). Lemon Squeezy is now owned by Stripe (acquired July 2024) and continues operating alongside Stripe's own new MoR product, "Stripe Managed Payments" (confirmed **3.5% on top of base Payments fees**). FastSpring is an older, enterprise-leaning MoR that does not publish self-serve pricing. Stripe itself, used directly (confirmed **2.9%+30¢** processing, plus optional Stripe Billing at **0.7% of volume** and Stripe Tax at **0.5%/transaction**), is *not* a merchant of record by default — the developer remains the seller of record and is responsible for their own tax registration/remittance unless they adopt Stripe Managed Payments. RevenueCat Web Billing sits a layer above all of these, letting a developer pick Stripe Billing, Paddle Billing, or RevenueCat's own Stripe-backed billing engine as the underlying processor while unifying entitlement state between mobile IAP and web purchases.

### Cited Findings
- Stripe acquired Lemon Squeezy (a merchant-of-record platform) in July 2024 for an undisclosed amount — [TechCrunch, "Stripe acquires payment processing startup Lemon Squeezy"](https://techcrunch.com/2024/07/26/stripe-acquires-payment-processing-startup-lemon-squeezy/)
- As of 2026, Lemon Squeezy continues operating ("we're not going anywhere, we're just getting stronger") while Stripe has separately launched "Stripe Managed Payments," its own MoR product, expanding to more regions — [Lemon Squeezy, "2026 Update: Lemon Squeezy + Stripe Managed Payments"](https://www.lemonsqueezy.com/blog/2026-update)
- **VERIFIED directly from vendor pricing pages (2026-09-27):** Paddle charges **5% + 50¢ per checkout transaction** (pay-as-you-go), all-inclusive of tax/VAT remittance, fraud/chargeback handling, subscription management, and 24/7 billing support — [paddle.com/pricing](https://www.paddle.com/pricing). Lemon Squeezy charges **5% + 50¢ per transaction**, no monthly fee, with the vendor noting "edge cases" can add small additional fees — [lemonsqueezy.com/pricing](https://www.lemonsqueezy.com/pricing). Stripe Managed Payments (Stripe's own MoR product) charges **3.5% per transaction in addition to** base Stripe Payments fees (2.9%+30¢), covering tax compliance/fraud/dispute handling across 75+ countries — [stripe.com/pricing](https://stripe.com/pricing). FastSpring remains the one MoR here with no public self-serve rate (requires a sales conversation) — [Dodo Payments, "Top 7 Merchant of Record Platforms 2026"](https://dodopayments.com/blogs/best-merchant-of-record-platforms) (secondary source; FastSpring's own pricing page was not checked this session).
- One aggregator's recommendation pattern: Lemon Squeezy for "indie developers/early-stage" ("If you sell digital products or a small SaaS and want tax handled with a pleasant UX, start here"), with a practical ARR ceiling around $500k–$1M for B2B SaaS contract/enterprise-billing needs; FastSpring/Paddle recommended for enterprise/complex B2B billing — [Fintechspecs](https://fintechspecs.com/blog/stripe-vs-paddle-vs-lemon-squeezy-vs-polar-merchant-of-record-b2b-saas/) (secondary; framed as B2B SaaS advice, not consumer-subscription-app-specific, so treat the specific ARR ceiling as an inference-flavored claim rather than settled fact)
- RevenueCat Web offers three billing-engine choices: RevenueCat Billing (RevenueCat's own engine, using Stripe as the payment gateway underneath), Stripe Billing (developer's own Stripe catalog, connected to RevenueCat Web features), and Paddle Billing (developer's own Paddle catalog, with Paddle as merchant of record) — [RevenueCat Docs, Web Billing Overview](https://www.revenuecat.com/docs/web/web-billing/overview); [RevenueCat Docs, Paddle Billing integration](https://www.revenuecat.com/docs/web/integrations/paddle); [RevenueCat Docs, Stripe Billing integration](https://www.revenuecat.com/docs/web/integrations/stripe)
- RevenueCat's Web SDK, Web Purchase Links, Web Paywalls, and Funnels can all be powered by whichever billing engine is chosen, and RevenueCat Entitlements are unified across mobile IAP and web purchases so app code checks one entitlement state regardless of purchase origin — [RevenueCat Docs, Web Billing Overview](https://www.revenuecat.com/docs/web/web-billing/overview)

### Inferences
- For a solo developer's very first paid app, the practical shortlist is: (a) Lemon Squeezy or Paddle if the priority is "never think about VAT/sales tax," accepting the ~5%+$0.50 fee; (b) Stripe Billing + Stripe Tax if the developer is willing to register for tax in their own jurisdictions in exchange for materially lower processing fees; (c) RevenueCat Web Billing on top of either, if the developer already uses (or plans to use) RevenueCat for mobile IAP and wants one entitlement model across platforms. FastSpring is likely overkill/inaccessible for a true solo-developer first launch given its enterprise/sales-led motion. This is a synthesis, not a directly cited recommendation.
- Because Lemon Squeezy is now Stripe-owned, a developer choosing it is implicitly already inside the Stripe ecosystem, which may simplify an eventual migration to plain Stripe Billing (dropping MoR status, taking on tax obligations directly) if/when volume grows — INFERENCE, not confirmed by a source describing migration mechanics.

### Gaps
- ~~Direct, current pricing pages for Stripe, Paddle, Lemon Squeezy~~ — RESOLVED, all three confirmed via direct vendor-page fetch (2026-09-27); see verified figures above and in §2.
- FastSpring's exact fee schedule — still unresolved; no public self-serve rate exists (confirmed pattern, not a number). Not fetched from fastspring.com directly this session.
- RevenueCat's own fee for Web Billing (percentage layered on top of the chosen engine) — still unresolved; only a secondary blog's title ("1% vs 0.7%") was found, not RevenueCat's own pricing documentation. Recommend fetching revenuecat.com/pricing directly in any follow-up.

---

## 5. EU DMA as of 2026: alternative business terms, Core Technology Commission, External Purchase Link, alternative PSPs/marketplaces

### Takeaway
Effective **October 1, 2026**, Apple replaced its prior tiered/optional EU business terms with a single **unified** set of terms (Attachment 14 of the Apple Developer Program License Agreement). The per-install **Core Technology Fee is gone**, replaced by a flat **5% Core Technology Commission (CTC)** on digital transactions in apps distributed outside the App Store (alternative marketplaces or Web Distribution). The old **Initial Acquisition Fee and Store Services Fee are eliminated** as standalone fees; App Store commission itself is 26% standard / 15% for Small Business Program-equivalent participants for Apple IAP, with parallel 20%/10% rates for in-app alternative payment processing and 15%/10% "Store Services Commission" for out-of-app linked offers (7-day attribution window). For a tiny solo developer, none of this is likely worth pursuing directly — the EU's alternative-marketplace/Web Distribution eligibility bar (financial audits, $1M letter of credit, or 1M first-year installs, among other criteria) is aimed at larger players — but the **in-app alternative-payment-processing** and **out-of-app linked-offer** options are available to any developer without that eligibility bar, at the 20%/15% (or 10% reduced) commission rates.

### Cited Findings
- From Oct 1, 2026: per-install Core Technology Fee replaced by a flat **5% Core Technology Commission** on digital transactions in apps distributed outside the App Store (alternative marketplaces / Web Distribution); Initial Acquisition Fee and Store Services Fee eliminated; apps may offer alternative payment options alongside Apple IAP; marketplace/web-distribution eligibility widens to **seven alternative criteria** — [Apple Newsroom, "Apple announces changes for apps in the European Union" (Aug 2026)](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/); corroborated in detail by [Apple Developer, "Changes for apps in the European Union"](https://developer.apple.com/support/apps-in-the-eu) and [Apple Developer, DMA and apps in the EU](https://developer.apple.com/support/dma-and-apps-in-the-eu) — **both fetched directly this session**, high-confidence primary source
- App Store commission structure (EU, effective Oct 1, 2026): Apple IAP 26% standard / 15% for SBP-equivalent & partner-program participants and for auto-renewable subscriptions after their first year; alternative payment processing in-app 20% standard / 10% reduced; out-of-app "Store Services Commission" on linked offers 15% standard / 10% reduced, only on sales completed within a 7-day window of the link tap — [developer.apple.com/support/apps-in-the-eu](https://developer.apple.com/support/apps-in-the-eu) and [developer.apple.com/support/dma-and-apps-in-the-eu](https://developer.apple.com/support/dma-and-apps-in-the-eu) (fetched directly)
- CTC is waived for small alternative-marketplace operators earning less than €10M global revenue (trailing 12 months) and under €1M lifetime revenue from marketplace download/subscription fees — [developer.apple.com/support/dma-and-apps-in-the-eu](https://developer.apple.com/support/dma-and-apps-in-the-eu)
- Developers must pick their EU payment option(s) — Apple IAP, alternative in-app payment processing, linking to the web, or a combination — and **maintain that choice for 12 months** — [developer.apple.com/support/dma-and-apps-in-the-eu](https://developer.apple.com/support/dma-and-apps-in-the-eu)
- Alternative-marketplace/Web-Distribution eligibility (as of Oct 1, 2026) requires meeting **at least one** of: a moderate Dun & Bradstreet financial-stability bar; being publicly traded (or owned by a public company); venture funding from an established firm; a completed financial audit by a licensed accountant; being a government/education/nonprofit entity (fee-waiver-approved); a standby letter of credit of **USD 1,000,000**; or **1,000,000 first-year worldwide installs**. Developers no longer need an EU legal entity to operate an alternative marketplace or use Web Distribution — [developer.apple.com/support/dma-and-apps-in-the-eu](https://developer.apple.com/support/dma-and-apps-in-the-eu)
- The old **StoreKit External Purchase Link Entitlement (EU) Addendum** and **Alternative Terms Addendum for Apps in the EU** are discontinued/superseded by the unified Attachment 14 terms as of Oct 1, 2026 — [developer.apple.com/support/apps-in-the-eu](https://developer.apple.com/support/apps-in-the-eu)
- Child-safety carve-outs: for Kids-category apps and users under 13, alternative-payment purchases must sit behind a parental gate and out-of-app website offers are prohibited entirely; for users 13–17, both alternative payment and out-of-app offers must sit behind a parental gate (higher age thresholds apply in storefronts with a higher parental-consent age) — [developer.apple.com/support/dma-and-apps-in-the-eu](https://developer.apple.com/support/dma-and-apps-in-the-eu)
- The European Commission has approved Apple's new EU terms (per one outlet), even though Epic disputes their adequacy — [AppleInsider, "European Commission approves of Apple's new App Store terms even if Epic doesn't"](https://appleinsider.com/articles/26/08/20/european-commission-approves-of-apples-new-app-store-terms-even-if-epic-doesnt) (secondary; corroborate against an EC press release before citing as final/settled, since Epic's disagreement suggests possible further dispute)

### Inferences
- For a solo developer with a small EU subscriber base, the realistic near-term choice is **in-app alternative payment processing** (20%/10%) rather than standing up an alternative marketplace or Web Distribution — the eligibility bar for the latter (audits, $1M letter of credit, 1M installs, etc.) is clearly built for scaled companies, not indie apps. The 20% (or 10% for qualifying programs/renewals) alternative-in-app-processing rate is only modestly better than Apple IAP's own 15% SBP rate, so unless a developer already has a payment processor relationship with materially better economics, it may not be worth the integration complexity for a first app. This is a synthesis judgment, not a directly sourced recommendation.
- The 12-month payment-option lock-in is an operationally important constraint a solo developer must plan around — switching payment strategy mid-year is not free.

### Gaps
- Direct confirmation of the European Commission's official position/press release on the Aug 2026 terms (only a secondary AppleInsider summary was found; Epic's specific objections were not investigated).
- Whether the pre-Oct-2026 EU External Purchase Link entitlement's terms (which existed before this unification) differed meaningfully in commission rate from the new Store Services Commission — not investigated in this session; if the report-writer needs a "before vs after Oct 2026" comparison table, an additional fetch of Apple's pre-August-2026 EU terms (e.g. via a web archive) would be needed.

---

## 6. Japan: Mobile Software Competition Act (effective December 2025)

### Takeaway
Japan's Mobile Software Competition Act ("Smartphone Act") took effect **December 18, 2025**. Apple's compliance, rolled out with **iOS 26.2**, opens Japan to alternative app marketplaces, the ability to operate an alternative marketplace, and processing app payments for digital goods/services outside Apple IAP — a structurally similar posture to the EU DMA changes, but arriving via Japanese law rather than EU regulation. The Japan Fair Trade Commission (JFTC) has signaled a dialogue-first enforcement posture rather than immediate sanctions.

### Cited Findings
- The Mobile Software Competition Act entered into force on Dec 18, 2025 — [Apple Newsroom, "Apple announces changes to iOS in Japan" (Dec 2025)](https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/); corroborated by [Bloomberg, "Apple Makes Changes to iOS Software in Face of Stricter Japanese Rules"](https://www.bloomberg.com/news/articles/2025-12-18/apple-aapl-makes-changes-to-ios-software-in-face-of-stricter-japanese-rules) and [KU Leuven CiTiP blog](https://www.law.kuleuven.be/ccm/blog/posts/japan_mobile_software_competition_act)
- Beginning with **iOS 26.2**, developers in Japan can: distribute apps on alternative app marketplaces, operate alternative app marketplaces, and process app payments for digital goods/services outside of Apple In-App Purchase — [Apple Developer News, "Changes to iOS in Japan"](https://developer.apple.com/news/?id=074b3wzz)
- Apple introduced new safeguards alongside these changes, including iOS app notarization, an authorization process for app marketplaces, and protections aimed at younger users — [Apple Newsroom (Dec 2025)](https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/)
- The JFTC, after roughly 18 months of preparation, is expected to lead with "dialogue and guidance" as its primary enforcement tool rather than immediate sanctions; whether it will escalate to sanctions for inadequate compliance is described as uncertain — [Kluwer Competition Law Blog, "Japan's Mobile Software Competition Act Grows its Guidelines"](https://legalblogs.wolterskluwer.com/competition-blog/japans-mobile-software-competition-act-grows-its-guidelines/)

### Inferences
- For a solo developer, Japan's changes mirror the EU pattern: an alternative-payment-processing option now technically exists, but the practical value for a tiny developer likely depends on the specific commission rates Apple charges for in-app alternative processing / out-of-app links in Japan, which were **not located this session** (see Gaps) — do not assume Japan's rates match the EU's 20%/15% figures without confirmation.

### Gaps
- Apple's specific Japan commission rates for alternative in-app payment processing and out-of-app linked offers (analogous to the EU's 20%/15%/10% structure) — not found in this session; the Apple Developer News item on Japan changes was found via search but not fetched in full.
- Whether Japan's regime includes anything resembling the EU's Core Technology Commission or a Japan-specific equivalent fee for alternative marketplaces.

---

## 7. South Korea, Netherlands, and other 2025–2026 changes

### Takeaway
**South Korea**: the 2021 Telecommunications Business Act amendment (world's first law of this kind) requires alternative payment methods; Apple complies via the Korea-specific StoreKit External Purchase entitlement, but in August 2026 Korea's regulator found Apple (and Google) still effectively nullified the law by charging ~26% fees on non-IAP transactions, i.e., a live, unresolved enforcement dispute. **Netherlands**: the long-running ACM dating-apps case is still not fully resolved as of March 2026 — Apple submitted an adjusted compliance proposal, and ACM postponed enforcement pending review; the existing Netherlands-only dating-app entitlement charges a reduced **3%** commission on external purchases (confirmed via direct fetch of Apple's own entitlement page).

### Cited Findings
- South Korea's National Assembly passed the amendment to the Telecommunications Business Act in August 2021, the first law of its kind requiring alternative payment methods; enforced by the Korea Communications Commission (KCC), which can fine violators up to 3% of Korea-generated turnover — [TechCrunch (2022), cited via search synthesis](https://techcrunch.com/2022/01/10/apple-to-allow-third-party-app-payment-options-in-south-korea)
- In August 2026, a Korean regulator (described as the "media watchdog") concluded Google and Apple violated the law by allowing third-party payment gateways while still imposing ~26% transaction fees on non-IAP purchases, which critics say effectively nullifies the law's intent — [Korea JoongAng Daily, "Korea watchdog finds Google and Apple violated app payment law"](https://www.koreajoongangdaily.com/business/korea-finds-google-apple-violated-inapp-purchases-law/12822157)
- Apple's Korea compliance mechanism is the StoreKit External Purchase Entitlement, available to apps distributed solely on the Korea App Store storefront, allowing an alternative in-app payment processing option — [Apple Developer News, "Update on apps distributed in South Korea"](https://developer.apple.com/news/?id=q0feipe4) (cited via search synthesis; not independently fetched in full this session)
- Netherlands: ACM's original Aug 2021 decision found Apple imposed unreasonable conditions on dating-app providers; a Dutch court (Rotterdam) upheld this decision on Jun 16, 2025; Apple was fined a cumulative €50 million in penalty payments over the course of the dispute — [ACM, "District Court of Rotterdam confirms ACM decision"](https://www.acm.nl/en/publications/district-court-rotterdam-confirms-acm-decision-apple-abused-its-dominant-position-dating-apps); [Taylor Wessing summary](https://www.taylorwessing.com/en/insights-and-events/insights/2025/09/dutch-court-upholds-apple-sanctions-for-unfair-conditions-imposed-on-dating-app-providers)
- On **March 27, 2026**, Apple submitted an adjusted proposal for Netherlands dating-app compliance; ACM postponed enforcement of its decision pending review of the new proposal, which will go out for market consultation before ACM rules on compliance — [ACM, "ACM to assess adjusted proposal of Apple regarding its conditions for dating apps"](https://www.acm.nl/en/publications/acm-assess-adjusted-proposal-apple-regarding-its-conditions-dating-apps)
- Apple's own Netherlands dating-app entitlement page (fetched directly this session) confirms: entitlement applies **only** to dating apps on the **Netherlands** App Store storefront; Apple charges a **reduced 3% commission** on the user-paid price (net of VAT, excluding payment-processing-related value); developers are responsible for collecting/remitting applicable taxes (e.g. Dutch VAT); developers must call `canMakePayments()` before each link use, confirm the Netherlands storefront via StoreKit APIs, show a mandated English/Dutch disclosure sheet ("You're about to leave the app and go to an external website. You will no longer be transacting with Apple."), link directly to an HTTPS URL (≤1,000 ASCII characters, no redirects, no URL parameters/user data without consent) in a **new browser window** (not a webview), get the URL approved via App Review, provide their own customer support for the external purchase (Apple explicitly will not help with refunds/payment history/subscription management for these), and submit **weekly sales reports** to Apple within 15 calendar days of Apple's fiscal week close, with invoices payable within 45 days — [developer.apple.com/support/storekit-external-entitlement/](https://developer.apple.com/support/storekit-external-entitlement/) (primary source, fetched directly, high confidence)

### Inferences
- The Netherlands dating-app entitlement is a useful **template for what "web-sale obligations" look like in Apple's own words** wherever an External Purchase Link entitlement applies (disclosure sheet, no Apple-side refund/support help, developer-run tax remittance, periodic sales reporting to Apple, App-Review-gated URLs) — a report-writer could reasonably generalize this operational checklist (self-serve support, tax remittance, reporting cadence) to other entitlement-based link-out regimes (Korea, and pre-unification EU) even where the exact commission rate differs, since the *procedural* requirements Apple imposes appear to follow a consistent pattern across entitlements. This is INFERENCE — the US anti-steering carve-out (§1) is legally distinct (court-ordered, not an Apple-granted entitlement) and its specific procedural requirements were not confirmed to match this pattern exactly.
- South Korea is a cautionary data point: even where a law has existed since 2021, a determined platform can keep effective compliance low by pricing the "alternative" option close to (or, per the regulator's Aug 2026 finding, not meaningfully below) the standard IAP rate — a solo developer should not assume "alternative payment allowed by law" implies "alternative payment is meaningfully cheaper in practice" without checking Apple's actual published commission for that storefront.

### Gaps
- Apple's exact current commission rate for the Korea StoreKit External Purchase Entitlement (the ~26% figure found is attributed to regulator findings about the effective fee, not confirmed as Apple's officially published entitlement-page rate) — the Apple Developer News page on Korea was not fetched in full this session.
- Current resolution status/outcome of the Netherlands ACM proceeding beyond March 27, 2026 (postponement) — no later update found; likely still pending as of Sept 2026, but not confirmed.
- No information gathered this session on any other 2025–2026 jurisdiction changes beyond the US, EU, Japan, South Korea, and Netherlands (e.g., UK CMA, Brazil CADE, India CCI) — out of scope per the assignment, but flagged in case the report-writer wants a "also watch" list; UNKNOWN/not researched.

---

## 8. Recommendation pattern for a first subscription app

### Takeaway (synthesis/INFERENCE — built on all cited findings above, not itself a directly sourced claim)
Start with **plain IAP** (Small Business Program, 15%) for a first subscription app in nearly all cases; add a **web purchase link** only once there is a specific, concrete reason that outweighs IAP's proven higher conversion and near-zero operational burden.

**Stay on plain IAP when:**
- This is the developer's first paid app and there is no pre-existing warm audience to direct to a web paywall — RevenueCat's data (§2) shows link-outs convert meaningfully worse and net less revenue even after fee savings, so for a cold-start audience IAP's higher conversion likely dominates any fee savings.
- The developer wants to minimize operational surface area: IAP means Apple handles payment collection, tax remittance (Apple is the merchant of record for IAP), refunds, chargebacks, and receipt/restore logic via StoreKit — none of which the developer has to build.
- The subscription price point is low enough (e.g., $9.99/mo) that the absolute dollar difference between 85% (SBP) and ~90–94% (web/MoR) take-home is small in early days, while the engineering time to stand up a compliant web-checkout-plus-entitlement-sync system is not small for a solo developer.

**Consider adding a web purchase link when:**
- The developer already has an engaged, price-motivated audience outside the app (email list, existing community, content marketing funnel) that can be routed to a web paywall without relying on in-app discovery — this is the scenario where web conversion loss is smallest relative to the audience's baseline intent.
- Annual revenue is approaching or has crossed the Small Business Program's $1M threshold, where the standard 30%/15%(after Y1) IAP economics become meaningfully worse than a ~5–10% MoR alternative — the fee delta at that point is large enough to justify the operational investment.
- The developer is building a Mac app that cannot pass Mac App Store review at all (sandbox/private API needs) — in that case there **is no IAP option**, and Developer ID + notarization + a web billing provider (§3, §4) is the only route; here the "web checkout" choice is not optional; it's the whole business model.
- US-specific: given the 0%-commission window described in §1 is temporary and litigation-dependent, a developer adding a US link-out today should treat it as an experiment to measure their own conversion delta (per RevenueCat's methodology) rather than a permanent architecture decision, since the commission on that path may change materially within the same calendar year.

**Regardless of path chosen**, budget engineering time for: entitlement sync between web and app (RevenueCat Web Billing, §4, is one way to avoid building this from scratch), restore-purchase UX parity, and — for any web/direct path — sales-tax/VAT handling (either via a merchant-of-record's built-in remittance or the developer's own registration), refund/chargeback policy, and customer support capacity, since Apple explicitly does not extend its own support/refund infrastructure to external-purchase-link transactions (confirmed pattern from the Netherlands entitlement text, §7).

### Gaps
- No direct, sourced "recommendation" from Apple, RevenueCat, or another authority was found stating this exact decision framework; this section is the research agent's synthesis across the cited data points above and should be presented to the report-writer as INFERENCE/synthesis, not as an independently-sourced recommendation.

---

## Session constraint note
Web search and web fetch tools hit a session-level rate limit partway through research, then recovered later in the same session, allowing a follow-up verification pass. **Resolved during the follow-up pass:** Stripe (processing/Billing/Tax/Managed Payments), Paddle, and Lemon Squeezy pricing (all confirmed via direct vendor-page fetch — see §2 and §4 "VERIFIED" callouts), and Sparkle framework capabilities (confirmed via direct fetch of sparkle-project.org — see §3). **Still unresolved / flagged as gaps:** exact current text of Guidelines 3.1.1/3.1.1(a)/3.1.3/3.1.3(a) (§1), precise Supreme Court docket dates (§1), FastSpring's fee schedule (§2/§4), RevenueCat Web Billing's own fee (§4), Apple's notarization/hardened-runtime documentation body text (the doc page is JS-rendered and did not yield readable content to the fetch tool either before or after the rate-limit reset — §3), Apple's Japan and Korea-specific alternative-payment commission rates (§6/§7), and the Netherlands ACM proceeding's status beyond March 27, 2026 (§7). **Recommend the report-writer or a follow-up pass re-verify these specific remaining items** before treating them as settled fact, since this topic area has changed repeatedly through 2025–2026.

---

## Proposed structural responses for app-workshop

*(Researcher proposes; implementation is out of scope for this pass.)*

### `modules/commerce/README.md` — proposed additions
1. **New section: "Beyond IAP: web checkout, alternative payment, and direct Mac sale (2026)."** Summarize, with dates and citations: (a) the US link-out is currently 0% Apple commission but litigation-pending (cite Ninth Circuit contempt ruling, SCOTUS cert, Apple's Aug 14 2026 proposed 15%/10%/5% rate filing — see §1 above); (b) the EU's Oct 1, 2026 unified terms (26%/15% IAP, 20%/10% alt-in-app-processing, 15%/10% out-of-app link, 5% Core Technology Commission for marketplace/web distribution — see §5); (c) Japan's Dec 18, 2025 Mobile Software Competition Act opening similar alternative-payment options (§6); (d) Netherlands (dating apps only, 3% entitlement, §7) and Korea (entitlement exists but regulator disputes its effectiveness, §7) as narrower, category/country-specific precedents.
2. **New subsection: "Choosing a web billing provider."** A short comparison table: Stripe (direct, developer is merchant of record, lowest fees, most tax/compliance burden), Paddle/Lemon Squeezy (merchant of record, ~5%+$0.50 headline — flagged in these notes as needing fresh verification against paddle.com/lemonsqueezy.com), FastSpring (enterprise MoR, no public self-serve rate), RevenueCat Web Billing (entitlement-unification layer over any of the above). Link to RevenueCat's web billing docs (https://www.revenuecat.com/docs/web/web-billing/overview) as the starting integration reference.
3. **New subsection: "Take-home math worksheet."** Reproduce the §2 arithmetic pattern (price × (1 − commission) − fixed fee) as a small formula/table developers can re-run with current rates, explicitly dated and flagged as needing rate re-verification at time of use given how frequently these numbers have changed in 2025–2026.
4. **Caveat banner at top of file:** "Payment-routing rules for iOS/Mac apps changed substantially and repeatedly in 2025–2026 across the US (litigation), EU (DMA), Japan, Korea, and Netherlands. Always re-check developer.apple.com/support/dma-and-apps-in-the-eu, developer.apple.com/app-store/review/guidelines, and the relevant country-specific Apple support page before relying on a specific commission percentage."

### `templates/generated-app/docs/release/CHECKLIST.md` — proposed expansion of the existing Mac-direct-distribution line
Existing line: *"If distributing a Mac app directly, verify Developer ID signing, hardened runtime, notarization, packaging, update delivery, and support for that route."*

Proposed expansion into sub-checklist items (each mappable to a `config/troubleshooting.json` rule below):
- [ ] Apple Developer Program membership is active (paid, $99/yr) — required for Developer ID certificates and notarization; there is no free-tier path to Gatekeeper-trusted direct distribution.
- [ ] App is signed with a "Developer ID Application" certificate and built with the Hardened Runtime capability enabled.
- [ ] App has been submitted via `notarytool` and successfully notarized (not the deprecated `altool` flow).
- [ ] Notarization ticket has been **stapled** to the app bundle / installer (`xcrun stapler staple`) so Gatekeeper can validate offline without a network call to Apple.
- [ ] Update delivery mechanism is in place (e.g., Sparkle appcast) and update packages are themselves signed/verified (e.g., Sparkle's EdDSA signing) — do not ship an updater that fetches unsigned code.
- [ ] Payment/licensing model decided and implemented: license-key (simpler, no server-side entitlement refresh) vs. account-based subscription (requires a running entitlement-check against a chosen billing provider — see `modules/commerce/README.md`).
- [ ] If selling a subscription outside the App Store, a plan exists for: tax registration/remittance (or a merchant-of-record that handles it), refund policy, chargeback handling, and customer support — none of this is provided by Apple for direct-distribution sales.
- [ ] Confirmed the app's required capabilities (sandbox exceptions, private APIs, deep system access) are in fact incompatible with Mac App Store review before committing to the direct-distribution path, since it forfeits App Store discovery and Apple-handled payments/tax/support.

### `config/troubleshooting.json` — proposed new rule entries
Proposed entries (id, title, symptom, 3 checks, one developer.apple.com source each):

```json
[
  {
    "id": "mac-direct-gatekeeper-warning",
    "title": "Mac app shows Gatekeeper 'unidentified developer' warning after direct download",
    "symptom": "Users report macOS blocks the app with a warning that the developer cannot be verified, even though the app was signed.",
    "checks": [
      "Confirm the app was signed with a 'Developer ID Application' certificate (not just an ad-hoc or development certificate).",
      "Confirm the app was actually notarized via notarytool and the submission returned an 'Accepted' status, not just signed.",
      "Confirm the notarization ticket was stapled to the app/installer with `xcrun stapler staple` before distribution."
    ],
    "source": "https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution"
  },
  {
    "id": "mac-direct-notarization-requires-paid-membership",
    "title": "Cannot notarize a Mac app / no Developer ID certificate available",
    "symptom": "Xcode or notarytool cannot create a Developer ID certificate, or notarization submission is rejected for account/entitlement reasons.",
    "checks": [
      "Confirm the Apple Developer Program membership is active and paid (not a free Apple ID account) — Developer ID and notarization require paid enrollment.",
      "Confirm the correct certificate type ('Developer ID Application' / 'Developer ID Installer') is being generated, not a Mac App Store distribution certificate.",
      "Confirm the Apple ID used is an admin/account-holder role with permission to create Developer ID certificates in the team."
    ],
    "source": "https://developer.apple.com/programs/"
  },
  {
    "id": "us-external-purchase-link-rejected",
    "title": "App Review rejects or flags an external/web purchase link on the US storefront",
    "symptom": "A submitted build using an external payment link or call-to-action button is rejected under Guideline 3.1.1/3.1.3 despite the US anti-steering carve-out.",
    "checks": [
      "Confirm the build/metadata correctly targets the US storefront only, since the no-entitlement-required link-out permission is US-storefront-specific and other storefronts still require a separate entitlement or different terms.",
      "Confirm the link/button implementation avoids the UX patterns previously found non-compliant in litigation (e.g., misleading framing, obstructive interstitials, or button styling designed to discourage use) even though no Apple entitlement application is required in the US.",
      "Re-check the current text of Guideline 3.1.1(a)/3.1.3(a) directly, since Apple has revised this guidance multiple times during 2025-2026 litigation."
    ],
    "source": "https://developer.apple.com/app-store/review/guidelines/"
  },
  {
    "id": "eu-alternative-payment-eligibility-confusion",
    "title": "Developer unsure which EU payment option (IAP / alternative in-app processing / web link / marketplace) applies to their app",
    "symptom": "Confusion over which of the post-Oct-2026 unified EU business terms commission tiers (26%/15% IAP, 20%/10% alt-processing, 15%/10% out-of-app link, 5% CTC) apply, or whether the app qualifies for alternative distribution.",
    "checks": [
      "Confirm whether the app is being distributed via the App Store (IAP/alt-processing/out-of-app-link rates apply) versus an alternative marketplace or Web Distribution (5% Core Technology Commission applies instead, plus its own eligibility criteria).",
      "If considering an alternative marketplace or Web Distribution, confirm the app/company meets at least one of the seven published eligibility criteria (e.g., financial audit, $1M standby letter of credit, or 1,000,000 first-year installs) before investing engineering time.",
      "Confirm the 12-month payment-option lock-in is acceptable before switching, since Apple requires maintaining the chosen EU payment option for a full year."
    ],
    "source": "https://developer.apple.com/support/dma-and-apps-in-the-eu"
  },
  {
    "id": "web-purchase-entitlement-sync-missing",
    "title": "User who purchased via a web/external purchase link has no access in the app",
    "symptom": "After completing checkout on an external website, the app does not unlock the subscribed content, or 'Restore Purchases' does not find the entitlement.",
    "checks": [
      "Confirm the web billing provider (or RevenueCat/other entitlement layer) is actually pushing entitlement state to the app's backend or SDK, since Apple's own restore/entitlement sync does not cover externally-purchased transactions.",
      "Confirm the app's entitlement check queries the external billing provider's account/session (e.g., an authenticated account tied to email) rather than only checking StoreKit/App Store receipt state.",
      "Confirm the required disclosure/consent flow (e.g., the mandated 'leaving the app' sheet for entitlement-based link-outs) was shown and did not block the purchase-completion redirect back to an account-linking step."
    ],
    "source": "https://developer.apple.com/support/storekit-external-entitlement/"
  }
]
```
