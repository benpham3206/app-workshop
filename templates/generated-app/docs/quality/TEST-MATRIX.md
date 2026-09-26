# Quality matrix

Select the rows that apply to the actual app. Record device, OS, build, result, and evidence. Simulator coverage alone does not prove hardware behavior. Use `GLASS-AND-PERFORMANCE.md` for runtime gates and `../design/NATIVE-REVIEW.md` for the full experience review.

## Representative devices

Record the oldest supported class, a common current class, and any materially different display or input class for **each selected platform**. Add the actual model and OS before beta. If a physical class is unavailable, keep its evidence pending and do not claim it was tested.

| Platform | Device and OS | Why this class matters | Build | Evidence status |
| --- | --- | --- | --- | --- |
| Primary | Pending | Oldest supported / baseline | | Pending |
| Primary | Pending | Common current | | Pending |
| Additional selected class | Pending | Different size, input, or performance | | Pending |

## Scenario checks

| Area | Scenario | Destination | Evidence | Result |
| --- | --- | --- | --- | --- |
| Core job | First useful result from a fresh install | Primary device | | Pending |
| Native experience | Complete job across sizes, appearances, states, and input methods | Each selected platform | | Pending |
{{IPHONE_TEST_MATRIX_ROW}}
| Recovery | Offline, interrupted, denied permission, or failed request | Primary device | | Pending |
| Data | Restart, migration, export/deletion, and sync conflict if used | Two devices if sync | | Pending |
| Accessibility | VoiceOver, large text, contrast, Reduce Motion | Each selected platform | | Pending |
| Localization | Long strings, plurals, right-to-left if supported | Each selected platform | | Pending |
| Glass | Navigation/control hierarchy, legibility over changing content, OS fallback | Each selected platform and appearance | | Pending |
| Glass accessibility | Increased contrast, reduced transparency, Reduce Motion, keyboard/focus | Representative devices | | Pending |
| Performance | Cold/warm launch and time to first useful result | Representative physical devices | | Pending |
| Performance | Main-action response, scrolling and animation hitches | Representative physical devices; release build | | Pending |
| Performance | Memory peak, long session, energy and thermal impact | Representative physical devices | | Pending |
| Performance | Background and extension budgets if selected | Supported hardware | | Pending |
| Commerce | Purchase, restore, expiration, cancellation, refund if used | Sandbox/TestFlight | | Pending |
| System surfaces | Widget/activity/intent and extension failure if used | Supported hardware | | Pending |
| Distribution | Signed build, TestFlight install, reviewer path | Release candidate | | Pending |

Add focused automated tests for critical rules and regressions. Use previews and fixtures for visual states. Reserve manual device testing for platform behavior automation cannot establish.

For a performance comparison, record the same scenario and dataset before and after the change. Use Xcode and Instruments when a result regresses; report observed numbers rather than an unsupported universal target.
