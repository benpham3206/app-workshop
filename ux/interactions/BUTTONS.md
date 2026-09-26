# Buttons and action feedback

Use a system `Button` for an action. Give it a verb or a clear noun-verb label. Use `Toggle` for an on/off state and a `Menu` when activation reveals a choice. A `NavigationLink` expresses navigation. Keep these meanings distinct even if they share a visual style.

| Decision | Default behavior |
| --- | --- |
| Primary action | One clear action in the relevant context; place it where the platform expects it. |
| Label | Say what will happen; pair a symbol with text when space allows. Give icon-only controls an accessibility label. |
| Activation | Run once per deliberate activation. Guard duplicate async requests in action state, not only by visual styling. |
| Waiting | Show immediate feedback, then progress if work is perceptible. Keep cancellation where meaningful. |
| Success | Show the resulting content or a concise confirmation; avoid a toast that replaces the result. |
| Failure | Preserve input, explain the failure in plain language, and give a retry or recovery route. |
| Destructive action | Use the destructive role, explicit action wording, and confirmation or undo appropriate to the loss. |
| Disabled state | Use only for a real prerequisite; explain how to become eligible nearby. |

The system owns pressed, hover, focus, VoiceOver, and platform adaptations when you use native controls. A brand may change tint, emphasis, shape, supporting motion, and copy within legibility and platform expectations. Custom controls must recreate the missing behavior and be tested across input modes; use them only for a clear product need.

**Implementation starting point:** SwiftUI `Button` with a label and action; `buttonStyle` for visual treatment; `role: .destructive` where appropriate. Keep the action implementation separate from its visual button so menus, keyboard shortcuts, widgets, and App Intents can invoke the same intent consistently.

Apple references: [Buttons HIG](https://developer.apple.com/design/human-interface-guidelines/buttons), [SwiftUI Button](https://developer.apple.com/documentation/swiftui/button), [SwiftUI Toggle](https://developer.apple.com/documentation/swiftui/toggle). Reviewed 2026-09-25.
