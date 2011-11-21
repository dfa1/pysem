PYTHON=/opt/python3.2/bin/python3

all: test

test:
	$(PYTHON) -m unittest discover -v -s src/pysem

.PHONY: test
