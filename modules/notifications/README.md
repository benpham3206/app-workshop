# Notifications module

Use when an event is valuable enough to interrupt the person. State the event, why now matters, and what tapping the notification opens. Keep the app useful when notification permission is denied or later revoked.

Before implementation, specify local or remote delivery, permission timing, categories and actions, quiet or summary behavior, privacy-safe text, deep link target, stale-event handling, and opt-out controls. Check current authorization before scheduling. Test denial, changed settings, duplicate delivery, an expired event, and a tap after the underlying item was deleted.

Source checked 2026-09-25: [User Notifications](https://developer.apple.com/documentation/usernotifications), [asking permission](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications).

## Build vs. buy

| Option | Choose when | Tradeoff |
| --- | --- | --- |
| UserNotifications and direct APNs (default) | A local notification or focused remote event serves the job. | No campaign vendor; a remote push still needs an APNs provider. |
| OneSignal | A named need for campaign segmentation or multiple messaging channels. | Shares tokens and event data with a vendor; price, binary license, privacy manifest, and exit path are unverified here—verify before adopting. |

Apple source: [User Notifications](https://developer.apple.com/documentation/usernotifications) (checked 2026-09-27).
