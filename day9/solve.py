from dataclasses import dataclass
from math import lcm

SAMPLE1 = "sample1.txt"
SAMPLE2 = "sample2.txt"
SAMPLE3 = "sample3.txt"
INPUT = "input.txt"
LEFT = "L"
RIGHT = "R"

def solve_part1(file):
    raw = load_file(file) 
    data = parse(raw)
    return run_lookup(data)

def solve_part2_try2(file):
    raw = load_file(file) 
    data = parse(raw)
    current_nodes = find_starting_nodes(data)
    last_z_values = [None for x in current_nodes]
    counter = 0 
    results = []
    for i, node in enumerate(current_nodes):
        result = calc_distance(data, node)
        results.append(result)
        print(f"  [{i}] : {node} = {result}")
    return lcm(*results)


def solve_part2(file):
    raw = load_file(file) 
    data = parse(raw)
    current_nodes = find_starting_nodes(data)
    last_z_values = [None for x in current_nodes]
    counter = 0 
    for instr in data.next_instr():
        counter += 1
        new_nodes = []
        for node in current_nodes:
            new_node = get_next_node(data, instr, node)
            new_nodes.append(new_node)
        #print(" ==", new_nodes, counter)

        all_z = False
        for i, node in enumerate(new_nodes):
            if node.endswith('Z'):
                last_z_values[i] = {node: counter}
                if i != 0:
                    print(" -", i, last_z_values)
                all_z = True
            else:
                all_z = False
                break
                
        if all_z:
            return counter
        current_nodes = new_nodes

def ends_with_z(arr):
    return all(s.endswith('Z') for s in arr)
        
def get_next_node(data, instr, current_node):
    if instr == LEFT:
        new_node = data[current_node][0]
    elif instr == RIGHT:
        new_node = data[current_node][1]
    return new_node
        
def calc_distance(data, start_node):
    counter = 0 
    current_node = start_node
    for instr in data.next_instr():
        #print(current_node)
        if current_node.endswith("Z"):
            break
        if instr == LEFT:
            current_node = data[current_node][0]
        elif instr == RIGHT:
            current_node = data[current_node][1]
        counter += 1
    return counter

def find_starting_nodes(data):
    nodes = []
    for entry in data.entries:
        if entry.endswith("A"):
            nodes.append(entry)
    return nodes 


def run_lookup(data):
    length = len(data.header)
    counter = 0 
    i = 0
    current = "AAA"
    
    while i != length:
        instr = data.header[i]
        i += 1
        if current == "ZZZ":
            break
        if i == length:
            i = 0
        if instr == LEFT:
            current = data[current][0]
        elif instr == RIGHT:
            current = data[current][1]
        counter += 1 
        #print(f" ({counter}) INSTR: {instr}, curr: {current}")
        #if counter == 10: break

    return counter


def parse_entry(line):
    label, elems = line.split("=")
    left, right = elems.split(", ")
    return label.strip(), left.strip(" ("), right.strip(")")
    
def parse(raw):
    data = Data()
    data.header = raw.pop(0).strip()
    for line in raw:
        line = line.strip()
        if line == '':
            continue
        label, left, right = parse_entry(line)
        data[label] = (left, right)
    return data

class Data:
    header = None
    entries = {}

    def __setitem__(self, key, val):
        self.entries[key] = val

    def __getitem__(self, key):
        return self.entries[key]
    
    def __repr__(self):
        out = self.header + "\n"
        for k, v in self.entries.items():
            out += f"{k} {v}"
        return out

    def next_instr(self):
        while True:
            for instr in self.header:
                yield instr


@dataclass
class Entry:
    label: str
    left: str
    right: str

    def __repr__(self):
        return f"{self.label} ({self.left} {self.right})"

