# Semantic design tokens

Define meanings first, then choose values for the selected identity and each appearance. Let native controls inherit system behavior where possible. Record a token only when the app needs to express the same meaning in more than one place. Prefer semantic system colors and text styles; test every custom value against content, material, and accessibility settings.

| Token | Meaning | Light | Dark | Increased contrast |
| --- | --- | --- | --- | --- |
| Accent | Primary interactive emphasis | Pending | Pending | Pending |
| Success | Completed result | Pending | Pending | Pending |
| Warning | Recoverable attention | Pending | Pending | Pending |
| Destructive | Irreversible or harmful action | Pending | Pending | Pending |
| Surface | Content background | Pending | Pending | Pending |
| Text | Primary readable content | Pending | Pending | Pending |

## Type and layout

| Role | Native starting point | App-specific decision | Compact and large-text review |
| --- | --- | --- | --- |
| Screen heading | Platform title style | Pending | Pending |
| Section heading | Semantic headline | Pending | Pending |
| Body and input | Semantic body | Pending | Pending |
| Supporting detail | Semantic secondary text | Pending | Pending |
| Data or code | Monospaced or tabular style only when meaning benefits | Pending | Pending |

Define a spacing rhythm for **within a control**, **between related controls**, **between sections**, and **page edges**. Review it on each selected device and window size; do not force identical pixel values across platforms. Record corner and stroke choices only for custom content surfaces. Leave system bars, focus, menus, and controls free to adapt to the OS.

## Motion and feedback

| Event | Purpose and end state | Motion or haptic | Reduce Motion / quiet alternative |
| --- | --- | --- | --- |
| Navigation | Preserve orientation | Pending | Pending |
| Work in progress | Show that an action started and can finish or fail | Pending | Pending |
| Completion | Show the resulting content or saved state | Pending | Pending |
| Attention | Identify an actionable problem without looping distraction | Pending | Pending |

Review the assembled screen, not just token swatches. Record evidence in `docs/design/NATIVE-REVIEW.md` for light/dark, increased contrast, reduced transparency, large text, and the selected platform inputs.
