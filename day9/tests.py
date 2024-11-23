import unittest
from solve import *
from utils import *
from pprint import pprint

class Download(unittest.TestCase):
    def test_download(self):
        download_input_file()

class Utils(unittest.TestCase):
    def test_load_file(self):
        data = load_input_file()

    def test_parse1(self):
        data = parse(SAMPLE1)
        print(data)

class Part1(unittest.TestCase):
    def test_sample(self):
        result = solve_part1(SAMPLE1)
        assert result == 114
        
    def test_input(self):
        raw = load_input_file()
        result = solve_part1(load_input_file())
        print(f"Part 1 Result: {result}")
        assert == 1684566095

if __name__ == '__main__':
    unittest.main()
