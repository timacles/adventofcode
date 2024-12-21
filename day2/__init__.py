SAMPLE_1 ="""\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


PART_1_SAMPLE_ANSWER = 2
PART_2_SAMPLE_ANSWER = 4


DAY_PATH = __file__


from utils import debug, load_input_file
import unittest
from dataclasses import dataclass





def evaluate_line(ints):
    legit = True
    for i, current in enumerate(ints):
        try:
            next = ints[i+1]
        except IndexError:
            break

        diff = abs(x - next)
        debug(f"  {i}) current: {current}, next: {next}, diff: {diff}")

        # conditions to invalidate on
        if diff > 3 or diff < 1: 
            debug("diff violation")
            legit = False
        if current > next and trend != DOWN: 
            debug("trend mismatch down")
            legit = False
        if x < next and trend != UP: 
            debug("trend mismatch up")
            legit = False 
    return legit



def solve_part_two(input):
    data = parse(input)
    counter = 0
    # main 'per line' loop
    for line in data:
        legit = True
        prev = None

        ints = [int(x) for x in line.split()]
        debug(f"Line: {line}, trend: {trend}")

        
        if not legit: break
        legit = True 
            
        if legit: 
            debug('this legit')
            counter += 1
            
    print("COUNTER:", counter)
    return counter


###
###===-===-===-===-
###

def solve_part_one(input):
    data = parse(input)
    counter = 0
    # main 'per line' loop
    for line in data:
        legit = True
        prev = None

        ints = [int(x) for x in line.split()]
        trend = determine_trend(ints)
        debug(f"Line: {line}, trend: {trend}")

        for i, x in enumerate(ints):
            # get value of the next element, or break 
            try:
                next = ints[i+1]
            except IndexError:
                break

            diff = abs(x - next)
            debug(f"{i}) current: {x}, next: {next}, diff: {diff}")

            # conditions to invalidate on
            if diff > 3 or diff < 1: 
                debug("diff violation")
                legit = False
            if x > next and trend != DOWN: 
                debug("trend mismatch down")
                legit = False
            if x < next and trend != UP: 
                debug("trend mismatch up")
                legit = False 

            if not legit: break
            legit = True 
        
        if legit: 
            debug('this legit')
            counter += 1
            
    print("COUNTER:", counter)
    return counter

UP = 'UP'
DOWN = 'DOWN'


def determine_trend(ints):
    ''' trend of the number pattern '''
    a,b = ints[:2]
    if a > b:
        return DOWN
    else:
        return UP


def parse(input):
    data = []
    for line in input.split("\n"):
        if line == '': 
            continue
        data.append(line)
    return data


class CheckExample(unittest.TestCase):
    ''' make sure the sample results is as expected '''

    def test_sample_one(self):
        ''' Test Sample One '''
        result = solve_part_one(SAMPLE_1)
        assert result == PART_1_SAMPLE_ANSWER

    def test_sample_two(self):
        ''' Test Sample Two '''
        result = solve_part_two(SAMPLE_1)
        assert result == PART_2_SAMPLE_ANSWER


test = unittest.main
