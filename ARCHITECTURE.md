# Architecture

App Workshop is a factory. It turns a validated project selection into a generated Apple app scaffold, and carries later factory changes to that app with `make update`.

## Flow

```text
project.json (selection)
      ↓  tooling/scaffold.py validate   (data only, never executed)
selection + config/ + templates/ + core/ + design/ + platforms/ + modules/
      ↓  tooling/scaffold.py generate | adopt
generated app + .apple-scaffold.json (template version, selection, file hashes)
      ↓  tooling/scaffold.py update     (replaces only files the builder never edited)
current generated app
```

`dogfood/app-workshop/` is one generated app, committed. `make verify` fails when it falls behind the factory.

## Upstream

agent-engineering is the language-neutral layer above this factory. `tooling/sync-agent-engineering.sh` copies its standards into `vendor/` and its role packets and `scripts/` into the root; `vendor/agent-engineering.lock` pins the commit. Change those files upstream, not here.

## Layers

- `core/` contains stable rules and interaction contracts that apply across products.
- `config/` defines project choices, capability declarations, and likely-failure rules.
- `design/` defines selectable brand recipes and semantic design tokens. A recipe may express personality without replacing expected system behavior.
- `ux/` defines reusable journeys, interaction contracts, states, accessibility, and recovery patterns.
- `platforms/` defines native presentation and input behavior for each platform.
- `modules/` contains optional capabilities. Keep a capability independent until a real product selects it.
- `templates/` contains generated project files; `tooling/` generates, validates, and builds troubleshooting guides.
- `docs/` records product questions, research, decisions, release requirements, and support practices.

## Invariants

1. Generation never overwrites a nonempty target. ADOPT writes nothing when a conflict exists.
2. Configuration is validated as data and never executed.
3. The same template version and selection produce the same files.
4. Generated projects contain no factory internals (`tooling/`, `templates/`, `config/`).
5. `update` never overwrites a file the builder edited and never deletes a file.
6. A starter builds, tests, and launches; optional modules stay optional.
7. Security, privacy, accessibility, and data-loss protection are never simplified away.

Protect these with the generator tests in `tests/generation/`. Extend the closest existing test; add a new one only for a new class of failure.
