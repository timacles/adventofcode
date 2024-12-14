# Variables (optional)
PYTHON = python  
SCRIPT = solve.py 
TESTS = tests.py 

# Default target: Run the Python script
run:
	$(PYTHON) $(SCRIPT)

# Clean: Remove .pyc files and __pycache__ directories
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

test:
	$(PYTHON) -m unittest -v

units sample1 sample2 part1 part2:
	$(PYTHON) -m unittest -v -k $(@:units=Units)

##test:
#	$(PYTHON) -m unittest -v
#
#units:
#	$(PYTHON) -m unittest -k Units
#
#sample:
#	$(PYTHON) -m unittest -k Sample
#
#part1:
#	$(PYTHON) -m unittest -k Part1
#
#part2:
#	$(PYTHON) -m unittest -k Part2

.PHONY: run setup install clean test lint
