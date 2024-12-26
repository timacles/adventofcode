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
DEBUG = True


from utils import debug as _debug, load_input_file
from dataclasses import dataclass
import unittest


def eval_all_possibilities(ints):

    # if the first pass is good, then just return
    legit, offender = evaluate_line(ints)     
    if legit:
        return legit

    # Remove each element, test and then reinsert it 
    offenders = []
    for i, element in enumerate(ints):
        ints.pop(i)
        debug(f"  popped: {element}, {ints}")
        legit, offender = evaluate_line(ints)
        # we only need to find one instance popped 
        # scenario that is legit, so exit if found
        if legit: 
            debug(f"  this legit")
            return legit
        ints.insert(i, element)


def solve_part_two(input):
    set_debug(True)
    data = parse(input)
    counter = 0
    for i, line in enumerate(data):
        legit = True
        ints = [int(x) for x in line.split()]
        debug(f"[{i}]  ENTRY: {ints} <==---------------------")
        legit = eval_all_possibilities(ints)
        if legit:
            counter += 1
    print("COUNTER:", counter)
    return counter


def evaluate_line(ints) -> (bool, tuple):
    ''' returns legit, & idx, val of the offending element ''' 
    legit = True
    offender = None
    prev_trend = determine_trend(ints)
    for i, current in enumerate(ints):

        try:
            next = ints[i+1]
        except IndexError:
            break

        trend = determine_trend([current, next])
        diff = abs(current - next)
        #debug(f"    {i}) current: {current}, next: {next}, diff: {diff}")

        violations = [
            (diff > 3 or diff < 1, "diff violation"),
            (current > next and trend != prev_trend, "trend change down"),
            (current < next and trend != prev_trend, "trend change up"),
        ]
        for condition, message in violations:
            if condition:
                legit = False
                offender = (i, current)
                debug(f"   ==> {message}, offender: {offender}")
        if not legit:
            break 
        # if there are no violations, the loop proceeds
        prev_trend = trend
    return legit, offender






### ---  ---  ---  ---  ---  ---  ---  ---
### ===--===--===--===--===--===--===--===
### ---  ---  ---  ---  ---  ---  ---  ---

def solve_part_one(input):
    set_debug(False)
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

    def test_edge_case_1(self):
        ''' Edge case 1 '''
        ints = [71, 69, 70, 71, 72, 75]
        debug(ints) 
        legit = eval_all_possibilities(ints)
        assert legit == True


test = unittest.main





def _old_solve_part_two(input):
    set_debug(True)
    data = parse(input)
    counter = 0
    for i, line in enumerate(data):
        legit = True
        ints = [int(x) for x in line.split()]
        debug(f"[{i}]  ENTRY: {ints} <==---------------------")
        legit, offender = evaluate_line(ints)     
        if legit: 
            debug('     === this legit ===')
            counter += 1
        else:
            ints.pop(offender[0])
            debug(f"=== 2nd Eval: {ints}")
            legit, offender = evaluate_line(ints)
            if legit: 
                debug('=== 2nd eval, this legit ===')
                counter += 1
    print("COUNTER:", counter)
    return counter
