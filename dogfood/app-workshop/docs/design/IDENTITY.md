# Identity decision

Selected starting recipe: **playful-kinetic**.

Use the selected recipe under `design/identity/` as a starting point. Define this app's own name, icon concept, accent, imagery, copy voice, semantic color variants, type hierarchy, motion, haptics, and accessibility alternatives. Record reusable values in `TOKENS.md` and UI patterns in `COMPONENTS.md`. Keep native controls and navigation recognizable.

Liquid Glass is the system layer for navigation and controls on supported OS versions. Record which standard controls provide it, whether any custom glass control has a real purpose, and what earlier OS versions show instead. Keep the content layer readable. Preview changing content behind glass, light/dark, increased contrast, reduced transparency, and Reduce Motion. Follow `docs/quality/GLASS-AND-PERFORMANCE.md`.

## Decisions

| Element | Decision | Evidence or preview |
| --- | --- | --- |
| Name and promise | App Workshop guides a first-time builder through 13 phases. | `docs/product/BRIEF.md`, `resources/process.json` |
| Icon | Three connected geometric pieces convey a path through phases. Rough images, circle construction, vector source, and a local Mac icon exist. | `design/assets/icons/README.md`, `design/assets/icons/` |
| Accent and semantic colors | Use the system accent for selection and the native green completion symbol. Avoid custom colors on core controls. | `App/Sources/AppWorkshop.swift`; contrast review Pending |
| Typography | Use system large title, title, headline, body, and caption styles with secondary emphasis for descriptions. | `App/Sources/AppWorkshop.swift`; large text review Pending |
| Motion and Reduce Motion | Native list selection and progress change only; no custom animation. | Reduce Motion review Pending |
| System glass and fallback | Native sidebar, list, toolbar behavior, buttons, and menus; content cards use a quiet quaternary background. macOS 14 fallback retains the standard toolbar. | `App/Sources/AppWorkshop.swift`; appearance review Pending |
| Representative device appearances | Dark appearance on one arm64 Mac was inspected. | `docs/quality/SELF-TEST.md`; other appearances and hardware Pending |
| Voice | Direct instructions, explicit outputs, and recovery guidance from the process data. | `resources/process.json` |
