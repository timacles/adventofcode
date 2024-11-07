SAMPLE1 = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

from dataclasses import dataclass
from utils import load_input_file

def solve_part1(input):
    parse(input)

def parse(input):
    data = []
    for line in input.split('\n'):
        entry = Entry(line.split(' '))
        data.append(entry)
    return data 

@dataclass
class Entry:
    data: list
    steps: list

    def __init(self, data):
        self.data = data
        self.calc_steps()
    
    def calc_steps(self):
        for i in range(len(self.data)):
            if i == 0:
                continue
            step = data[i] - data[i-1]






