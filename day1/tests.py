import unittest
from day1 import *
from pprint import pprint


class Sample(unittest.TestCase):
    def test_sample_one(self):
        result = solve_part_one(SAMPLE_1)
        assert result == 11

    def test_sample_two(self):
        result = solve_part_two(SAMPLE_1)
        assert result == 31

if __name__ == "__main__":
    unittest.main()
