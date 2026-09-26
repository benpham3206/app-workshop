# Xcode project setup decisions

Complete when a product and first target are selected. The `--starter ios` project creates an unsigned app with the bundle ID `com.example.<slug>`; replace it and choose a team before device builds. Without a starter, the scaffold does not create an app.

| Decision | Value | Evidence |
| --- | --- | --- |
| Primary platform and device | Pending | |
| Xcode and SDK version | Pending | |
| Minimum OS version | Pending | |
| Glass API availability and earlier-OS fallback | Pending | |
| Representative physical devices and OS versions | Pending | |
| App target and bundle identifier | Pending | |
| Additional targets or extensions | Pending | |
| Signing team and capabilities | Pending | |
| Data storage and sync | Pending | |
| Test targets and preview fixtures | Pending | |
| App icon asset or Icon Composer file | Pending | |
| Distribution route (App Store; direct Mac if applicable) | Pending | |

First build gate: launch a minimal native app in Simulator. Then run the first useful journey on a physical device before adding more platforms or optional extensions. Record a launch and interaction baseline on the primary device; expand the matrix when selecting more device classes. Follow `docs/quality/GLASS-AND-PERFORMANCE.md`.

Apple references: [Configuring a new target](https://developer.apple.com/documentation/xcode/configuring-a-new-target-in-your-project/), [running on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices), [creating an icon with Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer). Reviewed 2026-09-25.
