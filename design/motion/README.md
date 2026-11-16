# Motion

Use this spec when an app screen changes in view. It gives the motion rules for a native Apple app and the check that proves them. The identity recipe in `design/identity/` sets the character of the motion. This file sets the rules that hold for every recipe.

The rules come from two sources. Stageshow (the `stageshow` agent skill by Benji Taylor, MIT) is a set of rules for product demos on the web; the rules below are the ones that also hold in a real app, put in SwiftUI terms. The `principles-motion` skill in [Principles](https://github.com/benpham3206/principles) supplies the method for beats, setup and payoff, and proof by stills. Read it before you design a sequence longer than one transition.

## Rules

1. **Each motion has a cause.** A motion starts from an input or from a state change the person can see. Do not add motion that runs with no cause. After a motion ends, nothing moves.
2. **Feedback is immediate.** The response to a press starts on the press. Do not put a delay before feedback to make it look smooth. Only a sequence that explains something, such as onboarding, can go slower.
3. **Change only what changed.** When one value changes, move that value and keep the words around it still. Use `contentTransition(.numericText())` for a number. Give a control one fixed footprint for all its labels, so that a label change does not move its neighbors.
4. **Nothing appears or leaves in one frame.** Give each inserted view a transition, and keep a removed view until its exit ends. Put the neighbors in the same animation, so that they make room while the new view arrives.
5. **One object stays one object.** When a card opens into a screen, or a thumbnail becomes a detail view, move the same object. Use `matchedGeometryEffect` or the zoom navigation transition. Move size, position, and content as one transition. Do not stretch text; `geometryGroup()` keeps a child from animating apart from its parent.
6. **A motion can be interrupted.** A second input during a motion redirects it from its current position. Use spring animations for motion that follows a gesture. Do not block input until an animation ends.
7. **Navigation and data do not run backward.** A screen goes back only when the person goes back. A total, a list, or a progress value does not rewind in view.
8. **Each state has a resting frame.** The settled frame after a motion must show the result without the motion. This frame is the Reduce Motion design, the screenshot, and the App Store capture. Do not let a resting frame show a value in the middle of a change.
9. **Reduce Motion keeps the meaning.** Read `accessibilityReduceMotion`. Replace travel, zoom, and parallax with a short fade or with no animation. Keep the state change and the feedback.
10. **A group arrives in reading order.** Start each item 40 to 80 ms after the last one. One object arrives whole; do not stagger its parts.
11. **One accent per screen.** Mark the one moment that matters with the strongest motion. A persistent animation on a settled screen is a defect.

## Check

A still cannot show a view that appears in one frame. Record the motion and read the frames.

1. Run the job in Simulator and record it: `xcrun simctl io booted recordVideo docs/quality/evidence/<job>.mov`. Stop the recording with Control-C.
2. Step through each press, insert, removal, and navigation frame by frame in QuickTime Player (the arrow keys). Look for a view that appears with no entrance, text that stretches, a neighbor that jumps after the new view lands, and a value that changes in one frame.
3. Read the resting frame after each motion with the motion covered. If the frame does not show what happened, change the frame (rule 8).
4. Do the job again and interrupt each motion with a second input (rule 6).
5. Do the job again with Reduce Motion on (Settings, Accessibility, Motion). The job must reach the same resting frames.
6. Test a gesture, a haptic, or a hitch on a physical device. Simulator does not prove them.

Record the result in the Motion row of `design/NATIVE-REVIEW.md` with the path to the recording. If a step was not done, write that it was not done.

## Apple references

Primary sources checked 2026-11-16. Check them again against the SDK and minimum OS of the actual app.

| API | Available from |
| --- | --- |
| [`withAnimation`](https://developer.apple.com/documentation/swiftui/withanimation(_:_:)) | iOS 13, macOS 10.15, watchOS 6, visionOS 1 |
| [`accessibilityReduceMotion`](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion) | iOS 13, macOS 10.15, watchOS 6, visionOS 1 |
| [`matchedGeometryEffect`](https://developer.apple.com/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)) | iOS 14, macOS 11, watchOS 7, visionOS 1 |
| [`contentTransition(.numericText())`](https://developer.apple.com/documentation/swiftui/contenttransition/numerictext(countsdown:)) | iOS 16, macOS 13, watchOS 9, visionOS 1 |
| [`geometryGroup()`](https://developer.apple.com/documentation/swiftui/view/geometrygroup()) | iOS 17, macOS 14, watchOS 10, visionOS 1 |
| [Zoom navigation transition](https://developer.apple.com/documentation/swiftui/navigationtransition/zoom(sourceid:in:)) | iOS 18, watchOS 11, visionOS 2. Not on macOS. |

Design guidance: [Human Interface Guidelines: Motion](https://developer.apple.com/design/human-interface-guidelines/motion).
