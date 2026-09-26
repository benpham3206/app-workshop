# Native experience review

Use this review once a real product and runnable interface exist. A polished scaffold is a starting point; screenshots, interaction recordings, builds, and device observations support quality claims. Record results in `docs/quality/evidence/` and link them from the table below. Keep failed or unavailable checks visible.

Review one complete user job on every selected platform: arrival, first useful result, repeat use, interruption, recovery, and return. Capture the same job in each relevant appearance and input method. Check a compact and a spacious layout, large text, long localized text, VoiceOver or the platform's assistive input, increased contrast, reduced transparency, and Reduce Motion. For performance claims, use representative physical hardware and the same journey and data before and after a change.

## Review record

For every row, record **Pass**, **Needs work**, **Not applicable**, or **Pending**. A pass needs a path to a screenshot, recording, test, or measured observation. Name the build, device, OS, appearance, input, date, and reviewer in that evidence. A source link explains an expectation; it does not prove the app meets it.

| Area | What to inspect | Result | Evidence or issue |
| --- | --- | --- | --- |
| Purpose | The primary action and first useful result are clear without an explanation from the builder. | Pending | |
| Information hierarchy | The important content, next action, and current state remain clear at each size. | Pending | |
| Native navigation | Window, sidebar, tab, back, toolbar, menu, and focus behavior fit each selected platform. | Pending | |
| Controls | Buttons, menus, destructive actions, disabled states, keyboard and pointer paths have expected feedback. | Pending | |
| Materials | System Liquid Glass supports navigation and controls; content remains legible over changing backgrounds. | Pending | |
| Type and layout | Semantic text styles, alignment, spacing, safe areas, long text, and Dynamic Type or platform equivalents work. | Pending | |
| Identity | Accent, imagery, motion, haptics, and copy form a consistent selected recipe without obscuring status. | Pending | |
| Icon | The built icon has a clear small silhouette and is checked in its real platform context and appearances. | Pending | |
| States | Empty, loading, success, error, offline, denied permission, and interrupted flows say what happened and what to do. | Pending | |
| Accessibility | Assistive input, labels, focus order, contrast, reduced motion, and reduced transparency preserve the job. | Pending | |
| Localization | Text expansion, pluralization, date/number formats, and supported reading directions keep meaning and layout. | Pending | |
| Performance | Launch, main-action response, scrolling, memory, and energy fit the chosen hardware support promise. | Pending | |
| Privacy | Permission timing, visible data, sharing, deletion, and store claims agree with actual behavior. | Pending | |

## Evidence capture

1. Record the product promise, selected platform, minimum OS, build identifier, and primary user job in the product brief and quality matrix.
2. Use Xcode previews to iterate on sizes, states, appearances, and text. Inspect the runnable build in Simulator. Test hardware-dependent behavior and performance on physical devices.
3. Put captures under `docs/quality/evidence/` with names that identify platform, device, state, and appearance. Record defects beside the relevant row and link the fixing task.
4. Re-run affected rows after a design, navigation, component, or platform change. Keep a row pending if its evidence is unavailable.

Stop the release review when the core job is unreachable, a supported size clips essential content, an essential control lacks an accessible path, recovery loses user work, or measured performance contradicts the supported-device promise. Triage the defect, then repeat the affected journey.

## Apple references

Primary sources checked 2026-09-25. Recheck them against the SDK and OS used for the actual app.

- [Human Interface Guidelines: Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
- [Human Interface Guidelines: Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Human Interface Guidelines: Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [Human Interface Guidelines: Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [Human Interface Guidelines: Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
- [Human Interface Guidelines: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)
- [Xcode previews](https://developer.apple.com/documentation/xcode/adding-previews-to-your-interface-files)
- [Run on Simulator or devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices)
