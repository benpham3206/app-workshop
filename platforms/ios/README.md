# iOS profile

Primary input is touch. Design for compact space, orientation and size changes, safe areas, Dynamic Type, and one-handed reach when relevant. Select iPhone-specific system surfaces only when the app has a real use for them.

Let supported system bars and controls carry Liquid Glass; keep scrolling content legible beneath them and define an earlier-OS fallback for custom effects. Measure launch, main-action response, scrolling, memory, and energy on an oldest supported iPhone class and a current class, including a high-refresh display if promised.

Source checked 2026-09-25: [Apple interface fundamentals](https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals), [layout](https://developer.apple.com/design/human-interface-guidelines/layout).

For iPhone apps, use the adaptive layout contract (`platforms/ios/ADAPTIVE-LAYOUT.md` in the boilerplate; `docs/compatibility/IPHONE-DUO.md` in a generated app) as the iPhone Duo stress test. Preserve task state while the current scene changes between compact and regular space; verify the transitions in Simulator and on hardware before claiming support.
