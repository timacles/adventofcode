import unittest
from solve import *
from utils import *
from pprint import pprint



##################################
### PART 2
##


class Part2(unittest.TestCase):
    def test_sample(self):
        result = solve_part2(SAMPLE1)
        print(f"\n=== PART 2 SAMPLE RESULT ==> [{result}] <==") 

    def test_input(self):
        raw = load_input_file()
        result = solve_part2(load_input_file())
        print(f"\n=== PART 2 RESULT ==> [{result}] <==") 




##################################
### PART 1
##


class Part1(unittest.TestCase):

    def test_sample(self):
        result = solve_part1(SAMPLE1[0])
        assert result == 0

        
    # not ready
    def _test_input(self):
        raw = load_input_file()
        result = solve_part1(load_input_file())
        print(f"Part 1 Result: {result}")
        assert result == 0



##################################
### OTHER
##
        

class Download(unittest.TestCase):
    def test_download(self):
        download_input_file()


class Utils(unittest.TestCase):
    def test_load_file(self):
        data = load_input_file()

    def test_parse1(self):
        data = parse(SAMPLE1)
        print(data)

#######
##

if __name__ == '__main__':
    unittest.main()
