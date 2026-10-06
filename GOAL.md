# Goal

## Objective

Give a first-time Apple app builder a native, product-neutral scaffold and a step-by-step process from idea to App Store release, with the evidence each step needs.

## Success conditions

- A selection generates a scaffold that passes its own `make check`. Evidence: `make verify`.
- The iOS starter builds, tests, and launches in Simulator. Evidence: `make verify-xcode`.
- An existing app receives factory changes without losing the builder's edits. Evidence: `make update`, and the dogfood check in `make verify`.
- The factory follows agent-engineering's backbone. Evidence: `scripts/verify-repo.sh` in `make verify`.

## Constraints

Native Apple frameworks first. No backend, account, purchase, or dependency until a selected product needs it. The invariants in `ARCHITECTURE.md` hold.

## Non-goals

Choosing a product, price, or audience for the builder. Language-neutral rules (agent-engineering owns those).
