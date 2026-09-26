# Accounts module

Use only when the product needs an identity that local storage or iCloud alone cannot supply. First define what the account unlocks, whether guest use is possible, and which data belongs to the person versus the device. Choose sign-in methods after that decision; Sign in with Apple is an option, not a reason to add accounts.

Before implementation, specify creation, sign-in, sign-out, expired credentials, account recovery, device changes, data export, and deletion. Identify server ownership and what remains usable offline. If the app offers account creation, design an in-app path to initiate account deletion and explain what happens to associated data and active subscriptions. Test a lost credential and a deletion request as carefully as successful sign-in.

Source checked 2026-09-25: [Sign in with Apple implementation](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple), [account deletion guidance](https://developer.apple.com/support/offering-account-deletion-in-your-app).
