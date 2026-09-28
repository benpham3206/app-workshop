# 08 Fact-check — App Store to first subscriber (checked 2026-09-27)

Summary: 1 CORRECTED (beta builds OK for internal+external TestFlight) · 2 CONFIRMED · 3 CONFIRMED · 4 CONFIRMED · 5 CORRECTED (Apple says within 45 days; USD min = $0.02) · 6 CONFIRMED · 7 PARTLY CONFIRMED / subs half UNVERIFIABLE · 8 CONFIRMED · 9 CONFIRMED · 10 CORRECTED (cert granted 2026-06-30; proffer filed 2026-08-13; 15/10/5 not verified in filing) · 11 CONFIRMED (CTC only outside App Store) · 12 MOSTLY CONFIRMED (Apple enforcing TX since 2026-06-04; "developers do age checks" corrected) · 13 CONFIRMED · 14 CONFIRMED · 15 CONFIRMED · 16 CONFIRMED (applies to all online distance contracts) · 17 CONFIRMED as Apple's "might" (usually not owed) · 18 CONFIRMED · 19 CONFIRMED · 20 CORRECTED (93¢ = app revenue with web button vs IAP-only) · 21 CONFIRMED · 22 CONFIRMED · 23 CONFIRMED

## Claim 1 — Beta Xcode/SDK submission block; Xcode 27 date; SDK floors
**Verdict: CORRECTED (partly)**
- CONFIRMED: Xcode 27 (27A266a) released 2026-09-14 — https://developer.apple.com/news/releases/ (entry dated 2026-09-14). Also Xcode 27.1 beta (27A9269) 2026-09-18 and Xcode 27.2 beta (27B5019j) 2026-09-16 listed.
- CONFIRMED: SDK 26 floor from 2026-04-28 — https://developer.apple.com/news/?id=ueeok6yw ("Upcoming SDK minimum requirements", dated 2026-02-03). Covers iOS/iPadOS/tvOS/visionOS/watchOS 26 SDK; macOS not listed. Note: Apple's text is phrased as SDK requirement, not "Xcode 26".
- CONFIRMED: SDK 27 floor "Starting April 2027" — https://developer.apple.com/news/?id=k1mtkt1k ("App Store submissions now open for the latest OS releases", dated 2026-09-09) and https://developer.apple.com/app-store/submitting/ (undated, read 2026-09-27). NEW detail the notes miss: the submitting page adds that iOS/iPadOS apps must also "target iOS 15 or later" from April 2027.
- CORRECTED (TestFlight paths): Apple's App Store Connect release notes (https://developer.apple.com/help/app-store-connect/release-notes/) explicitly allow beta-Xcode/beta-SDK builds for **both internal AND external TestFlight testing** — e.g. 2026-09-18: "You can now submit apps built with Xcode 27.1 beta ... for internal and external testing"; same wording for Xcode 27 betas 1–6 (2026-06-09 → 2026-08-25) and 27.2 beta (2026-09-16). Only GM/RC builds are listed "for the App Store" (Xcode 27 RC 2026-09-09; Xcode 27 2026-09-14). So: beta builds → TestFlight internal + external OK (external still goes through Beta App Review); App Store submission blocked. Note 02's "apparently not all TestFlight internal testing" and the inference that only internal testing tolerates beta builds are wrong/understated. Note also the RC build is App-Store-eligible (not only GM).

## Claim 2 — Paid Apps Agreement gates IAP creation; Account Holder only
**Verdict: CONFIRMED (with wording nuance)**
- https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements (undated help page, read 2026-09-27): "Required role: Account Holder"; "You won't be able to create a new app or In-App Purchase until you've agreed to the most recent version of the Paid Apps Agreement." Also "This agreement must be active in order for you to submit or update paid apps and In-App Purchases."
- Nuance: the creation gate is phrased as having *agreed to* the latest version; the *Active* status (which also needs tax + banking) is what's required to submit/update paid apps/IAPs. Note 01's "Until that agreement reads 'Active' you cannot even create..." slightly overstates the creation gate; the submission gate is "active".

## Claim 3 — First IAP/subscription must ship with a new app version
**Verdict: CONFIRMED (per type)**
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-purchase (undated, read 2026-09-27): "The first consumable, non-consumable, auto-renewable subscription, and non-renewing subscription In-App Purchase of each type must be submitted with a new app version." After the first of a type is approved, later items of that type can be submitted without a new version (app must have ≥1 approved version).

