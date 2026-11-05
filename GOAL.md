# Goal

## Objective

Give an Apple app builder a native, product-neutral scaffold, a runnable iOS starter, and verifiable build and release requirements.

## Success conditions

- A selection generates a scaffold that passes its own `make check`. Evidence: `make verify`.
- The iOS starter builds, tests, and launches in Simulator. Evidence: `make verify-xcode`.
- An existing app receives factory changes without losing the builder's edits. Evidence: generation, adoption, and update checks in `make verify`.
- Repository structure, unresolved template tokens, and tracked secret files are checked by locally owned scripts. Evidence: `make verify`.

## Constraints

Native Apple frameworks first. No backend, account, purchase, or dependency until a selected product needs it. The invariants in `ARCHITECTURE.md` hold.

## Non-goals

Choosing a product, price, or audience for the builder. Selling, store publishing, hosted legal pages, and general engineering method. External homes are linked in `README.md`.
