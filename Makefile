PYTHON ?= python3
CONFIG ?= examples/neutral-preview/project.json
OUTPUT ?= dist/neutral-preview
STARTER ?=
PROJECT ?=
APPLY ?=
ICON_BRIEF ?= dist/neutral-preview/design/icon-brief.json
ICON_OUTPUT ?= dist/neutral-preview/docs/design/ICON-PLAN.md

.PHONY: validate generate adopt update troubleshoot icon-plan process-guide verify verify-xcode

validate:
	$(PYTHON) tooling/scaffold.py validate --config "$(CONFIG)"

generate:
	$(PYTHON) tooling/scaffold.py generate --config "$(CONFIG)" --output "$(OUTPUT)" $(if $(STARTER),--starter "$(STARTER)")

adopt:
	$(PYTHON) tooling/scaffold.py adopt --config "$(CONFIG)" --project "$(PROJECT)"

update:
	$(PYTHON) tooling/scaffold.py update --project "$(PROJECT)" $(if $(APPLY),--apply)

troubleshoot:
	$(PYTHON) tooling/troubleshoot.py --config "$(CONFIG)"

icon-plan:
	$(PYTHON) tooling/icon_plan.py --brief "$(ICON_BRIEF)" --output "$(ICON_OUTPUT)"

process-guide:
	$(PYTHON) tooling/process_guide.py

verify:
	$(PYTHON) -m unittest discover -s tests/generation -v
	bash scripts/verify-repo.sh

verify-xcode:
	APP_WORKSHOP_XCODE=1 $(PYTHON) -m unittest discover -s tests/generation -v
