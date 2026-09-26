# Permission request and denial

Request a protected resource at the moment its benefit is clear. Use the system request and a concise purpose string that describes the actual use. A feature that can work without access should still offer that path. Review exact API behavior and platform availability when choosing a capability.

## Contract for each request

| Field | Product decision |
| --- | --- |
| User action that needs the resource | Pending |
| Resource and smallest useful scope | Pending |
| Prompt timing and purpose string | Pending |
| Data handling and retention | Pending |
| Denied, restricted, limited, or revoked path if applicable | Pending |
| Manual or reduced-function alternative | Pending |
| Where the person can revisit the choice | Pending |

Keep the original task and entered data intact when access is denied or the app is interrupted. Say which part cannot proceed and offer an actionable next step. Do not imitate the system permission alert or repeatedly block the whole app with a custom prompt. For a resource essential at launch, explain its need in context before requesting it.

Test first request, denial, limited access where supported, later revocation in Settings, and a return to the waiting task. Inspect privacy strings, entitlements, the privacy plan, and the selected module contract before release.

Apple source checked 2026-09-25: [Privacy HIG](https://developer.apple.com/design/human-interface-guidelines/privacy).
