PYTHON ?= python3
SAMPLE ?= sample-data/test-failure.json

.PHONY: setup test run run-json sample verify clean

setup:
	$(PYTHON) -m pip install -e .

test:
	$(PYTHON) -m unittest discover -s tests -v

run:
	$(PYTHON) -m ci_triage --input $(SAMPLE)

run-json:
	$(PYTHON) -m ci_triage --input $(SAMPLE) --format json

sample:
	./scripts/run-sample.sh

verify:
	./scripts/verify-environment.sh
	./scripts/validate-samples.sh
	$(PYTHON) -m unittest discover -s tests -v

clean:
	./scripts/cleanup.sh
