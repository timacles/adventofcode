SAMPLE_1 ="""\
3   4
4   3
2   5
1   3
3   9
3   3
"""


DAY_PATH = __file__


from utils import debug, load_input_file


def solve_part_two(input):
    print("\n*** PART -TWO- ***")
    results = []
    col1, col2 = parse(input)
    for i in col1:
        count = 0
        for j in col2:
            if i == j:
                count += 1
        results.append(i * count)
    result = sum(results)
    print(f"  ==> PART -TWO- RESUlT: [[ {result} ]]")
    return result


def solve_part_one(input):
    print("\n*** PART -ONE- ***")
    col1, col2 = parse(input)
    col1 = sorted(col1)
    col2 = sorted(col2)
    diffs = []
    debug(f"{col1} {col2}")
    for i in range(0, len(col1)):
        a = col1[i]
        b = col2[i]
        diff = abs(a - b)
        debug(f"{i}) {a} - {b} :: {diff}")
        diffs.append(diff)
    result = sum(diffs)
    print(f"  ==> PART -ONE- RESUlT: [[ {result} ]]")
    return sum(diffs)

def parse(input):
    col1 = []
    col2 = []
    for line in input.split("\n"):
        if line == '': continue
        a, b = line.split("   ")
        col1.append(int(a))
        col2.append(int(b))
    return col1, col2

def solve():
    input = load_input_file(DAY_PATH)
    solve_part_one(input)
    solve_part_two(input)

