# Adaptive iPhone layout: iPhone Duo stress test

Checked 2026-09-25 against Apple's [iPhone Duo overview](https://developer.apple.com/iphone-duo/), [preparation talk](https://developer.apple.com/videos/play/tech-talks/111461/), [design talk](https://developer.apple.com/videos/play/tech-talks/111466/), [posture talk](https://developer.apple.com/videos/play/tech-talks/111463/), and [scenes talk](https://developer.apple.com/videos/play/tech-talks/111464/). Recheck the shipping SDK before using a new API. Apple currently calls for the iOS 27.1 SDK to optimize the full display; an ordinary iPhone app can run before that work is done.

## What “translate” means

Build **one app with one task and data model** whose presentation adapts to the available scene. The app can rearrange its own navigation, content, and controls. It cannot re-layout arbitrary third-party apps or change iOS system chrome. The form factor is a demanding test of the architecture, not a separate product feature.

## Keep these stable

- The user's current task, draft, selection, playback or activity state, and undo history survive open, close, rotate, resize, and split-view transitions.
- Data ownership and permissions remain the same on the outer and inner displays. A new view is not a reason to request access again or duplicate work.
- Actions keep their meaning and accessible names. A compact toolbar may move an action into a menu, but the action and result remain available.
- Deep links and restoration resolve to a task or item identifier, not to a hard-coded screen position.

## Let these adapt

| Available space | Presentation | Engineering rule |
| --- | --- | --- |
| Compact outer display | Focused list or detail, concise toolbar | Show the next useful action without needing the inner display. |
| Regular inner display | Sidebar with detail, or two useful panes | Use `NavigationSplitView` when the content has real list/detail structure; let it collapse naturally. |
| Rotation, resize, or multitasking | Reflow according to the **current scene or container** | Prefer size classes, safe areas, `ViewThatFits`, and local geometry. Never branch on model name, screen width, or `UIScreen.main`. |
| Folded or partially folded arrangement | Keep important content and targets in visible safe regions | Start with system layout and safe areas. Use posture-specific APIs only for a task that benefits from them, after checking availability and fallback. |

Keep Liquid Glass in system navigation and controls; do not create a translucent content sheet just because more pixels are available. Measure animation and scrolling during transitions on representative hardware.

## Implementation contract

1. Define the task state in an observable model outside the adaptive view hierarchy. Persist user work before a scene can be discarded.
2. Give list selections and destinations stable IDs. Use scene restoration for each window; do not share a global selected row across independent scenes.
3. Use native adaptive navigation first. If compact and regular layouts need different compositions, pass the **same state and actions** into both rather than forking business logic.
4. Read the current scene's environment and container size. Avoid static device detection and global screen geometry.
5. Test every permission, failure, keyboard, VoiceOver, Dynamic Type, contrast, and Reduce Motion path in both compact and regular layouts.
6. Treat extensions and system surfaces as separate presentations of the same underlying job. A Live Activity or widget is not an automatic continuation of an open app scene.

## Required stress matrix for an iPhone app

Record build, OS, simulator/device, result, screenshot or trace, and remaining issue for each applicable row in `docs/quality/TEST-MATRIX.md`:

| Transition or state | Pass condition |
| --- | --- |
| Ordinary compact iPhone, portrait and landscape | Primary job completes; controls remain reachable. |
| Duo outer display, open to inner, then close | Same draft/selection/result survives; no duplicate action or permission prompt. |
| Duo inner display, rotate and resize | Content reflows; no clipped controls, blank pane, or accidental navigation reset. |
| Duo partial fold and tent/landscape posture | Important text and controls stay visible and usable where the system allows. |
| Split view, two app scenes, and restoration | Each scene has the right navigation state; shared data stays consistent. |
| Largest supported text, VoiceOver, reduced transparency/motion | Reading order, focus, contrast, and task completion remain sound. |
| Transition while saving, loading, or offline | Work survives, progress is honest, cancellation and retry behave correctly. |
| Long session and repeated transitions | No meaningful memory growth, animation hitches, or thermal regression. |

Use Xcode's Duo simulator with the matching SDK for layout checks, then a physical Duo for hinge, touch, thermal, and performance claims. If either is unavailable, mark those rows **Pending**. Do not advertise verified Duo optimization on the strength of a compact iPhone preview alone.
