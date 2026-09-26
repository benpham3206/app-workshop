# Input and gestures

Design the action first, then expose it through the input each platform supports. System controls handle many gestures, pointer interactions, keyboard focus, and accessibility behaviors for you.

| Platform | Primary inputs to check | Common failure |
| --- | --- | --- |
| iPhone | Touch, VoiceOver, hardware keyboard where present | Essential action exists only behind an undiscoverable gesture. |
| iPad | Touch, pointer, keyboard, Pencil where relevant | Hover or shortcut differs from touch result. |
| Mac | Pointer, keyboard, VoiceOver | A command works only in one window or has no shortcut where expected. |
| Watch | Touch, Digital Crown, accessibility input | Tiny target or long interaction for a glanceable job. |
| Apple TV | Remote focus and select, accessibility input | Focus cannot reach or leave a control. |
| Vision Pro | Look and pinch, direct input where appropriate | Target is difficult to acquire or physically uncomfortable. |

Use standard tap, swipe, scroll, and drag meanings. If a custom gesture is essential, provide a visible or accessible alternative. Keep hit areas generous and test the actual device input where behavior depends on hardware. Do not use gesture recognition to change a standard control's expected action without a clear reason.

Apple references: [Gestures HIG](https://developer.apple.com/design/human-interface-guidelines/gestures/), [Accessibility HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility), [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection). Reviewed 2026-09-25.
