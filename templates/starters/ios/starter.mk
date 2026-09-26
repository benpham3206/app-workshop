# Added by the iOS starter. The planning targets live in Makefile.
.PHONY: run test

run:
	./scripts/simulator.sh run

test:
	./scripts/simulator.sh test
