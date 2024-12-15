SAMPLE_1 ="""\
"""

PART_1_SAMPLE_ANSWER = 0
PART_2_SAMPLE_ANSWER = 0 

DAY_PATH = __file__

from utils import debug, load_input_file
import unittest


def solve_part_two(input):
    print("\n*** PART -TWO- ***")
    data = parse(input)
    result = None
    print(f"  ==> PART -TWO- RESULT: [[ {result} ]]")
    return result


def solve_part_one(input):
    print("\n*** PART -ONE- ***")
    data = parse(input)
    result = None
    print(f"  ==> PART -ONE- RESULT: [[ {result} ]]")
    return result


def parse(input):
    data = []
    for line in input.split("\n"):
        if line == '': 
            continue
        data.append(line)
    return data


class Sample(unittest.TestCase):
    def test_sample_one(self):
        result = solve_part_one(SAMPLE_1)
        assert result == PART_1_SAMPLE_ANSWER

    def test_sample_two(self):
        result = solve_part_two(SAMPLE_1)
        assert result == PART_2_SAMPLE_ANSWER


test = unittest.main
