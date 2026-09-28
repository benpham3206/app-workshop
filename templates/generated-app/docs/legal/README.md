# Public pages before submission

Apple requires public web pages before an app can be submitted: a privacy policy URL and a support URL for every app, plus a Terms of Use link for an app that sells auto-renewable subscriptions. The drafts here give a first-timer a starting point. They are not legal advice; have each one reviewed before publishing.

| Page | Draft | Needed for |
| --- | --- | --- |
| Privacy policy | [`PRIVACY-POLICY.md`](PRIVACY-POLICY.md) | Every app: App Store Connect metadata and inside the app ([Guideline 5.1.1(i)](https://developer.apple.com/app-store/review/guidelines/), checked 2026-09-27) |
| Support | [`SUPPORT-PAGE.md`](SUPPORT-PAGE.md) | Every app: support URL in App Store Connect |
| Terms of Use | [`TERMS-OF-USE.md`](TERMS-OF-USE.md) | Subscription apps, unless you use Apple's standard EULA |

## Steps

1. Fill `docs/privacy/PLAN.md` first. The privacy policy and the App Store privacy label must both say what that plan says.
2. Fill each draft, delete every `[bracket]` prompt that does not apply, and have it reviewed.
3. Publish each page at its own public HTTPS URL that opens without login, a cookie wall, or an app install. A static site or GitHub Pages works. Publish the finished text, not the draft banner or the placeholders.
4. Choose stable URLs that do not change per app version, and enter them in App Store Connect and inside the app. Open each one in a private window on a phone before submitting.
5. Record the URLs in `docs/release/STORE-PAGE.md`.

## Keep the pages alive

- The pages must stay reachable for as long as the app is listed. An expired domain breaks the listing links, lets someone else publish text under your privacy policy URL, and loses any support mailbox on that domain.
- Record the domain or host owner and its renewal date in the release checklist; turn on auto-renew.
- Do not use the same domain for your Apple Account email unless you protect it: whoever controls an expired domain could receive that mail.
- Change the policy, the privacy label, and `docs/privacy/PLAN.md` together when you add an SDK, an AI service, or a new kind of data.
- A subscription app links Terms of Use and the privacy policy both in the purchase flow and in the store metadata; see `TERMS-OF-USE.md`.
