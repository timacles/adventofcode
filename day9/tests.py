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
        
if __name__ == '__main__':
    unittest.main()
