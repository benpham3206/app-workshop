# Notifications module

Use when an event is valuable enough to interrupt the person. State the event, why now matters, and what tapping the notification opens. Keep the app useful when notification permission is denied or later revoked.

Before implementation, specify local or remote delivery, permission timing, categories and actions, quiet or summary behavior, privacy-safe text, deep link target, stale-event handling, and opt-out controls. Check current authorization before scheduling. Test denial, changed settings, duplicate delivery, an expired event, and a tap after the underlying item was deleted.

Source checked 2026-09-25: [User Notifications](https://developer.apple.com/documentation/usernotifications), [asking permission](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications).
