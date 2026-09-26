# Liquid Glass and device performance gates

These are priorities for every app built from this scaffold. Apply them when a real product and supported devices are chosen. A generated app records evidence in `docs/quality/TEST-MATRIX.md`; this guide defines what to look for. Recheck API availability and current Apple guidance with each SDK release.

## 1. Use Liquid Glass as a platform layer

Start with native navigation, toolbars, sidebars, sheets, and controls. On supported OS versions, the system supplies much of the Liquid Glass appearance and behavior. Keep the product's content clear and let the navigation and control layer float above it. Add custom glass only when a functional control needs it; group nearby custom elements coherently and avoid stacked blur, opaque chrome, decorative tint, and glass cards filling the content area. The three identity recipes can change accent, content, icon, motion, and copy without replacing native navigation behavior.

Record the minimum OS and fallback for any explicit glass API. Check light and dark appearances, increased contrast, reduced transparency, Reduce Motion, changing content behind controls, window resizing, pointer/keyboard/focus, and legibility at small sizes. A screenshot from one OS and appearance is not a glass review for all selected platforms.

## 2. Make performance a device matrix

Choose representative hardware for each selected platform: the oldest supported device class, a common current device, and any materially different display, input, or performance class the app promises to support. Include Mac architecture and window sizes where applicable. Add paired-device and extension paths when selected. Record the model, OS, build configuration, dataset, and scenario; a simulator is useful for layout and debugging but does not replace physical-device performance evidence.

Measure the actual user journey: cold and warm launch, first useful result, response to the main action, scrolling and animation hitches, memory peak, long-session behavior, energy and thermal impact, background or extension work, and recovery after interruption. Pick numeric targets after a baseline on representative hardware; do not invent a universal threshold. Re-run the same scenario after a change and compare. Use Xcode and Instruments to investigate a symptom, then fix the owning work (for example, broad view updates, unstable list identity, work in view bodies, image decoding, or excessive effects) before tuning visuals further.

## 3. Gate design and release with evidence

| Gate | Evidence required | If it fails |
| --- | --- | --- |
| First design pass | Native control/navigation proposal, content-versus-glass decision, minimum OS fallback, representative device list | Simplify the surface or narrow supported scope. |
| Working vertical slice | Preview states plus the primary journey on hardware; launch and interaction baseline | Diagnose the slow or unclear path before adding more surfaces. |
| Before beta | Appearance/accessibility checks and repeatable performance captures across representative device classes | Fix high-impact regressions or state the unsupported class honestly. |
| Before release | Final-build matrix with device, OS, scenario, observed result, remaining risks, and support path | Do not claim coverage that was not run. |

The goal is a responsive, legible app that fits each device, not a fixed amount of translucency. Standard controls may already deliver the correct glass. Treat every new custom effect as a cost in readability, rendering, and maintenance that must earn its place.

Sources checked 2026-09-25: [Apple HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [SwiftUI performance](https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance), [Xcode performance and metrics](https://developer.apple.com/documentation/xcode/performance-and-metrics).
