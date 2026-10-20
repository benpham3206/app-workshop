# Per-app website boilerplate

> **Orchestrator filter (2026-10-19), applied against the rules in [`REPORT.md`](REPORT.md#website-the-function-is-the-form) ("the function is the form").**
>
> **Kept:** static HTML/CSS with minimal JavaScript, no framework by default (matches `benpham3206/distribution`); Cloudflare Pages as the default host; the core pages (support, privacy, terms; Apple requires the support and privacy URLs); Smart App Banner, Universal Links, official badge rules; Buttondown for a simple waitlist; the generator fit in §5; all CI checks in §6; the tokens, honest-materials, and reduced-motion rules in §4; the teardown lessons from Raycast ("a product interaction as hero") and Halide ("show the result the product produces").
>
> **Rejected:**
> - *Landing order item 3, "Product image or short, user-started demo".* Under the rule, the hero **is** the working product, live, not an image placed third. The interactive demo moves to position 1 and replaces the image.
> - *Item 5, "Three specific outcomes/features".* This is template order. The page follows the user's journey in the app instead (capture → organize → done → return), and each step is shown working.
> - *GitHub Pages for the dogfood site.* The lane found GitHub's terms exclude commercial services. App Workshop is offered to clients, so its site goes on Cloudflare Pages (see open decision 6 in the report).
>
> **Gap:** the lane read page text only. It did not look at rendered pages, so typefaces, spacing, motion, and contrast are UNKNOWN for all 15 sites. A visual teardown with screenshots is still needed before choosing a visual direction (ledger row 30).


**Decision — INFERENCE:** Generate a small static `site/` for every app from `project.json`: semantic HTML, CSS, and only the JavaScript needed for working interactions. Deploy static assets to Cloudflare Pages by default. Make the App Store download the main call to action after release; before release, use a waitlist. Keep analytics off by default.

A website is the app’s public destination for discovery, download, trust, and support. It should not become an account portal or creator console by default. When a product needs web checkout, account deletion, or a customer portal, add those as explicit modules with their own contracts and checks.

**Evidence key:** FACT is supported by the linked source and was checked on 2026-10-19 unless another date is stated. INFERENCE is a recommendation derived from the evidence or owner-provided direction. UNKNOWN means I could not verify it in this pass. No third-party revenue or performance estimates are used below.

## 1. Indie and productivity site teardown

**Scope — FACT:** I inspected the live page text, links, and available image descriptions for the sites below on 2026-10-19. That establishes their page structure and published claims; it does not establish exactly how their typography, animation, or responsive layouts look when rendered.

**Performance — UNKNOWN:** I did not validate site-specific PageSpeed Insights or CrUX results for these domains. Google says CrUX may lack sufficient page or origin data, and PSI can fall back from page-level to origin-level results. Do not treat a site’s visual polish or marketing claim as field-performance evidence. [Google’s PSI and CrUX data notes](https://developers.google.com/speed/docs/insights/v5/about)

| Site | Observed structure, proof, CTA, and pricing | Transferable premium cue |
|---|---|---|
| [Things](https://culturedcode.com/things/) | **FACT:** Intro and feature video links, screenshots across Apple devices, separate Mac/iPhone/Watch/iPad pricing paths, editorial quotes and awards, newsletter, support, press, privacy, and terms. | **INFERENCE:** The site connects one clear product promise to concrete platform-specific paths and substantial independent proof. Exact visual type and animation behavior: **UNKNOWN**. |
| [Flighty](https://flighty.com/) | **FACT:** Travel-oriented hero, flight-status examples, award marks, sequential feature explanations, repeated App Store download CTA, pricing, help, press, and business links. | **INFERENCE:** Realistic, specific examples make the value legible before asking for a download. Exact motion and typeface: **UNKNOWN**. |
| [Structured](https://structured.app/) | **FACT:** Single-sentence planner proposition, timeline screenshots across iPhone/Mac/Watch, feature exploration, reviews and press logos, help, press kit, and “start free” calls to action. The page publishes usage and review counts as its own claims. | **INFERENCE:** It shows the product across devices and supports claims with proof. Use only measured, current numbers in a generated site. Exact font and animation: **UNKNOWN**. |
| [Tiimo](https://www.tiimoapp.com/) | **FACT:** Hero says who it serves, multi-device product imagery, short sections for focus timer, timeline, customization, and widgets, plus an App Store Award claim and newsroom links. | **INFERENCE:** The page explains user jobs through focused sections instead of one generic feature grid. Exact price display, animation, and typography: **UNKNOWN**. |
| [Bear](https://bear.app/) | **FACT:** Short writing-focused hero, video, feature sections, awards, pricing with free and paid plans, trial and annual/monthly amounts, reviews, newsletter, help, and App Store links. | **INFERENCE:** The price is connected to a plain explanation of what the paid tier adds; the surrounding product copy gives visitors a reason to care. |
| [Craft](https://www.craft.do/for/sales) | **FACT:** The inspected sales page is use-case specific: proposal workflow, product examples, a short “download/write/send” path, comparisons, and plan information. The main site did not load in this text capture. | **INFERENCE:** A targeted page can speak to one buyer’s job more clearly than a broad feature list. Main-site page structure and motion: **UNKNOWN**. |
| [Fantastical](https://flexibits.com/fantastical) | **FACT:** Calendar-focused hero, free-start and Mac-download calls to action, user testimonials, platform support, product sections, press quotes, pricing/support navigation. | **INFERENCE:** Repeated user language and a wide device story reinforce the core promise. Exact type and animation: **UNKNOWN**. |
| [Day One](https://dayoneapp.com/) | **FACT:** Journal-focused hero, App Store/platform routes, award and press marks, feature sections, privacy/data-safety explanation, user stories, review count claim, blog, pricing, help, press, terms, and privacy. | **INFERENCE:** For a trust-sensitive product, explain data ownership and protection beside the product story, not only in the footer. |
| [Raycast](https://www.raycast.com/) | **FACT:** The homepage leads with a keyboard-oriented proposition and product interaction, then shows extension categories, integrations, AI features, and performance claims. | **INFERENCE:** A distinct product metaphor and believable product UI make a more memorable hero than decorative mockups. Exact web animation behavior: **UNKNOWN**. |
| [Halide](https://halide.cam/) | **FACT:** Camera-oriented headline, photo comparisons and sample images, product-specific explanations, privacy claim, one-week trial language, App Store CTA, press kit, and support. | **INFERENCE:** Show the result the product produces, then explain the controls that produce it. |
| [Linear](https://linear.app/) | **FACT:** Product proposition, rich UI examples, customer/resource navigation, sequential feature areas, sign-up routes, and pricing. | **INFERENCE:** Its page behaves like a product tour: recognizable workflow evidence carries the long explanation. |
| [Notion Calendar](https://www.notion.com/en-gb/product/calendar) | **FACT:** Short headline and calendar promise, product video with a visible Play control, feature sequences, language/platform information, free CTA, App Store link, and FAQ. The site page notes that an ad blocker may prevent video playback. | **INFERENCE:** A product demo needs a useful static fallback and a clear play state; the page itself shows why a video-only hero can fail. |
| [Arc](https://arc.net/) | **FACT:** The page now promotes Dia while still presenting Arc download paths and a warning about Arc’s update/security state, alongside feature and privacy claims. | **INFERENCE:** Keep a product’s lifecycle and support status clear when the product changes direction; stale marketing creates trust debt. |
| [Dia](https://www.diabrowser.com/) | **FACT:** Trailer, short promise, download CTA, three concrete workday workflows, more feature explanations, privacy controls, and availability. | **INFERENCE:** A new product can establish identity through a compact promise and clear use cases instead of a long company story. |
| [mymind](https://mymind.com/) | **FACT:** Two-part headline, manifesto, privacy positioning, app/platform routes, feature stories, and visual product examples. | **INFERENCE:** A strong point of view can make a site feel authored, but it should still quickly explain the actual product and download path. |

**Visual audit limitation — UNKNOWN:** The text inspection did not reveal precise typefaces, spacing, motion choreography, or rendered contrast for any of the 15 sites. Those should be evaluated from screenshots/browser playback before adopting a specific visual treatment.

## 2. Functional surface catalog

| Tier | Pages and functions | Recommendation |
|---|---|---|
| **Core** | Landing page, store links, support/contact, privacy, terms when applicable, social preview metadata, app-specific SEO metadata | Every generated site should have a working public home and support path. Apple requires a Support URL for each platform version; it must lead to actual contact information. Apple requires a privacy-policy URL for all apps. [Support URL requirements](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information), [privacy URL requirements](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy) |
| **Core when pre-launch** | Waitlist/email signup, confirmation state, privacy notice, unsubscribe path | Only show signup when the owner has a real plan for sending updates. Collect email with a clear purpose and use double opt-in by default. |
| **Core when paid** | Pricing or plan explanation, current subscription terms, links to Apple subscription management/refund support | Display prices and trial/renewal conditions from actual configured products. For App Store subscriptions, route cancellation and refunds to Apple’s tools unless the product has a distinct web billing contract. |
| **Module** | Account deletion page, universal links/AASA, localized pages, press kit, changelog, privacy-first analytics, support knowledge base, waitlist provider integration | Emit only when the selected product needs the surface. If account creation exists, account deletion must be initiable in the app; a website link may finish the flow, but the app must link directly to that page. [Apple account deletion guidance](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion/) |
| **Later** | Public service status page, long-form content/blog, creator-console entry point, web paywall or account portal | Add a status page when users depend on a hosted service. Keep creator operations such as revenue, reviews, crashes, releases, analytics, and feedback in the separate creator console. |

### Email capture provider comparison

**Recommendation — INFERENCE:** Use Buttondown as the lightest default for a basic product waitlist/newsletter. It has default confirmation, subscriber export, and a low initial price; keep the provider choice explicit in config. For product lifecycle messaging, evaluate Loops. Use Resend when the product has a real transactional-email or custom integration need. Kit fits creator newsletters better than a product waitlist.

| Provider | Price checked 2026-10-19 | Double opt-in | Export and fit |
|---|---|---|---|
| [Buttondown](https://buttondown.com/pricing) | **FACT:** First 100 subscribers are free; features/add-ons are priced separately and list pricing is interactive. Exact 1,000-subscriber total was **UNKNOWN** in this capture. | **FACT:** Default for newsletters and API-created subscribers; API can bypass per subscriber. [Buttondown DOI](https://docs.buttondown.com/double-opt-in) | **FACT:** CSV export is supported. [Export API](https://docs.buttondown.com/api-exports-create). **INFERENCE:** Best fit for a simple waitlist or occasional launch updates. |
| [Loops](https://loops.so/pricing) | **FACT:** Free for up to 1,000 subscribed contacts, with 4,000 combined marketing/transactional sends per rolling 30 days; paid tier begins at $49/month for 1,001–5,000 contacts. | **FACT:** Available and configurable for form/form-endpoint signups; when enabled, contacts must confirm. [Loops DOI](https://loops.so/changelog/double-opt-in) | **UNKNOWN:** I did not verify its export workflow in the docs checked. **INFERENCE:** Stronger fit when segmentation and product lifecycle email matter. |
| [Kit](https://kit.com/pricing) | **FACT:** Free to 10,000 subscribers; Creator plan shown at $33/month for 1,000 subscribers. [Kit plan details](https://help.kit.com/en/articles/16627071-the-kit-free-plan) | **FACT:** Confirmation email/double opt-in is on by default. [Kit DOI](https://help.kit.com/en/articles/2971364-the-all-important-double-opt-in) | **FACT:** Subscriber CSV export supported. [Kit export guide](https://help.kit.com/en/articles/2502489-how-to-export-subscribers-in-kit). **INFERENCE:** Better for a creator publishing a newsletter than an app-only waitlist. |
| [Resend Audiences](https://resend.com/features/audiences) | **FACT:** Resend’s email pricing lists $0 for 3,000 monthly emails and $20/month for 50,000 on Pro. Contact pricing/limits for the Audience feature were **UNKNOWN** in the pages checked. [Resend pricing](https://resend.com/pricing?product=marketing) | **UNKNOWN:** I did not verify built-in DOI behavior. | **FACT:** Audience supports API/CSV import and unsubscribe handling. **UNKNOWN:** Export workflow not verified. **INFERENCE:** Best when email is integrated into a developer-owned workflow, not as the easiest hosted waitlist. |

**Safety — INFERENCE:** Never place an email-provider secret in browser JavaScript. Use the provider’s hosted form/embed, or a server-side endpoint with validation and abuse controls.

### Apple and App Store web surfaces

- **FACT:** Use Apple’s official badge artwork. The black badge is preferred; do not alter, angle, or animate it. On-screen minimum height is 40 px, with required clear space. [Apple App Store marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/)
- **FACT:** A Smart App Banner uses Apple’s `apple-itunes-app` meta tag with the App Store ID and optional app argument. [Apple Smart App Banner docs](https://developer.apple.com/documentation/webkit/promoting-apps-with-smart-app-banners)
- **FACT:** Universal Links need both the app’s Associated Domains entitlement and a website association file; each subdomain needs its own association. [Apple Associated Domains docs](https://developer.apple.com/documentation/xcode/supporting-associated-domains)
- **FACT:** The App Store privacy URL is required for every app; the Support URL is also required for each platform version and must lead to actual contact information. [Privacy field](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy), [Support field](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information)
- **FACT:** Account-creating apps must let users initiate account deletion inside the app. If web completion is required, link directly to that page. A support email/chat flow is not an acceptable substitute for ordinary apps. [Apple account deletion guidance](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion/)
- **FACT:** Apple’s current review rules allow external purchase calls to action without the link entitlement in U.S. storefront apps. Other storefronts have region/platform-specific restrictions and entitlements. EU alternative terms can add commissions, VAT, and tax responsibilities. [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [EU commissions and taxes](https://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/commissions-fees-and-taxes)
- **INFERENCE:** A website may describe and sell a web subscription, but do not generate an in-app link to RevenueCat Web Purchase Links globally by default. Gate app-to-web purchase links by storefront and current Apple terms.
- **FACT:** RevenueCat Web Purchase Links can host product selection and checkout using RevenueCat Billing, Stripe Billing, or Paddle Billing; customer identity and anonymous redemption have different setup requirements. [RevenueCat Web Purchase Links docs](https://www.revenuecat.com/docs/web/web-billing/web-purchase-links)

### Other useful web features

- **FACT:** Google supports `SoftwareApplication` structured data, but rich-result display is not guaranteed. App price, rating, review, and platform claims must reflect real published facts. [Google Software App structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- **INFERENCE:** Generate Open Graph and X card metadata for every public page, with a real product image and accurate title/description. No tracking pixels should be required for social previews.
- **INFERENCE:** Add i18n only when the product actually ships localized app/store content. Keep page language, store links, and pricing aligned; do not generate machine-translated legal copy.
- **INFERENCE:** Add press kit when there are real brand assets, screenshots, contact details, and approved product facts to publish.
- **INFERENCE:** Add a changelog when updates are regular enough to maintain. A stale changelog weakens trust.
- **INFERENCE:** Add a status page only when there is a hosted dependency whose availability users need to know.

## 3. Stack and hosting

### Default stack

**INFERENCE:** Plain HTML, CSS, and small progressive-enhancement JavaScript is the best default for one product landing page plus several support/legal pages. It meets the owner’s “no framework” distribution rule, avoids client-side app weight, and makes the generated output easy to inspect and edit.

- **FACT:** Astro’s default output is pre-rendered static HTML, with on-demand rendering available when needed. [Astro rendering modes](https://docs.astro.build/en/guides/on-demand-rendering/)
- **FACT:** Next.js can emit static HTML files per route and deploy them to any static web server. [Next.js static export](https://nextjs.org/docs/pages/guides/static-exports)
- **INFERENCE:** Switch to Astro or Eleventy when the site grows into multiple content templates, localization, or regularly maintained editorial content. Astro provides an easy path to static generation and optional interactive islands. Keep Eleventy as an alternative for Markdown-first publishing.
- **INFERENCE:** Use Next.js only for a real server-rendered product, authenticated web app, or web purchase/customer portal. A static marketing site does not need its runtime.
- **INFERENCE:** Framer can suit a marketing team that prioritizes visual editing and accepts a managed, proprietary workflow. It is not the factory default because the generated site should stay editable and portable as source.

### Hosting comparison

| Host | Evidence checked 2026-10-19 | Fit |
|---|---|---|
| **Cloudflare Pages** | **FACT:** Static asset requests are free and unlimited; adding Pages Functions changes the metering path. [Pages pricing](https://developers.cloudflare.com/pages/functions/pricing/) | **INFERENCE:** Recommended static host. Use a function only when form integration needs server-side secrets or validation. |
| **GitHub Pages** | **FACT:** GitHub says Pages is not for free hosting of an online business or commercial software service; it also lists soft bandwidth/build limits. [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) | **INFERENCE:** Do not default to it for client app marketing sites. |
| **Vercel** | **FACT:** The Hobby plan is for non-commercial personal use. [Vercel Hobby plan](https://vercel.com/docs/plans/hobby) | **INFERENCE:** Use a paid plan if Next.js is actually needed; not the default for static output. |
| **Netlify** | **FACT:** Free plan is $0 with a 300-credit hard monthly limit; Personal is $9/month for 1,000 credits. [Netlify pricing](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/) | **INFERENCE:** Viable when its integrated forms/deploy workflow is valuable; review usage limits before relying on it. |

## 4. Design system

**INFERENCE:** Share the product identity across app and site through semantic tokens, not by copying native screen layouts into the browser.

- Generate a small `tokens.css` from product identity: brand/accent, background, surface, text, muted text, border, focus, and status colors. Keep those roles consistent with the app’s identity recipe.
- Use a short, deliberate type scale, readable measure, and strong contrast. Start with the system font stack; include a custom font only when its web license explicitly permits embedding and redistribution. The SIL Open Font License is one permissible license family, subject to its terms. [SIL OFL](https://software.sil.org/oflt/)
- Support light and dark appearance with `prefers-color-scheme`; check increased contrast and keyboard focus. Make the brand recognizable through the icon, product imagery, composition, and one memorable visual motif.
- Keep motion purposeful: a meaningful state transition or user-started product demo. Honor `prefers-reduced-motion` by removing or replacing nonessential movement. [MDN reduced-motion guidance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion)
- Do not make glass the site’s default material. If a functional control benefits from blur, provide an opaque fallback and test on real target devices. **FACT:** `backdrop-filter` affects pixels behind a transparent element, may harm performance, and should be tested before deployment. [MDN backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter), [web.dev performance guidance](https://web.dev/articles/backdrop-filter)
- Use AVIF/WebP and responsive `srcset`; specify image dimensions to prevent layout shift. Use a poster image and user-started play for the owner’s 15-second product loop. Do not autoplay a large hero video above the fold.
- **INFERENCE from owner direction:** Dyson, Easlo, and Benji Taylor suggest a site with clear product form, purposeful material, and specific customer value. Avoid generic gradients, ornamental glass, and stock dashboard mockups. Let each app’s actual product content carry the personality.

## 5. Generator fit

**FACT — current repository:** App Workshop validates `project.json`, generates files from templates, records file hashes in `.apple-scaffold.json`, and `make update` only replaces files the builder has not edited. Generation is deterministic and does not delete files. [Architecture](../../../ARCHITECTURE.md)

**INFERENCE — recommended implementation shape:**

1. Add website fields to the validated `project.json` schema only for data the site cannot derive: domain, App Store IDs/URLs by platform, support contact, release state, email provider/form endpoint, and optional privacy-friendly analytics selection.
2. Reuse existing project name, tagline/product promise, icon, identity choice, platforms, and legal documents. Do not ask the builder to re-enter values already in config.
3. Generate a `site/` folder containing the landing page, legal/support pages, `robots.txt`, `sitemap.xml`, social metadata, icon assets, and optional AASA file. Use the same templating and manifest/hash process as current generated files.
4. Include honest release states: pre-launch CTA shows email signup; released app CTA uses the real platform store URL. Do not emit placeholder purchase URLs or fabricated customer proof.
5. Keep editable generated files under `make update` protection. Put published assets with meaningful paths and avoid renaming/moving generated paths without recording a retirement.
6. Keep form credentials out of `project.json` and generated browser code. Configure provider-hosted capture or a separately deployed endpoint through the owner’s deployment setup.

**UNKNOWN:** The current schema is strict and does not include website keys; exact implementation effort and generated-file naming should be decided against the generator’s current template sources before coding.

## 6. Acceptance checks for CI

**INFERENCE — proposed checks; not run in this read-only research task:**

- Generate a representative project twice and verify identical `site/` output. Run `make update` dry-run against an app with an edited page and confirm that edit is reported as a conflict, not overwritten.
- Run Lighthouse CI on mobile and desktop preview builds. Enforce a transfer-size and script budget, and check lab LCP/CLS regressions.
- Track field Core Web Vitals through CrUX/PSI after the site has sufficient visits. **FACT:** good field thresholds at the 75th percentile are LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1. A Lighthouse lab run does not establish those field values. [Google PSI thresholds and field-data behavior](https://developers.google.com/speed/docs/insights/v5/about)
- Run axe accessibility checks, then separately review keyboard navigation, visible focus, contrast, reduced motion, and narrow/large screens. Automated checks do not establish full accessibility.
- Validate generated HTML with the Nu HTML Checker; run a link checker over internal and external links.
- Validate JSON-LD with Google’s Rich Results Test. Do not require a rich result to appear; Google does not guarantee it. [Google structured-data guidance](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- When Universal Links are selected, parse the AASA file as JSON and verify the deployed domain serves the expected association file and matching app/team identifiers.
- Check Open Graph and X metadata, title, description, icon, and image references on every public route.
- With analytics off, fail CI if unapproved tracking scripts, pixels, or third-party beacons appear. When consent is configured for a tracking tool, verify it does not load before consent.
- For email signup, run a repeatable end-to-end submission through success, invalid input, duplicate signup, confirmation email, unsubscribe, and export. Preserve the run report as an artifact.

## Recommended default page and landing-page order

**INFERENCE — default page set:**

1. `/` — landing page
2. `/support/` — contact, FAQs, device compatibility, and recovery links
3. `/privacy/` — published privacy policy
4. `/terms/` — terms where applicable
5. `/delete-account/` — only when accounts exist and web completion is part of the deletion flow
6. `/press/`, `/changelog/`, `/status/` — optional modules when content and operations justify them

**INFERENCE — landing-page section order:**

1. Small header with wordmark and one primary action.
2. Clear one-sentence promise tied to the user’s job.
3. Product image or short, user-started demo showing a real task.
4. One primary CTA: App Store download after release, waitlist before release.
5. Three specific outcomes/features with evidence from the product.
6. Device coverage and real product screenshots.
7. Trust evidence: privacy, offline behavior, support, ratings or testimonials only when verified.
8. Pricing/subscription explanation when paid, aligned with current StoreKit products and terms.
9. Final CTA.
10. Footer with Support, Privacy, Terms, Contact, and optional Press/Changelog links.

## Ten details that separate a premium site from a template

1. **INFERENCE:** One clear customer outcome in the headline.
2. **INFERENCE:** Product imagery that shows a real task, not a decorative mockup.
3. **INFERENCE:** A specific visual motif that connects icon, site, and app.
4. **INFERENCE:** Distinctive composition instead of centered blocks repeated down the page.
5. **INFERENCE:** Typography with a small intentional scale and readable line lengths.
6. **INFERENCE:** Motion that explains a change, with a useful reduced-motion state.
7. **INFERENCE:** Exact platform and pricing choices presented without ambiguity.
8. **INFERENCE:** Real proof—named quotes, true review counts, awards, or measurable outcomes—with source and date.
9. **INFERENCE:** A working waitlist/support flow with clear success, failure, confirmation, and unsubscribe states.
10. **INFERENCE:** A fast page that remains legible, stable, and useful before its images or video load.

**Skipped/not checked:** I did not edit files, inspect rendered screenshots, run CI, or obtain site-specific PageSpeed/CrUX results. The main risks are stale vendor pricing and Apple storefront rules; recheck both before implementation or enabling web checkout.

