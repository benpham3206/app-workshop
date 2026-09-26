# App Intents module

Use when a real app action or piece of content should be reachable through system experiences such as Shortcuts, Siri, Spotlight, or interactive widgets. Define the same user-visible meaning and result as the in-app action; avoid a second implementation with different rules.

Before implementation, specify the intent's inputs, entity identity, confirmation, authentication, privacy, error and cancellation behavior, and what happens when the app is not foregrounded. Check which selected platforms and OS versions support the chosen intent surface. Test missing or stale entities, ambiguous input, denied access, and a repeated invocation. The action should return a useful result or a clear recovery path.

Source checked 2026-09-25: [App Intents overview](https://developer.apple.com/documentation/appintents), [getting started](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework).
