PYTHON=/opt/python3.3/bin/python3.3

all: test

test:
	$(PYTHON) -m unittest discover -v -s src/pysem

.PHONY: all test
