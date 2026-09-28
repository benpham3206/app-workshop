# Measurement plan

Instrument questions, not every tap. Collect only data needed to answer a specific product or reliability question, with a documented privacy basis and user controls.

| Question | Metric and exact definition | Data source | Review cadence | Decision it informs |
| --- | --- | --- | --- | --- |
| Does the first session deliver value? | First useful result / eligible first launches | Pending | Weekly | Onboarding and core flow |
| Do people return for the job? | Repeat task completions by cohort | Pending | Monthly | Product value |
| Is the app reliable? | Crash and critical failure rate | Pending | Each release | Fix priority |
| Is support sustainable? | Repeated issue count and resolution time | Pending | Weekly | Reliability and help UX |
| Is payment justified? | Trial starts, first paid transactions, first renewals, refunds, and support load if paid; define denominators by cohort | Pending | Monthly | Offer and pricing |

Before release, specify event names, consent and privacy handling, retention, and a way to validate that events fire once and mean what their names claim. Do not add an analytics SDK solely because a template lists metrics.

For subscriptions, count a first renewal only after the second successful paid transaction in the same subscription lineage, not when a trial converts to its first charge. Reconcile that definition against verified StoreKit transactions or App Store Server Notifications V2 `DID_RENEW`; an introductory trial can also emit renewal events when it first becomes paid. Keep subscription events idempotent and do not infer a renewal from an install or paywall view. [App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications), [subscription event reference](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype) (checked 2026-09-27).

For subscriptions, register each planned price change and its effective storefront date before scheduling it: a price decrease lowers existing renewals and cannot preserve the old higher price; only one future change per territory can be scheduled. Source checked 2026-09-27: [Apple subscription pricing](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions/).
