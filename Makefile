PYTHON = python  
SCRIPT = solve.py 
TESTS = tests.py 

include ../.env

export

run:
	$(PYTHON) $(SCRIPT)

clean:
	rm '__pycache__'

test:
	$(PYTHON) -m unittest -v -k $@

part1 part2 utils download:
	$(PYTHON) -m unittest -v -k $(@:units=Units)

.PHONY: run setup install clean test lint
