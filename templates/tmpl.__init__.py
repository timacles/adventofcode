SAMPLE_1 ="""\
"""


PART_1_SAMPLE_ANSWER = None
PART_2_SAMPLE_ANSWER = None

DAY_PATH = __file__


from utils import debug, set_debug, load_input_file
import unittest


def solve_part_two(input):
    set_debug(True)
    data = parse(input)
    return None


def solve_part_one(input):
    set_debug(True)
    data = parse(input)
    return None


def parse(input):
    data = []
    for line in input.split("\n"):
        if line == '': 
            continue
        data.append(line)
    return data


class Sample(unittest.TestCase):
    def test_sample_one(self):
        ''' Test Sample One '''
        result = solve_part_one(SAMPLE_1)
        assert result == PART_1_SAMPLE_ANSWER

    def test_sample_two(self):
        ''' Test Sample Two '''
        result = solve_part_two(SAMPLE_1)
        assert result == PART_2_SAMPLE_ANSWER


test = unittest.main
