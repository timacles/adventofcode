import unittest
from solve import *
from utils import *
from pprint import pprint

class Download(unittest.TestCase):
    def test_download(self):
        download_input_file()

class Utils(unittest.TestCase):
    def test_env(self):
        print(SESSION_COOKIE)
    
        
if __name__ == '__main__':
    unittest.main()
