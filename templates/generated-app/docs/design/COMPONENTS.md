# Component inventory

Start with system controls. Add a reusable custom component only when the same product need appears more than once or a system control cannot express it.

| Component or pattern | User intent | Native base | States to preview | Platform differences |
| --- | --- | --- | --- | --- |
| Primary action | Pending | `Button` | Ready, working, disabled, error | Pending |
| Choice | Pending | `Picker` or `Menu` | Selected, unavailable | Pending |
| On/off preference | Pending | `Toggle` | On, off, disabled | Pending |
| Navigation | Pending | Native navigation API | Current, back, deep link | Pending |
| Collection row | Pending | `List` and native row content | Empty, selected, loading, error | Pending |
| Data entry | Pending | `TextField`, `SecureField`, or platform input | Blank, invalid, working, saved | Pending |
| Completion or status | Pending | `ProgressView` or readable status text | Working, complete, failed | Pending |
| Confirmation | Pending | Native alert, confirmation dialog, or undo | Cancel, confirm, recovery | Pending |
| Empty result | Pending | Native unavailable-content pattern or clear message | First use, filtered empty, unavailable | Pending |

Record labels, VoiceOver output, large-text behavior, and interactions alongside appearance. Avoid building a visual component library before a real app exposes its repeated needs.

For each custom component, write its **user intent, state owner, input paths, accessibility contract, layout range, performance cost, and evidence**. Link the action contract and preview fixtures. A visually shared component can vary its navigation, focus, menu, and sizing by platform.

For each control, note whether system Liquid Glass already covers it. Reserve custom glass for an actual control in the functional layer; identify its supported OS versions, fallback, reduced-transparency appearance, and performance impact. Keep content cards and reading surfaces clear.
