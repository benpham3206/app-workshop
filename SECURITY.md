# Security policy

The Apple security rules for generated apps are in `core/principles/SECURE-FAST-DEFAULTS.md`. Signing, App Store Connect, and TestFlight actions require explicit authorization from the builder in a bounded assignment. An agent cannot expand its own authority.

For this repository:

- Never commit secrets, signing assets (`.p8`, `.p12`, provisioning profiles), or populated `.env` files. `scripts/security-check.sh` fails on tracked secret files; `make verify` runs it.
- Project configuration is validated as data and never executed (`ARCHITECTURE.md`, invariant 2).
- Report a vulnerability privately to the repository owner through GitHub, not in a public issue.
