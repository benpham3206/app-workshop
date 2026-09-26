# Build and verification automation

Introduce automation after an Xcode project exists. Keep the first pipeline fast and meaningful.

| Trigger | Checks | Evidence |
| --- | --- | --- |
| Every change | Format/lint if configured, build selected targets, focused unit tests, generated-file validation. | Exit status and logs linked to the change. |
| Before beta | UI journeys, preview or screenshot review, accessibility and localization checks, signed archive. | Test matrix, build artifact, device notes. |
| Before release | Final platform matrix, privacy and entitlement review, purchase restore if used, release metadata, TestFlight feedback. | Release checklist and approved candidate build. |
| After release | Crashes, launch/performance trends, support reports, OS beta compatibility. | Triage and next patch decision. |

Pin the Xcode and SDK environment, use deterministic fixtures, and keep credentials in the CI service rather than the repository. Start with one primary platform; add build destinations as supported product behavior is added. Xcode Cloud can build, analyze, test, archive, and distribute to TestFlight; choose it or another CI system based on the actual project and account setup.

Apple reference: [Configuring your first Xcode Cloud workflow](https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow). Reviewed 2026-09-25.
