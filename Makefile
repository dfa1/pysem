PYTHON=python3.1

all: test

test:
	@PYTHONPATH=$$PYTHONPATH:src $(PYTHON) -m unittest pysem

.PHONY: test
