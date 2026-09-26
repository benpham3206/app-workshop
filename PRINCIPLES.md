# What good work means here

This is a standard for decisions, implementation, and review. It applies to the boilerplate and to every app generated from it. The words below describe observable work, not praise.

## Four levels

| Level | What it means | Evidence |
| --- | --- | --- |
| **Great — baseline** | The product solves a real job clearly and reliably. A new person can reach the promised result, understand controls, and recover from ordinary failures. | A working first-use journey; native and accessible controls; honest copy; focused tests and device evidence. |
| **Outstanding — baseline** | The whole journey feels coherent. Details hold under changing data, device sizes, input methods, appearances, permissions, and network conditions. The app respects time, attention, battery, privacy, and trust. | Reviewed empty, loading, error, offline, and return states; useful feedback; performance and accessibility checks; fewer unexplained decisions. |
| **Exceptional — working method** | The team sees second-order effects early and removes friction before it spreads. Architecture keeps common meaning shared and platform behavior native. Failures are diagnosable and fixes strengthen the system. | Explicit assumptions and tradeoffs; narrow interfaces; migration and rollback plans where needed; clear diagnostics; repeated issues converted into tests or design changes. |
| **Timeless — goal** | The product remains understandable and useful beyond a current visual trend, device shape, or SDK release. Its purpose, data, and interactions can evolve without betraying users or requiring a rewrite for every change. | A durable user job; semantic design; portable or recoverable user data; documented decisions; regular compatibility review; maintained trust. |

Great and outstanding are release expectations. Exceptional is how we work toward them. Timeless is a direction that must be earned over years; a first release cannot declare itself timeless.

## Engineering habits

1. **Start with the user outcome.** State what a person will be able to do, then trace each proposed feature back to it. Remove work that only makes the architecture look impressive.
2. **Think one step beyond success.** For each important action, ask what happens with no data, duplicate input, interruption, denial, partial completion, stale information, and a return weeks later. Add the cases that are credible for this product.
3. **Preserve the platform contract.** Use native behavior first. If changing a familiar control or gesture, write down the gained value and test every input and accessibility path it replaces.
4. **Make state and ownership explicit.** Know which component owns data, what persists, what syncs, what can be deleted, and what happens when two devices disagree.
5. **Keep changes small and inspectable.** Prefer one complete vertical slice over many partial features. Give shared code an owner and a clear boundary; do not extract it just because it might be reused.
6. **Use evidence proportional to risk.** Test rules that can break, preview states that can look wrong, and use physical devices for hardware-dependent behavior. Report exactly what was checked.
7. **Design for repair.** Errors should preserve work, explain the next action, and leave enough diagnostic evidence to reproduce the problem without exposing private data.
8. **Account for future cost.** Every entitlement, backend, dependency, notification, and platform target adds support and update work. Make its benefit visible before accepting that cost.
9. **Tell the truth.** Copy, paywalls, privacy claims, progress, and release notes must match actual behavior. Do not label a prompt, mockup, generated file, simulator run, or unchecked build as shipped quality.
10. **Revisit assumptions.** Apple APIs, devices, rules, and user needs change. Keep a short decision record with the condition that would make us change course.

## Apple engineering method

A strong Apple engineer is not ten times faster at typing. They remove waiting and rework: they decide on running software, let tools catch mistakes early, and never ship a claim they cannot show. Each practice below points to the place where this factory makes it required, not just encouraged.

| Practice | What it means here | Where it is enforced |
| --- | --- | --- |
| **Demo, then decide.** | Judge a flow, control, or animation on a running build. A document or mockup starts a discussion; it does not settle one. | `generate --starter ios` and `make run`; the `simulator-launch` gate comes before identity and polish work. |
| **One owner per decision.** | Every gate and every shared file has one directly responsible owner. Parallel agents never share a write scope. | `docs/agents/TASK-PACKET.md`. |
| **Say no first.** | A module, target, entitlement, SDK, or backend is rejected until a named user job needs it. | Capability contract in `AGENTS.md`. |
| **The compiler reviews first.** | Build in the Swift 6 language mode with complete data-race checking from the first commit. Adopting it later means a migration; adopting it at the start costs nothing. | Starter build settings. |
| **Tests pin behavior, measurements pin speed.** | Swift Testing covers state rules. XCTest metrics such as `XCTApplicationLaunchMetric` and Instruments compare a journey against a recorded baseline. | Starter `AppTests/`, `docs/quality/TEST-MATRIX.md`. |
| **Logs are part of the product.** | Use `Logger` with a subsystem, a category, and privacy on interpolated values; never `print`. Use signposts for slow intervals, and MetricKit and the Xcode Organizer for shipped builds. | Starter `FirstTask.swift`, `SECURE-FAST-DEFAULTS.md`. |
| **Every release is one-way.** | The App Store cannot roll back a binary; a phased release can only pause. During a rollout, old and new versions read the same data, so version stored data from the first release. | `docs/release/CHECKLIST.md`. |
| **Work to the platform calendar.** | Test betas from June, ship for the September release, and meet the SDK minimum that App Store Connect enforces each spring. | `docs/compatibility/REVIEW.md`, release checklist. |
| **Send bugs upstream.** | Reduce an Apple defect to a small sample project, file it in Feedback Assistant, and put the FB number beside the workaround so it can be removed later. | `docs/TROUBLESHOOTING.md`. |
| **Evidence states its limits.** | A gate is done only when it cites files that exist. A Simulator result never stands in for a device result. | `docs/quality/gates.json` and `make check`. |

The cultural practices come from published insider accounts, not Apple documentation: Ken Kocienda, *Creative Selection* (2018), on demo-driven decisions, and Adam Lashinsky, *Inside Apple* (2012), on directly responsible individuals. The technical practices cite Apple sources in `docs/research/apple-guideline-audit.md`.

## Two release priorities

Use the system's Liquid Glass for navigation and controls on supported OS versions, then verify legibility, accessibility settings, and fallback behavior. Keep content visually clear and treat custom glass as a deliberate functional choice. Measure responsiveness, memory, and energy on representative physical devices for every selected platform. Read `core/principles/GLASS-AND-PERFORMANCE.md` in this factory or `docs/quality/GLASS-AND-PERFORMANCE.md` in a generated app before approving a visual or performance claim.

## Review questions

Before calling work done, ask:

- Can a first-time person finish the intended job without explanation?
- What breaks when input, data, network, permission, account, or device state changes?
- Does the action mean the same thing wherever it appears?
- Is the result accessible, localizable, private, and responsive on selected platforms?
- Can we tell whether the change worked, failed, or made support harder?
- What evidence exists, and which claims remain unverified?
- Would this decision still make sense after the next OS release or a second app joins the ecosystem?

Answer the relevant questions with product evidence. Do not turn this guide into a ceremonial checklist for features that do not exist.
