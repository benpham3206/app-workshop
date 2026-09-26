# {{PROJECT_NAME}}

This is a product-neutral Apple app planning scaffold. Its selected identity, platforms, and optional modules are recorded in `.apple-scaffold.json`. There is no application implementation yet.

## Start here

1. Read `docs/BEGINNER-GUIDE.md` for the step-by-step path. Complete `docs/product/BRIEF.md` with the user's job and first useful result. Use `docs/START-TO-SHIP.md` and `docs/OPERATING-SYSTEM.md` as the delivery maps.
2. Review `docs/design/IDENTITY.md` and the selected identity recipe.
3. Map the main journey in `docs/ux/FLOWS.md`.
4. Define each important action with `docs/ux/interactions/ACTION-CONTRACT.md`. Read the button, menu, and input guides before styling controls.
   Use `docs/ux/patterns/` for first launch, permissions, settings, and help decisions when they apply.
5. Fill `docs/ux/STATES.md`; then choose semantic tokens and components in `docs/design/` and review `APP-ICON.md`.
6. Confirm selected platform profiles and module contracts. Use `docs/TROUBLESHOOTING.md` for likely failures.
7. When a product is chosen, fill `docs/engineering/PROJECT-SETUP.md` before creating the Xcode project. Track work in `docs/operations/WORKBOARD.md`, evidence in `docs/quality/TEST-MATRIX.md`, and later automation in `docs/quality/AUTOMATION.md`.
8. Treat `docs/quality/GLASS-AND-PERFORMANCE.md` as a design and release gate: use native glass for controls and navigation where supported, and measure the real journey across representative devices.
9. Use `docs/design/NATIVE-REVIEW.md` to inspect the runnable experience and record evidence for each supported platform.
10. Revisit `docs/compatibility/REVIEW.md` for each OS, SDK, or device change that could affect the app.

Run `make check` in this project to verify its generated structure and list open planning decisions. Once the product promise and motifs are real, fill `design/icon-brief.json` and run `make icon-plan` here. These tools are included in the generated project. `make check` does not verify an app build or approve release.

Read `AGENTS.md` and `docs/agents/NAVIGATION.md` before changing this project. Use `docs/agents/TASK-PACKET.md` to give any assigned agent a clear file scope and evidence target.
