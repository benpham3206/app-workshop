# App Workshop self-test evidence

Checked 2026-09-25 on an arm64 Mac running macOS 27.2.

| Check | Observed result |
| --- | --- |
| Factory contract suite | Ten tests passed after the current generator changes. |
| Generated project self-check | `make check` passed structure and reported the remaining planning and device-review decisions. |
| Generated navigation | Factory and App Workshop relative links resolved; selected map lists macOS and no optional modules. |
| Catalog generation | All nine optional module contracts generated in a temporary iOS + macOS selection. |
| Local Mac build | `App/build.sh` compiled the SwiftUI app, bundled the process guide and icon, and produced an ad hoc signed `.app`. |
| Bundle metadata | Binary load command and Info.plist both declare macOS 14 as the minimum. Signature verification passed. |
| UI structure | `NavigationSplitView`, a native list, menus, checkboxes, and system buttons are used; the detail uses content dividers rather than custom cards or glass effects. |
| Checklist and flow | In the running app, all three phase-1 checkboxes were selected; “Mark as complete” then became enabled. Pressing it selected phase 2 and changed progress to 1 of 13. Test progress was reset afterward. |
| Window chrome | The duplicate phase title and lighter toolbar background were removed on the tested macOS 27.2 window. |
| Progress model | `App/test.sh` passed legacy checklist migration, completion gating, persistence, reopening after uncheck, and reset in an isolated defaults suite. Stable action IDs now keep progress through copy changes. |
| Sandbox | The local build was signed with the App Sandbox entitlement and passed strict signature verification. No network, file access, or account entitlement is requested. |

The app was launched and its phase list and detail layout were visually inspected on this Mac during the self-test. This is a local prototype, so the release matrix remains pending: no older macOS device, Intel Mac, accessibility setting sweep, Instruments capture, energy profile, or App Store distribution test has been completed. Native system controls are the chosen Liquid Glass path; visual behavior under multiple appearances and OS versions still needs review before any broad compatibility claim. Record those results in `TEST-MATRIX.md` when the app advances toward beta.
