SAMPLE_1 ="""\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""


PART_1_SAMPLE_ANSWER = 161
PART_2_SAMPLE_ANSWER = None

DAY_PATH = __file__


from utils import debug, load_input_file
import unittest


def solve_part_two(input):
    data = parse(input)
    return None


def solve_part_one(input):
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
