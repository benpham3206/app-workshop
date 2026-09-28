# Agent navigation: {{PROJECT_NAME}}

This map is for work on this **app**. Read [AGENTS.md](../../AGENTS.md), [PRINCIPLES.md](../../PRINCIPLES.md), [README.md](../../README.md), the [product brief](../product/BRIEF.md), and the assigned [task packet](TASK-PACKET.md). The selected configuration is recorded in `.apple-scaffold.json`. A generated plan is a starting point; check what the app actually implements before describing behavior as working.

## Selected scope

Identity: [{{IDENTITY}}](../../design/identity/RECIPE.md).

Platform profiles:
{{SELECTED_PLATFORM_FILES}}

Optional module contracts:
{{SELECTED_MODULE_FILES}}

Compatibility routes:
{{SELECTED_COMPATIBILITY_FILES}}

Only these selected profiles and contracts are present. If an agent needs another platform or capability, it must first explain the user job, compatibility, privacy, maintenance cost, and needed configuration change. Do not infer a future device from the current selection.

## Find the owning file

| If the task is about… | Open first | Then inspect |
| --- | --- | --- |
| Why the app exists, who returns, or what they pay for | `docs/product/BRIEF.md`, `docs/operations/MEASUREMENT.md` | `docs/BEGINNER-GUIDE.md`, `docs/operations/WORKBOARD.md` |
| A journey, control, menu, or state | `docs/ux/FLOWS.md`, `docs/ux/STATES.md`, `docs/ux/interactions/`, applicable `docs/ux/patterns/` | `docs/design/COMPONENTS.md`, selected platform profiles, quality matrix |
| Color, type, motion, layout, or icon | `docs/design/IDENTITY.md`, `design/identity/RECIPE.md`, `docs/design/APP-ICON.md` | `docs/design/NATIVE-REVIEW.md`, `docs/design/TOKENS.md`, `design/assets/`, appearance and accessibility states |
| Liquid Glass or speed on supported devices | `docs/quality/GLASS-AND-PERFORMANCE.md` | `docs/design/COMPONENTS.md`, selected platform profiles, `docs/quality/TEST-MATRIX.md`, actual device captures |
| App code or stored data | `docs/engineering/ARCHITECTURE.md`, `docs/engineering/SECURE-FAST-DEFAULTS.md`, `docs/engineering/PROJECT-SETUP.md`, `App/` if it exists | module contracts, privacy plan, test matrix, troubleshooting |
| A system surface or permission | selected `platforms/` and `modules/` paths above | `docs/privacy/PLAN.md`, `docs/TROUBLESHOOTING.md`, release checklist |
| Who may do what, or a review | `docs/agents/TASK-PACKET.md` (roles, allowed capabilities) | `AGENTS.md` operating loop, `.github/pull_request_template.md` |
| A build or behavior failure | `docs/TROUBLESHOOTING.md`, `docs/quality/TEST-MATRIX.md` | code or contract that owns the failing behavior |
| Shipping, support, or claims | `docs/release/`, `docs/privacy/PLAN.md`, `docs/legal/`, `docs/operations/SUPPORT.md` | product brief, actual build/device evidence, current Apple rules |
| An OS, SDK, or device change | `docs/compatibility/REVIEW.md`, selected platform profiles | `docs/design/NATIVE-REVIEW.md`, test matrix, release checklist |

Use `rg --files docs design platforms` to locate the core files; add `modules` and `App` to a search only when those directories exist. Use `rg -n 'term' docs design platforms` to trace references, adding the same optional directories as needed. Do not copy the factory's `config/` or `tooling/` paths into this app: those live upstream in the boilerplate.

## Work within a lane

| Lane | Normal write scope | Coordinate when |
| --- | --- | --- |
| Product | `docs/product/`, `docs/operations/MEASUREMENT.md` | A promise changes a flow, metric, paywall, or listing claim. |
| Experience and identity | `docs/ux/`, `docs/design/`, `design/` | A control needs code, data, a permission, or platform-specific behavior. |
| Engineering | `App/`, `docs/engineering/` | An interface, persistence rule, module contract, or entitlement changes. |
| Platform surfaces | `platforms/`, `modules/` | The selection, availability, privacy, or extension behavior changes. |
| Quality | `docs/quality/`, `docs/TROUBLESHOOTING.md`, tests when present | A failure needs a fix in its owning lane. |
| Release and support | `docs/release/`, `docs/privacy/`, `docs/legal/`, `docs/operations/SUPPORT.md` | An external claim or support flow needs product or engineering evidence. |

The task packet's `May edit` field narrows these defaults. Read across lanes as needed; describe a needed cross-lane edit before making it when another agent owns the file. Avoid two agents editing the same source concurrently. Keep app-specific changes here and reusable factory improvements upstream.

## Think ahead before marking done

Trace **entry → action → state change → visible result → recovery → return** for the affected user job. Check the credible second-order effects:

- Action change: toolbar, menu bar, keyboard, gesture, widget, intent, notification, deep link, VoiceOver, and undo where they actually exist.
- Data change: ownership, old data, sync conflict, offline state, export, deletion, migration, and restoration.
- Visual change: system glass versus content, earlier-OS fallback, light/dark, contrast, reduced transparency, large text, localization, small icon size, motion preference, and performance on representative devices.
- Capability change: OS/API availability, entitlement, permission denial, privacy disclosure, background limits, battery, and support.
- Payment or release change: current App Review rules, truthful copy, restore/cancel paths, test accounts, and support response.

Choose relevant cases, verify them at the right level, and write remaining risks in the completion note. A document is evidence of a decision; a build, preview, Simulator run, and physical-device check prove different things. Use `docs/agents/TASK-PACKET.md` for assignment and handoff.
