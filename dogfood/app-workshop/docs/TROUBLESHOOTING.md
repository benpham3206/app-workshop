# Likely failures and first checks

Generated for **App Workshop**. These are hypotheses to investigate, not diagnoses. Recheck linked Apple guidance when implementing a capability.

## Use this guide

1. Reproduce the symptom and record OS, device, build, account, and network state.
2. Follow the checks for the matching symptom; preserve the exact error or log.
3. Add the confirmed cause, fix, and regression check to the project issue or support note.
4. If the cause is in Apple's code, reduce it to a sample project, file it in [Feedback Assistant](https://developer.apple.com/bug-reporting/), and record the FB number beside the workaround.

## Build fails or an API is unavailable

**Symptom:** A selected target does not compile, launch, or offer the expected API.

First checks:

- Confirm Xcode, SDK, deployment target, and device OS versions for each selected platform.
- Check API availability and conditional code at the call site; do not infer support from another Apple platform.
- Reproduce on a supported Simulator and, for hardware-specific behavior, a physical device.

Apple reference: https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices

## A capability works in one build but fails after signing

**Symptom:** A device, TestFlight, or release build cannot use an expected capability.

First checks:

- Compare the capability in the target, App ID, provisioning profile, and signed entitlements.
- Check the failing build configuration and distribution environment rather than assuming debug settings carry over.
- Save the exact entitlement error and the affected target before changing signing settings.

Apple reference: https://developer.apple.com/documentation/bundleresources/diagnosing-issues-with-entitlements

## Privacy declaration or App Review blocks release

**Symptom:** Archive validation or App Review reports missing disclosure, permission context, or required metadata.

First checks:

- Inventory collected data, third-party SDKs, required-reason APIs, permission prompts, and in-app disclosures.
- Check the built app and included SDK privacy manifests against the actual behavior.
- Reproduce the reviewer path and include working credentials or demo access when review requires an account.

Apple reference: https://developer.apple.com/documentation/bundleresources/privacy-manifest-files

## A screen breaks with larger text or another language

**Symptom:** Content clips, controls lose labels, or a flow becomes difficult to complete.

First checks:

- Preview representative content at large text sizes, increased contrast, and Reduce Motion settings.
- Test longer translated strings and right-to-left layout where applicable.
- Verify every critical action with the platform's accessibility input and focus model.

Apple reference: https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog

## Liquid Glass is hard to read or feels overused

**Symptom:** Navigation or controls lose contrast, overlap content, or look inconsistent across OS versions and appearances.

First checks:

- Check whether standard navigation and controls already provide the correct system glass before adding a custom effect.
- Keep glass in the functional layer; remove decorative glass from content cards and reduce stacked blur or tint.
- Compare light and dark, increased contrast, reduced transparency, Reduce Motion, changing content, and earlier-OS fallback on selected devices.

Apple reference: https://developer.apple.com/design/human-interface-guidelines/materials

## The app is smooth on one device but slow or hot on another

**Symptom:** Launch, scrolling, a main action, memory, or energy use regresses on a supported device class.

First checks:

- Record the device, OS, release build, dataset, and exact journey; reproduce on representative physical hardware rather than relying on Simulator.
- Compare cold and warm launch, response, hitches, memory, and energy with a baseline for the same scenario.
- Profile the failing path with Xcode and Instruments; inspect broad view updates, main-thread work, images, and custom effects before changing the device support promise.

Apple reference: https://developer.apple.com/documentation/xcode/performance-and-metrics

## App Store submission rejects a beta toolchain build

**Symptom:** A build used in TestFlight cannot be submitted to the App Store.

First checks:

- Record the exact Xcode and SDK build used for the archive.
- Check the current App Store Connect release notes for App Store eligible release or RC builds and current SDK minimums.
- Use the allowed internal or external TestFlight path for beta builds while producing a separate eligible App Store archive.

Apple reference: https://developer.apple.com/help/app-store-connect/release-notes/

## App disappears from EU storefronts

**Symptom:** An intended EU listing is unavailable despite an approved app.

First checks:

- Check the app's EU territory availability in App Store Connect.
- Confirm the developer's DSA trader status was submitted and verified.
- Resolve an unverified trader status before investigating a binary or search-index issue.

Apple reference: https://developer.apple.com/news/?id=einwn76m
