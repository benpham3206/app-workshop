# Sync module

Use when the same user data must stay useful on more than one device. Define the local source of truth, what syncs, what stays private to a device, and what a person should see while offline. Evaluate iCloud's storage options against the actual data shape before choosing CloudKit.

Before implementation, specify stable record identity, conflict resolution, deletion and tombstones, initial download, migrations, account unavailable or changed, retries, and export/recovery. Test two devices editing the same item, an offline edit followed by reconnect, a deleted item reappearing, and an old app version. A sync indicator should describe real state rather than claim instant consistency.

Source checked 2026-09-25: [CloudKit](https://developer.apple.com/documentation/cloudkit), [deciding whether CloudKit fits](https://developer.apple.com/documentation/cloudkit/deciding-whether-cloudkit-is-right-for-your-app).
