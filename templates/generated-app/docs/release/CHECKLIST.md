# Release checklist

Complete this for the actual app and supported regions. Treat unchecked items as decisions to make, not claims of compliance.

- [ ] Build and run on every selected platform and relevant physical hardware.
- [ ] Check accessibility, localization, appearance, and Reduce Motion.
- [ ] Complete `docs/design/NATIVE-REVIEW.md` with build and device evidence; resolve all core-job blockers.
- [ ] Review permissions, privacy manifest, App Store privacy details, and third-party SDKs.
- [ ] Verify purchase and restore flows if commerce is selected.
- [ ] If selling IAP, confirm the Paid Apps Agreement is Active, tax and banking are complete, and the first IAP of each type is submitted with a new app version. [Agreements](https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements), [first IAP](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-purchase) (checked 2026-09-27).
- [ ] Record the owner and renewal or expiry date for Developer Program membership, the paid agreement, payment card, bank/tax status, signing certificates, and any account-linked domain; review before each release. [Program renewal](https://developer.apple.com/help/account/membership/renewal/), [agreement states](https://developer.apple.com/help/app-store-connect/manage-agreements/view-agreements-status), [certificates](https://developer.apple.com/support/certificates/) (checked 2026-09-27).
- [ ] If selling subscriptions, compare the visible title, duration, price, trial conversion, Terms of Use, Privacy Policy, and restore path with the configured product and store metadata. [App Review Guidelines §3.1.2](https://developer.apple.com/app-store/review/guidelines/) (checked 2026-09-27).
- [ ] Review every planned subscription price change: a decrease also lowers existing subscribers' renewal price and cannot preserve their higher price. [Subscription pricing](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions/) (checked 2026-09-27).
- [ ] Verify account deletion if the app creates accounts.
- [ ] Prepare truthful metadata, screenshots, support and privacy URLs, and reviewer access.
- [ ] Determine encryption export requirements and any category-specific rules.
- [ ] Test a final build with appropriate beta distribution before submission.
- [ ] Archive for App Store submission with an eligible release or RC Xcode/SDK, not a beta build; beta builds may be eligible for internal and external TestFlight. Meet the current SDK floor. [App Store Connect release notes](https://developer.apple.com/help/app-store-connect/release-notes/), [submitting](https://developer.apple.com/app-store/submitting/) (checked 2026-09-27).
- [ ] Answer the current age rating questions in App Store Connect.
- [ ] For selected regions, verify EU DSA trader status and whether a release is a significant change under Apple's Texas age-assurance guidance; use the relevant age APIs and consent-revocation handling if applicable. [EU trader status](https://developer.apple.com/news/?id=einwn76m), [Texas update](https://developer.apple.com/news/?id=sg176nne) (checked 2026-09-27).
- [ ] If personal data is shared with third-party AI, disclose where it goes and get explicit permission first. [App Review Guidelines §5.1.2(i)](https://developer.apple.com/app-store/review/guidelines/) (checked 2026-09-27).
- [ ] Declare Accessibility Nutrition Labels only for features that pass Apple's evaluation criteria.
- [ ] Plan for no rollback: the previous version can read data this version writes, phased release is on, and a fix-forward build path is ready.
- [ ] Resolve the current OS and device decisions in `docs/compatibility/REVIEW.md`; align the support claim with tested evidence.
- [ ] If distributing a Mac app directly, verify Developer ID signing, hardened runtime, notarization, packaging, update delivery, and support for that route.
- [ ] Confirm support contact, issue triage, crash monitoring, and a way to ship fixes after launch.
