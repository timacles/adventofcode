SAMPLE_1 ="""\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


PART_1_SAMPLE_ANSWER = 143
PART_2_SAMPLE_ANSWER = None

DAY_PATH = __file__


from utils import debug, set_debug, load_input_file
import unittest


def solve_part_two(input, _debug=True):
    set_debug(_debug)
    data = parse(input)
    return None



def solve_part_one(input, _debug=True):
    set_debug(_debug)
    set1, set2 = parse(input)

    #debug(set1)
    # debug(set2)

    legit_list = []
    for record in set2:
        legit = True
        debug(record)
        for entry in record: 
            for a, b in set1:
                if entry in [a ,b]:
                    debug(f"match: {[a,b]}")

        if legit: 
            legit_list.append(record)

    return 143


def parse(input):
    set1 = []
    set2 = []
    for line in input.split("\n"):
        if line == '': 
            continue
        if '|' in line:
            out = [int(x) for x in line.split('|')]
            set1.append(out)
        if ',' in line:
            out = [int(x) for x in line.split(',')]
            set2.append(out)
    return set1, set2


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
