SAMPLE1 = ["""\
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
""",
]

from dataclasses import dataclass
from utils import load_input_file, debug, info
from pprint import pprint


###########################==--
### part 2 #########==--
## ==---------

def solve_part2(input):
    results = []
    print(f"*** Part 2 ***")
    return results


###########################==--
### part 1 #########==--
## ==---------


def solve_part1(input):
    print(f"*** Part 1")
    results = []
    data = parse(input)
    data.print()
    s_location = find_s(data)
    debug(f"*** Start {s_location}")
    return sum(results)



###########################
### functions
##


def find_next_loc(in_loc, char):
    ''' determine the next location from the current
    character and location.
    '''



def find_loop(start_loc, data):
    x, y = *start_loc
    while True:
        pass



def find_s(data):
    for row, col, char in data:
        if char == "S":
            return Loc(row, col)
    raise Exception(f"S not found. End pos = [{i}:{j}]")



def parse(input):
    data = Data()
    for line in input.split('\n'):
        rows = [x for x in line if line != '']
        data.append(rows)
    return data 


@dataclass
class Loc:
    row: int 
    col: int

    def __add__(self, other):
        if '|':
            return Loc(other.row + 



@dataclass 
class Data:
    data = []

    def append(self, elem):
        self.data.append(elem)

    def __iter__(self):
        ''' return the row, column, char '''
        for i, row in enumerate(self.data):
            for j, char in enumerate(row):
                yield i, j, char

    def print(self):
        ''' pretty printer '''
        ## Print column header
        length = len(self.data[0])
        str = '\n  R || '
        for i in range(length):
            str += f'{i} '
        print(str)
        print(f"  ==||=={'==' * length}")
        # print the rows
        for i, row in enumerate(self.data):
            if len(row) == 0: 
                continue
            str = f'  {i} || '
            for j, char in enumerate(row):
                str += f'{char} '
            print(str)
        print()

