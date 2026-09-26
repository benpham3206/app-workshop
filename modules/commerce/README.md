# Commerce module

Use when a defined product has a paid value proposition. Decide whether the value is one-time or continuing before selecting purchase products. Keep price, trial, renewal, and access copy aligned with the configured StoreKit products and current App Review rules.

Before implementation, specify product IDs, what each purchase grants, purchase and restore entry points, entitlement ownership, offline behavior, refunds, billing issues, family sharing if offered, cancellation guidance, and support. Test interrupted purchase, already-owned product, expired entitlement, device change, and restore. A successful payment must lead to the promised access; failure must preserve the user's work.

Source checked 2026-09-25: [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase), [choosing a StoreKit API](https://developer.apple.com/documentation/storekit/choosing-a-storekit-api-for-in-app-purchases).