## Claim 4 — Small Business Program
**Verdict: CONFIRMED**
- https://developer.apple.com/app-store/small-business-program/ (undated; example uses 2022; read 2026-09-27): eligibility up to USD 1M proceeds in prior calendar year (incl. Associated Developer Accounts); exceeding $1M mid-year → standard rate applies to future sales only (not retroactive); reduced commission takes effect "fifteen (15) days after the end of the fiscal calendar month" in which enrollment is approved (example: approved Feb 10, 2022 → proceeds adjusted from Mar 14, 2022). So "~15 days" is 15 days after *fiscal-month end*, not after approval — up to ~6–7 weeks from approval.

## Claim 5 — Payout timing and USD minimum threshold
**Verdict: CORRECTED**
- Apple's own wording: payments are made "within 45 days of the last day of the fiscal month in which the transaction was completed" — https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments (undated, read 2026-09-27). "~33 days, on a Thursday" is a secondary-source observation of typical practice, not Apple's commitment; the notes should cite 45 days as Apple's stated max. (The old fiscal-calendar URL returns 404; no primary 2026 payment-date table found.)
- USD minimum threshold FOUND (Note 01 listed it as a GAP): https://developer.apple.com/help/app-store-connect/reference/reporting/minimum-payment-threshold (undated, read 2026-09-27) — United States bank / USD account: minimum payment **USD 0.02**; any bank country/currency not in the table: **USD 40**. So for a US developer with a USD account, a single subscriber's proceeds clear the threshold; there is effectively no roll-forward.

## Claim 6 — Apple $5,000 1099-K vs IRS $20,000/200
**Verdict: CONFIRMED**
- Apple: https://developer.apple.com/help/app-store-connect/manage-tax-information/manage-invoices-and-other-tax-documents/ (undated, read 2026-09-27) still says "at least $5,000" unadjusted gross sales; notes pre-2024 threshold was $20,000 and >200 transactions. Mailed by Jan 31.
- IRS: https://www.irs.gov/businesses/understanding-your-form-1099-k (last reviewed 2026-06-28) — "over $20,000 in more than 200 transactions"; https://www.irs.gov/newsroom/irs-issues-faqs-on-form-1099-k-threshold-under-the-one-big-beautiful-bill-dollar-limit-reverts-to-20000 — OBBB **retroactively** reinstated the pre-ARPA threshold. Correction to framing: it is retroactive (not merely "2025+"). Apple's page is stale vs. federal law (Apple may still voluntarily issue at the lower amount; unknown).

## Claim 7 — Membership lapse: apps removed, existing subscriptions continue
**Verdict: PARTLY CONFIRMED / subscription half UNVERIFIABLE**
- CONFIRMED: https://developer.apple.com/help/account/membership/renewal/ and https://developer.apple.com/support/renewal/ (undated, read 2026-09-27): apps "will no longer be available for download", no new submissions/updates or Certificates/IDs/Profiles access, but "your apps will still function for users who have already installed or downloaded them." Renewal: free apps return within 24h; paid apps after re-accepting the Paid Applications Agreement.
- UNVERIFIABLE: neither page (the one Note 01 cites) says anything about existing auto-renewable subscriptions continuing to renew/bill after a membership lapse. Tried: both renewal pages, App Store Connect "remove app" help (404), site-restricted search of developer.apple.com (only forum threads, about *removing an app from sale* while leaving IAP on sale — a different scenario). Note 01 labels this FACT; it should be downgraded to unconfirmed. Practical risk: whether renewals continue, and whether proceeds are paid while the Paid Apps Agreement is lapsed, is unknown from primary sources.

## Claim 8 — Individuals' seller name = legal name; no DBA
**Verdict: CONFIRMED**
- https://developer.apple.com/help/account/membership/program-enrollment/ (undated, read 2026-09-27): "If you're an individual or sole proprietor/single-person business, your personal legal name will be listed as the seller on the App Store. Do not enter an alias, nickname, or company name..." and for organizations "We don't accept DBAs, fictitious businesses, trade names, or branches." Also https://developer.apple.com/programs/enroll/ ("Your name will be displayed as the seller name"). Note: the exact sentence "You cannot use a DBA ... instead of your legal name" quoted in Note 01 line 85 was not found verbatim on /programs/enroll/ as fetched; the substance is confirmed by the program-enrollment help page.

