# Security policy

The general rules are agent-engineering's `vendor/agent-engineering/standards/security.md`. The Apple rules for generated apps are `core/principles/SECURE-FAST-DEFAULTS.md`. Agent authority over App Store Connect, signing, and TestFlight is in `docs/agents/TASK-PACKET.md`.

For this repository:

- Never commit secrets, signing assets (`.p8`, `.p12`, provisioning profiles), or populated `.env` files. `scripts/security-check.sh` fails on tracked secret files; `make verify` runs it.
- Project configuration is validated as data and never executed (`ARCHITECTURE.md`, invariant 2).
- Report a vulnerability privately to the repository owner through GitHub, not in a public issue.
