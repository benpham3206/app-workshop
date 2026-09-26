PYTHON ?= python3
CONFIG ?= examples/neutral-preview/project.json
OUTPUT ?= dist/neutral-preview
ICON_BRIEF ?= dist/neutral-preview/design/icon-brief.json
ICON_OUTPUT ?= dist/neutral-preview/docs/design/ICON-PLAN.md

.PHONY: validate generate troubleshoot icon-plan process-guide verify

validate:
	$(PYTHON) tooling/scaffold.py validate --config "$(CONFIG)"

generate:
	$(PYTHON) tooling/scaffold.py generate --config "$(CONFIG)" --output "$(OUTPUT)"

troubleshoot:
	$(PYTHON) tooling/troubleshoot.py --config "$(CONFIG)"

icon-plan:
	$(PYTHON) tooling/icon_plan.py --brief "$(ICON_BRIEF)" --output "$(ICON_OUTPUT)"

process-guide:
	$(PYTHON) tooling/process_guide.py

verify:
	$(PYTHON) -m unittest discover -s tests/generation -v
