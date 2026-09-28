# Commerce module

Use when a defined product has a paid value proposition. Decide whether the value is one-time or continuing before selecting purchase products. Keep price, trial, renewal, and access copy aligned with the configured StoreKit products and current App Review rules.

Before implementation, specify product IDs, what each purchase grants, purchase and restore entry points, entitlement ownership, offline behavior, refunds, billing issues, family sharing if offered, cancellation guidance, and support. Test interrupted purchase, already-owned product, expired entitlement, device change, and restore. A successful payment must lead to the promised access; failure must preserve the user's work.

Source checked 2026-09-25: [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase), [choosing a StoreKit API](https://developer.apple.com/documentation/storekit/choosing-a-storekit-api-for-in-app-purchases).

## Before the first subscription

The Account Holder must agree to the latest Paid Apps Agreement before creating an IAP; the agreement must be **Active** to submit one. Complete tax and banking setup early. Enable the In-App Purchase capability for the app ID and target. Submit the first auto-renewable subscription with a new app version, including review screenshot, localized product and group details, price, and reviewer path. See [agreements](https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements), [first IAP submission](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-purchase), and [capabilities](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app) (checked 2026-09-27).

Decide Family Sharing before enabling it: the setting cannot be undone. [Subscriptions](https://developer.apple.com/app-store/subscriptions/) (checked 2026-09-27).

The paywall and store metadata must plainly show the subscription title, duration, price and price per unit where relevant, what a trial becomes, and working Terms of Use and Privacy Policy links. Provide a working restore path and cancellation guidance. Do not call a trial free without showing the later charge. Compare the rendered paywall with the actual StoreKit product. [App Review Guidelines §3.1.2](https://developer.apple.com/app-store/review/guidelines/) (checked 2026-09-27).

## Entitlement failure policy

Specify a bounded offline grace window (for example, three days) from the last **verified** active entitlement; persist signed transaction evidence and its trusted date, not a bare Boolean. A network error within that window may preserve already granted local access. Deny an unverified transaction, a refund or revocation, and access after the window ends; moving the device clock backward never extends access. Honor Apple's configured billing grace period while a verified subscription is in grace. Server-funded or per-use costs require a fresh server-side entitlement decision and fail closed when it cannot be verified. Keep user data readable and exportable after access lapses. These are **factory policy choices**, not Apple guarantees. [Current entitlements](https://developer.apple.com/documentation/storekit/transaction/currententitlements), [subscriptions and grace periods](https://developer.apple.com/app-store/subscriptions/) (checked 2026-09-27).

Confirm exact `SKTestSession` API methods against the selected SDK before implementing the scenarios; real storefront and family approval require separate checks.

Run deterministic local StoreKit tests with `SKTestSession`: first purchase; already-owned purchase; Ask to Buy pending then approved/denied; interrupted and failed purchase; app restart and transaction update; explicit restore; trial to first charge to renewal; grace period, billing retry, expiration, refund/revocation; offline within and beyond the chosen grace window; clock rollback; upgrade/downgrade; and server-cost denial when verification is unavailable. Then test App Store Connect configuration and a second-device restore in sandbox, and the release flow in TestFlight. [Testing with Xcode and sandbox](https://developer.apple.com/documentation/storekit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox), [sandbox settings](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings/) (checked 2026-09-27).

## Build vs. buy

| Option | Choose when | Cost and responsibility |
| --- | --- | --- |
| StoreKit 2 (default) | One Apple-only entitlement model; no remote paywall or cross-store state needed. | No vendor fee; own entitlement policy, tests, and any server notifications. |
| RevenueCat `purchases-ios` | A named need for cross-store entitlements, remote paywalls, or managed subscription operations justifies the SDK. | Vendor data processing and exit plan; pricing is free to $2,500 monthly tracked revenue, then 1% on Pro as checked 2026-09-27. Verify current terms before adopting. |

[StoreKit](https://developer.apple.com/documentation/storekit), [RevenueCat pricing](https://www.revenuecat.com/pricing/) (checked 2026-09-27). Keep any RevenueCat `sk_` secret on a server; a public `appl_` SDK key is a different credential.