## Claim 9 — EU DSA trader-status removal since 2025-02-17
**Verdict: CONFIRMED**
- https://developer.apple.com/news/?id=einwn76m ("Apps without trader status will be removed from the App Store in the EU", dated 2025-01-16): "Starting February 17, 2025 ... apps without trader status will be removed from the App Store in the European Union until trader status is provided and verified."

## Claim 10 — Epic v. Apple status
**Verdict: CORRECTED (dates/details); core picture confirmed**
- CONFIRMED: Ninth Circuit judgment 2025-12-11 (9th Cir. No. 25-2935) — recorded as the lower-court decision date on the SCOTUS docket https://www.supremecourt.gov/docket/docketfiles/html/public/25-1311.html (read 2026-09-27). (Justia opinion URL returned 403 to fetch; docket used instead.)
- CORRECTED: cert **granted 2026-06-30**, "limited to Question 1" (whether contempt can rest on violating an injunction's "spirit") — same docket. Note 04's "per one source, July 2, 2026" is wrong. Petition filed 2026-05-21 (docketed 05-27). Apple merits brief + joint appendix filed 2026-09-14; Epic's brief due 2026-11-13.
- CONFIRMED: Kagan denied Apple's stay-of-mandate application 25A1213 on 2026-05-06 — https://www.supremecourt.gov/docket/docketfiles/html/public/25a1213.html.
- MISSED by notes: second application 26A194 (stay of district-court remand proceedings) — Kagan granted a 24-hour administrative stay 2026-08-12, then **denied 2026-08-13** — https://www.supremecourt.gov/docket/docketfiles/html/public/26a194.html. District court (YGR) had denied Apple's stay motion 2026-08-11 (N.D. Cal. Dkt 1706).
- CORRECTED date: Apple's filing proposing link-out commission was **"Apple Inc.'s Remand Proffer," filed 2026-08-13** (N.D. Cal. 4:20-cv-05640, Dkt 1708, redacted; sealing motion Dkt 1709), plus an administrative motion for referral to a settlement conference (Dkt 1710, Epic opposed 08-17) — https://www.courtlistener.com/docket/17442392/epic-games-inc-v-apple-inc/ (last updated 2026-09-26). TechCrunch's 08-14 date is the article date. The 15%/10%/5% (+10% renewals) figures could not be verified from the primary filing (would require downloading the PDF — not done); they rest on TechCrunch/MacRumors/9to5Mac. No order approving any rate appears on the docket through 2026-09-25.
- CONFIRMED (0% today): App Review Guidelines 3.1.1(a) (https://developer.apple.com/app-store/review/guidelines/, read 2026-09-27, no date shown): entitlements "are not required for developers to include buttons, external links, or other calls to action in their United States storefront apps"; no commission stated. With no approved rate on the docket, US link-outs are currently commission-free.

## Claim 11 — EU unified terms 2026-10-01, 5% CTC
**Verdict: CONFIRMED (with scope clarification)**
- https://developer.apple.com/support/dma-and-apps-in-the-eu (read 2026-09-27; no page date shown): unified business terms effective **October 1, 2026**; **5% Core Technology Commission** applies to digital transactions in apps distributed **outside the App Store** (alternative marketplaces, Web Distribution) — not to App Store sales. EU App Store rates: IAP 26% / 15% (SBP, partner programs, subs after year 1); alternative in-app payment 20%/10%; Store Services Commission on linked offers 15%/10% (7-day window). As of today (2026-09-27) these are announced but not yet in force (4 days out).

## Claim 12 — US age-assurance laws
**Verdict: MOSTLY CONFIRMED; "developers responsible for age checks" CORRECTED; Note 05 Apple-Texas status is stale**
- Texas SB 2420 SCOTUS denial 2026-07-06 CONFIRMED: https://www.supremecourt.gov/docket/docketfiles/html/public/25a1389.html — 2026-07-06 "Application (25A1389) to vacate stay ... referred to the Court is denied"; companion CCIA v. Paxton 25A1390 denied same day (Order List 609 U.S., https://www.supremecourt.gov/orders/courtorders/070626zr1_dc8f.pdf). Fifth Circuit stay → law effective 2026-06-04.
- Apple's own current Texas post: https://developer.apple.com/news/?id=sg176nne ("Update for apps distributed in Texas", dated **2026-06-03**) — new Texas Apple Accounts subject to SB 2420 from **2026-06-04**; Apple performs age assurance and parental consent for downloads, IAP and significant changes. Note 05 lines 33/41 rely on the 2025-12-23 "pause" post (https://developer.apple.com/news/?id=8jzbigf4) and call Texas status UNKNOWN — that is stale; Apple resumed on 2026-06-04.
- CORRECTED wording on responsibility: Apple does not say developers are responsible for *age checks*. Apple performs age assurance/consent at the account level; the June 3 post says "it's the developer's responsibility to determine when there's a significant change to their app", and developers request age category via Declared Age Range API, use PermissionKit Significant Change API, and handle consent-revocation server notifications.
- Utah delayed CONFIRMED (secondary + primary bill): HB 498 (2026), https://le.utah.gov/~2026/bills/static/HB0498.html (bill text PDF https://le.utah.gov/Session/2026/bills/enrolled/HB0498.pdf not opened — would be a download); key obligations delayed to 2027-05-06 per Wiley/Mondaq/Loeb; Alston & Bird's LA post says "May 7, 2027" — minor discrepancy, 2027-05-06 is the majority figure. Enforcement = private right of action only.
- Louisiana delayed CONFIRMED: HB 977 enrolled as Act No. 185 of 2026 (https://www.legis.la.gov/legis/ViewDocument.aspx?d=1475238), signed 2026-05-15, new effective date 2027-07-01 (per Alston & Bird; Act PDF not opened). Note Apple's Feb 24, 2026 news post (https://developer.apple.com/news/?id=f5zj08ey) still lists Utah 2026-05-06 / Louisiana 2026-07-01 — Apple's page is stale vs. the amended statutes.
- California AB 1043 CONFIRMED: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1043 — Chapter 675, chaptered 2025-10-13; operative January 1, 2027.

## Claim 13 — Guideline 5.1.2(i) third-party AI; age-rating tiers
**Verdict: CONFIRMED**
- https://developer.apple.com/app-store/review/guidelines/ (read 2026-09-27; no date displayed): 5.1.2(i) "You must clearly disclose where personal data will be shared with third parties, including with third-party AI, and obtain explicit permission before doing so."
- Age ratings: https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions (undated, read 2026-09-27) lists 4+, 9+, 13+, 16+, 18+ (plus Unrated; regional variants for Australia, Brazil, Korea).

## Claim 14 — Amended COPPA Rule compliance date 2026-04-22
**Verdict: CONFIRMED**
- Federal Register 90 FR (2025-04-22), doc 2025-05904, via GovInfo https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm and FTC https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-312-coppa-final-rule-amendments: effective 2025-06-23; "Except with respect to § 312.11(d)(1), (d)(4), and (g), regulated entities have until April 22, 2026 to comply." (federalregister.gov itself redirected to an unblock page.)

## Claim 15 — FTC Click-to-Cancel vacated; California AB 2863
**Verdict: CONFIRMED**
- Eighth Circuit, Custom Communications, Inc. v. FTC, No. 24-3137, opinion filed 2025-07-08, petitions granted and rule vacated (procedural — no preliminary regulatory analysis) — https://ecf.ca8.uscourts.gov/opndir/25/07/243137P.pdf (the "25/07" path and search-result metadata show July 2025; PDF not opened since that would be a download; date corroborated by GovInfo listing https://www.govinfo.gov/app/details/USCOURTS-ca8-24-03137 and many law-firm alerts). The FTC ANPRM date (2026-01-30) was not checked.
- AB 2863: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2863 — Chapter 515, approved 2024-09-24, operative 2025-07-01; defines "free-to-pay conversion" (free trial that auto-converts to paid) and requires keeping proof of express affirmative consent "for at least three years, or one year after the contract is terminated, whichever period is longer."

## Claim 16 — EU withdrawal button from 2026-06-19
**Verdict: CONFIRMED (researcher's flagged item is real; scope corrected)**
- Directive (EU) 2023/2673, EUR-Lex https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2673 (OJ, 2023; read 2026-09-27): inserts **Article 11a** into the Consumer Rights Directive 2011/83/EU — "For distance contracts concluded by the means of an online interface, the trader shall ensure that the consumer can also withdraw from the contract by using a withdrawal function", labelled "withdraw from contract here" or equivalent, continuously available through the withdrawal period, prominently displayed; plus an online withdrawal statement and a confirmation function. Art. 2: transpose by 2025-12-19, "apply those measures from 19 June 2026."
- CORRECTION to Note 05's framing: Art. 11a is not limited to financial services — it applies to **all** B2C distance contracts concluded via an online interface (the directive also extends it to financial-services contracts). INFERENCE (not checked against a primary source): for App Store IAP Apple is the trader/merchant of record, so this obligation mainly bites a developer who sells subscriptions to EU consumers on its own website/web checkout (unless an MoR like Paddle is the trader).

## Claim 17 — HTTPS/OS-crypto-only apps may still owe a BIS year-end self-classification report
**Verdict: CONFIRMED as Apple's statement (it says "might"); practical likelihood is lower than the notes imply**
- https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations (no date shown; read 2026-09-27 via browser): OS-built-in encryption such as "HTTPS connections using URLSession—is exempt from export documentation upload requirements"; "If your app uses exempt forms of encryption, you might alternatively be required to submit a year-end self-classification report to the U.S. government."
- BIS: https://www.bis.gov/learn-support/encryption-controls/annual-self-classification — report required for items exported under License Exception ENC §740.17(b)(1) (unless a CCATS was obtained), due "no later than February 1" of the following year. https://www.bis.gov/learn-support/encryption-controls/mass-market — mass-market items under §740.17(a) "do not require any submission to BIS." Per BIS's 2021 Wassenaar-implementation rule (via BIS search summary; not opened in full), among mass-market items only "components" and "executable software" stay subject to self-classification reporting. So a typical app whose only crypto is OS HTTPS usually owes nothing to BIS; "may still owe" is accurate but should be framed as an edge case to confirm, not a likely obligation. The "~Feb 1" deadline the notes list as unverified is CONFIRMED.

## Claim 18 — Sandbox and subscription mechanics
**Verdict: CONFIRMED**
- https://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings/ (undated, read 2026-09-27): "By default, accounts are set to a speed equalization of 1 month = 5 minutes"; "Subscriptions automatically renew up to 12 times before auto-renewal turns off on the thirteenth renewal attempt." Default-rate sandbox billing retry 10 min, grace 5 min (1-month).
- https://developer.apple.com/app-store/subscriptions/ (undated, read 2026-09-27): grace period "3, 16, or 28 days"; "When a subscription renewal fails, Apple attempts to recover it for 60 days"; Family Sharing: "Please note that this can't be undone."

## Claim 19 — RevenueCat pricing, SDK version, license
**Verdict: CONFIRMED**
- https://www.revenuecat.com/pricing/ (undated, read 2026-09-27): "Pay nothing for up to $2,500 in monthly tracked revenue", "Then pay 1% of what you track once you hit $2,500 in MTR" (Pro plan).
- GitHub API `repos/RevenueCat/purchases-ios/releases` (https://github.com/RevenueCat/purchases-ios/releases), queried 2026-09-27: latest **5.91.0 published 2026-09-23T19:15Z** (not prerelease); prior 5.90.2 (09-18), 5.90.1 (09-17), 5.90.0 (09-17), 5.89.0 (09-09) — matches Note 03 exactly.
- License: GitHub repo metadata spdx_id = **MIT**.

## Claim 20 — RevenueCat study: $0.93 per $1
**Verdict: CORRECTED (framing)**
- Primary: https://www.revenuecat.com/blog/growth/iap-vs-web-purchases-conversion-test/ (Jacob Eiting & Rik Haandrikman; test ran 2025-05-07 → 2025-05-28 on RevenueCat-owned Dipsea; published May 2025): "Once we added a web purchase button, the app made 93¢ for every dollar we made with IAP-only" — after accounting for Apple's fee.
- Correction: the $0.93 is **total app revenue of the web-purchase variant vs. the IAP-only variant**, not "web-linked purchases net $0.93 per $1 of IAP revenue". It's one app, one 3-week US test. Note 04's trial-start figures (IAP ≈27.0% vs web ≈18.1%) do not match the primary article as read (65.6% vs 39.1% completion from CTA tap; "roughly one-third" lower); the ~27/18 figures may be a different base (e.g., per paywall view) cited by Daring Fireball — cite the RevenueCat post directly and state which denominator.

## Claim 21 — Custom Product Pages: keywords, up to 70
**Verdict: CONFIRMED**
- https://developer.apple.com/app-store/custom-product-pages/ (undated, read 2026-09-27): "You can publish up to 70 additional versions of your product page on the App Store for iPhone and iPad." and "You can also assign keywords to your custom product page ... each keyword combination is unique to a single product page."

## Claim 22 — App Store Connect API cannot create an app record
**Verdict: CONFIRMED**
- https://developer.apple.com/documentation/appstoreconnectapi/apps (read 2026-09-27 via browser; no date): operations listed are List apps / Read app information / Modify an app (no Create); overview says "Don't use this API to create new apps; instead, create new apps on the App Store Connect website." Also: the API "doesn't permit you to directly upload your builds" — use Xcode or Transporter (answers part of Note 07's upload-path gap). The quoted 403 "does not allow CREATE" error text in Note 07 was not re-verified.

## Claim 23 — Mac: Accessibility API vs App Sandbox; sandbox mandatory for Mac App Store
**Verdict: CONFIRMED (with wording nuance)**
- https://developer.apple.com/documentation/security/app-sandbox (read 2026-09-27 via browser): "To distribute a macOS app through the Mac App Store, you must enable the App Sandbox capability."
- https://developer.apple.com/documentation/security/protecting-user-data-with-app-sandbox: "Certain activities are forbidden by the operating system when an app runs in a sandbox," including "Use of accessibility APIs in assistive apps", "Sending Apple Events to arbitrary apps", "Terminating other running apps". Apple's wording targets accessibility APIs used to control other apps ("assistive apps"); it doesn't name AXUIElementSetAttributeValue, but controlling other apps' windows is exactly that category. Conclusion stands: window-tiling of other apps via AX is not possible in a sandboxed Mac App Store build.

## Other wrong or stale claims noticed in the notes
1. **05 lines 33 & 41**: say Apple's Texas implementation is paused and status UNKNOWN. Stale: Apple's post "Update for apps distributed in Texas" (https://developer.apple.com/news/?id=sg176nne, 2026-06-03) says new Texas accounts have been under SB 2420 age assurance/parental consent since 2026-06-04.
2. **05 line 32**: Apple's Feb-2026 post dates for Utah (2026-05-06) and Louisiana (2026-07-01) have since been superseded by the statute amendments (2027). Note 05 cites them without saying they're superseded.
3. **01 line 181**: says the USD minimum payment threshold is a GAP. It's USD 0.02 for a US bank in USD, USD 40 for unlisted bank country/currency combinations (https://developer.apple.com/help/app-store-connect/reference/reporting/minimum-payment-threshold).
4. **01 lines 170/174/178**: "~33 days after fiscal month close" should be stated as Apple's "within 45 days"; the 6–10-week first-payout estimate should widen to allow up to 45 days.
5. **01 line 97**: "users with existing active in-app subscriptions retain access" is labelled FACT, but the cited renewal page doesn't say that. Downgrade to unverified.
6. **02 lines 8, 29 (Inferences), 271**: beta-Xcode builds *can* go to external TestFlight testers. Apple's ASC release notes list every Xcode 27 beta as OK "for internal and external testing". Also the **RC** build is App-Store-eligible (2026-09-09), so "GM only" is too strict.
7. **04 line 10**: the cert-grant date "July 2, 2026" is wrong (it was 2026-06-30, limited to Q1). The note also misses the Aug 12–13 SCOTUS administrative-stay episode (26A194, denied) and the 2026-08-11 district-court denial of Apple's stay motion.
8. **07 line 115**: the "Xcode 26 required" floor is cited to a vendor blog (seasiainfotech). Apple's primary notice (https://developer.apple.com/news/?id=ueeok6yw, 2026-02-03) phrases it as an SDK-26 requirement for iOS/iPadOS/tvOS/visionOS/watchOS and doesn't mention macOS.
9. **Not in the notes**: from April 2027, Apple's submitting page also requires iOS/iPadOS apps to "target iOS 15 or later" as well as build with the SDK 27 (https://developer.apple.com/app-store/submitting/).
10. **07 line 128 (upload-path gap)**: Apple's Apps API page says builds are uploaded with Xcode, Transporter or the Transporter Mac app, never via the REST API.
11. **04 line 53**: the IAP-vs-web trial-start percentages (27.0% vs 18.1%) don't match the RevenueCat primary post as read (65.6% vs 39.1% from CTA tap). Re-check the denominator.
12. **05 line 164**: the EU withdrawal button is framed as "financial/distance-contract services". Art. 11a covers all B2C online distance contracts.
