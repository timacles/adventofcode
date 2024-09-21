import unittest
from solve_problem import *

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

    def test_final_input(self):
        raw = load_file(INPUT)
        time, dist = parse_raw(raw)
        time = join_elements(time)
        dist = join_elements(dist)
        results = process(time, dist)
        print("RESULT:", results)
        assert results[0] == 27363861
        
if __name__ == '__main__':
    unittest.main()
