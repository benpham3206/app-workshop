# Sync module

Use when the same user data must stay useful on more than one device. Define the local source of truth, what syncs, what stays private to a device, and what a person should see while offline. Evaluate iCloud's storage options against the actual data shape before choosing CloudKit.

Before implementation, specify stable record identity, conflict resolution, deletion and tombstones, initial download, migrations, account unavailable or changed, retries, and export/recovery. Test two devices editing the same item, an offline edit followed by reconnect, a deleted item reappearing, and an old app version. A sync indicator should describe real state rather than claim instant consistency.

Source checked 2026-09-25: [CloudKit](https://developer.apple.com/documentation/cloudkit), [deciding whether CloudKit fits](https://developer.apple.com/documentation/cloudkit/deciding-whether-cloudkit-is-right-for-your-app).

## Build vs. buy

| Option | Choose when | Tradeoff |
| --- | --- | --- |
| SwiftData and CloudKit (default) | The data belongs to a person's Apple devices and iCloud fits its shape. | No sync vendor; test conflicts, offline use, and account changes. |
| Supabase | A named need for a relational backend shared with web or Android. | Own schema, access rules, and hosted data; verify current price, license, privacy declarations, and export before adopting. |
| Firebase | A named need for its document model or existing Firebase operations. | A different data model and service dependency; verify current price, license, privacy declarations, and migration path before adopting. |

Apple source: [CloudKit](https://developer.apple.com/documentation/cloudkit) (checked 2026-09-27).
