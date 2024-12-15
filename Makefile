PYTHON = python  
SCRIPT = __main__.py 
TESTS = tests.py 

run:
	$(PYTHON) $(SCRIPT) $(ARGS)

clean:
	rm '__pycache__'

test:
	$(PYTHON) -m unittest -v -k $@

part1 part2 utils download:
	$(PYTHON) -m unittest -v -k $(@:units=Units)

.PHONY: run setup install clean test lint
