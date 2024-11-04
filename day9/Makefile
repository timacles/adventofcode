PYTHON = python  
SCRIPT = solve.py 
TESTS = tests.py 

include .env

export

run:
	$(PYTHON) $(SCRIPT)

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

test:
	$(PYTHON) -m unittest -v

units sample1 sample2 sample3 part1 part2 utils download:
	$(PYTHON) -m unittest -v -k $(@:units=Units)

.PHONY: run setup install clean test lint
