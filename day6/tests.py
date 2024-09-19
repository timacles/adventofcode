import unittest
from solve_problem import *

SAMPLE = "sample.txt"
INPUT = "input.txt"

class DAY6(unittest.TestCase):
    def test_Sample(self):
        raw = load_file(SAMPLE)
        time, dist = parse_raw(raw)

        results = process(time, dist)

        assert prod(results) == 288 

    def test_input1(self):
        raw = load_file(INPUT)
        time, dist = parse_raw(raw)

        results = process(time, dist)

        assert prod(results) == 771628
        
if __name__ == '__main__':
    unittest.main()
