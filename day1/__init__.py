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
    results = []
    col1, col2 = parse(input)
    for i in col1:
        count = 0
        for j in col2:
            if i == j:
                count += 1
        results.append(i * count)
    return sum(results)


def solve_part_one(input):
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
