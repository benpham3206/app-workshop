# Interaction system

This is where behavior lives. A flow describes **why and when** someone acts; an interaction contract describes **what happens** when they act; `design/` defines the visual expression; `platforms/` records how that interaction appears on each device. Start with native SwiftUI controls and document exceptions.

| Layer | Question | In a generated project |
| --- | --- | --- |
| Flow | What job is the person completing? | `docs/ux/FLOWS.md` |
| Action | What does a tap, click, key, voice command, or remote press do? | `docs/ux/interactions/` |
| State | What appears before, during, after, and on failure? | `docs/ux/STATES.md` |
| Appearance | What can the brand change? | `docs/design/IDENTITY.md`, `TOKENS.md`, and `COMPONENTS.md` |
| Platform | Where does the action live and which input is primary? | `platforms/*/PROFILE.md` |

## Define one action once

For each important action, record: user intent; label; entry points; prerequisites; result; loading and failure states; undo or recovery; destructive confirmation; keyboard/voice/accessibility equivalent; analytics event if justified. The same action may be exposed by an iPhone toolbar button, a Mac menu command, a Watch control, and an App Intent. Its meaning should stay consistent even when the surface changes.

Use `ACTION-CONTRACT.md` as the fill-in example. The other guides cover [buttons](BUTTONS.md), [menus and menu bars](MENUS.md), [input and gestures](INPUT.md), and [state-driven rendering](RENDERING.md). In a generated project, the app icon process is in `docs/design/APP-ICON.md`.

## Learning loop

1. Sketch a three-step flow with one useful result.
2. List each action and fill an action contract before styling it.
3. Build the flow with system controls; preview every state.
4. Try it with touch, keyboard or pointer where supported, VoiceOver, larger text, and a failure case.
5. Add identity styling only after the behavior is clear, then test again.

Apple references: [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), [SwiftUI controls and indicators](https://developer.apple.com/documentation/swiftui/controls-and-indicators), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures/). Reviewed 2026-09-25.
