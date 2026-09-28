# Accounts module

Use only when the product needs an identity that local storage or iCloud alone cannot supply. First define what the account unlocks, whether guest use is possible, and which data belongs to the person versus the device. Choose sign-in methods after that decision; Sign in with Apple is an option, not a reason to add accounts.

Before implementation, specify creation, sign-in, sign-out, expired credentials, account recovery, device changes, data export, and deletion. Identify server ownership and what remains usable offline. If the app offers account creation, design an in-app path to initiate account deletion and explain what happens to associated data and active subscriptions. Test a lost credential and a deletion request as carefully as successful sign-in.

Source checked 2026-09-25: [Sign in with Apple implementation](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple), [account deletion guidance](https://developer.apple.com/support/offering-account-deletion-in-your-app).

## Build vs. buy

| Option | Choose when | Tradeoff |
| --- | --- | --- |
| AuthenticationServices: Sign in with Apple and passkeys (default) | The app needs identity on Apple platforms. | No auth vendor; the app still owns account data and deletion. |
| Supabase Auth | A named need for a relational backend and shared identity across clients. | Hosted identity data and backend operations; verify current price, SDK license, privacy declarations, and export before adopting. |
| Clerk | A named need for managed MFA or organization sign-in UI. | Hosted identity and vendor integration; SDK license, pricing, privacy declarations, and exit path are unverified here—verify before adopting. |

Apple source: [AuthenticationServices](https://developer.apple.com/documentation/authenticationservices) (checked 2026-09-27).
