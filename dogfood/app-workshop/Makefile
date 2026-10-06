PYTHON ?= python3

.PHONY: check icon-plan

check:
	$(PYTHON) tools/readiness.py

icon-plan:
	$(PYTHON) tools/icon_plan.py --brief design/icon-brief.json --output docs/design/ICON-PLAN.md

-include starter.mk
