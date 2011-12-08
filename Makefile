PYTHON=/opt/python3.3/bin/python3.3

all: test

clean:
	find . -name \*.pyc -delete -print 

test:
	$(PYTHON) -m unittest discover -v -s src/pysem

.PHONY: all test
