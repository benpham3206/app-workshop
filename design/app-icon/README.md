# App icon process

An icon is a product decision. The boilerplate supplies a process, not a generic icon or a shape that every app must share.

1. Write the app's one-sentence purpose and three recognizable visual ideas.
2. Sketch simple silhouettes that work at small sizes and do not depend on text or a screenshot of the UI.
3. Choose one symbol language that fits the selected identity recipe; check contrast and recognition in light and dark appearances.
4. Build platform variants from a common concept. Use Apple's current icon tools and export requirements for the selected SDK and platforms.
5. Preview the icon on a Home Screen or Dock, in search, notifications, and against neighboring icons. Test recognition at actual size.
6. Record source artwork, licenses, exported assets, and the decision in the generated project's identity document.

The generated project contains `design/icon-brief.json` and an icon planner. Once a real product promise and visual motifs are filled in, run `make icon-plan` from that project's root. It creates `docs/design/ICON-PLAN.md` with three concept prompts and a production checklist. Use an image-generation tool or designer for exploration, then refine the selected artwork and verify it in Xcode. A prompt is not a finished app icon.

Keep the source artwork editable under `design/assets/` in a real product. Do not add a placeholder icon to a generated app: it can be mistaken for a finished brand decision.

Apple reference: [App icons HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons). Apple's current guidance describes Icon Composer for iOS, iPadOS, macOS, and watchOS icon layers. Check platform-specific export details when a product is selected. Reviewed 2026-09-25.
