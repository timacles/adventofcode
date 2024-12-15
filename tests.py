import unittest
from utils import *
from pprint import pprint



class Utils(unittest.TestCase):

    def test_template_lister(self):
        files = get_list_of_template_files()
        print(files)


if __name__ == "__main__":
    unittest.main()
