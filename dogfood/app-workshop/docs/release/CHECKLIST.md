# Release checklist

Complete this for the actual app and supported regions. Treat unchecked items as decisions to make, not claims of compliance.

- [ ] Build and run on every selected platform and relevant physical hardware.
- [ ] Check accessibility, localization, appearance, and Reduce Motion.
- [ ] Complete `docs/design/NATIVE-REVIEW.md` with build and device evidence; resolve all core-job blockers.
- [ ] Review permissions, privacy manifest, App Store privacy details, and third-party SDKs.
- [ ] Verify purchase and restore flows if commerce is selected.
- [ ] Verify account deletion if the app creates accounts.
- [ ] Prepare truthful metadata, screenshots, support and privacy URLs, and reviewer access.
- [ ] Determine encryption export requirements and any category-specific rules.
- [ ] Test a final build with appropriate beta distribution before submission.
- [ ] Resolve the current OS and device decisions in `docs/compatibility/REVIEW.md`; align the support claim with tested evidence.
- [ ] If distributing a Mac app directly, verify Developer ID signing, hardened runtime, notarization, packaging, update delivery, and support for that route.
- [ ] Confirm support contact, issue triage, crash monitoring, and a way to ship fixes after launch.
