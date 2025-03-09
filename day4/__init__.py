SAMPLE_1 = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

SAMPLE_2 = """\
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""

PART_1_SAMPLE_ANSWER = 18
PART_2_SAMPLE_ANSWER = 9

DAY_PATH = __file__
X = "X"
XMAS = "XMAS"


from utils import debug, set_debug, load_input_file
import unittest


def solve_part_two(input, _debug=True):
    set_debug(_debug)
    data = parse(input)
    grid = Grid(data)
    count = 0
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col != "A":
                continue
            diag1 = grid.diag_1(i, j)
            diag2 = grid.diag_2(i, j)
            if diag1 in ['MAS','SAM']:
                if diag2 in ['MAS','SAM']:
                    debug(f" match: {i},{j}")
                    count += 1
            # TODO: find MAS in an X pattern going in
            # either direction.

    debug(f"COUNT: {count}")
    return count
    return None




def solve_part_one(input, _debug=False):
    set_debug(_debug)
    data = parse(input)
    grid = Grid(data)
    # grid.pprint()
    count = 0
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col != X:
                continue
            for dir, fn in grid.directions.items():
                out = fn(i, j)
                if out == "XMAS":
                    count += 1
                    # debug(f'{count}) {dir} [{i},{j}]')
    debug(f"COUNT: {count}")
    return count


class Grid:
    """Grid calculator."""

    def __init__(self, data):
        self.data = data
        # all possible direction calculators
        self.directions = {
            "UP": self.up,
            "DOWN": self.down,
            "UP LEFT": self.up_left,
            "UP RIGHT": self.up_right,
            "DOWN LEFT": self.down_left,
            "DOWN RIGHT": self.down_right,
            "RIGHT": self.right,
            "LEFT": self.left,
        }

    def diag_1(self, i, j):
        top_right = self.grid(i-1, j+1)
        bottom_left = self.grid(i+1, j-1)
        return top_right + 'A' + bottom_left

    def diag_2(self, i, j):
        top_left = self.grid(i-1, j-1)
        bottom_right = self.grid(i+1, j+1)
        return top_left + 'A' + bottom_right

    def up(self, i, j):
        str = "X"
        for x in range(1, 4):
            str += self.grid(i - x, j)
        return str

    def down(self, i, j):
        str = "X"
        for x in range(1, 4):
            str += self.grid(i + x, j)
        return str

    def up_left(self, i, j):
        str = "X"
        for x in range(1, 4):
            str += self.grid(i - x, j - x)
        return str

    def up_right(self, i, j):
        str = "X"
        for x in range(1, 4):
            str += self.grid(i - x, j + x)
        return str

    def down_left(self, i, j):
        str = "X"
        for x in range(1, 4):
            str += self.grid(i + x, j - x)
        return str

    def down_right(self, i, j):
        str = "X"
        for x in range(1, 4):
            str += self.grid(i + x, j + x)
        return str

    def right(self, i, j):
        str = "X"
        for x in range(1, 4):
            str += self.grid(i, j + x)
        return str

    def left(self, i, j):
        str = "X"
        for x in range(1, 4):
            str += self.grid(i, j - x)
        return str

    def grid(self, i, j):
        """
        safe grid access.
        prevent out of bounds & negative values
        """
        if i < 0 or j < 0:
            return ""
        try:
            return self.data[i][j]
        except IndexError:
            return ""

    def pprint(self):
        print()
        colsize = len(self.data[0])
        str = "    "
        for x in range(colsize):
            str += f"{x} "
        for i, row in enumerate(self.data):
            str += f"\n {i}) "
            for j, col in enumerate(row):
                str += col + " "
        print(str)


def parse(input):
    data = []
    for row in input.split("\n"):
        if row == "":
            continue
        cols = [x for x in row]
        data.append(cols)
    return data


class Sample(unittest.TestCase):
    def test_sample_one(self):
        """Test Sample One"""
        result = solve_part_one(SAMPLE_1)
        assert result == PART_1_SAMPLE_ANSWER

    def test_sample_two(self):
        """Test Sample Two"""
        result = solve_part_two(SAMPLE_1)
        assert result == PART_2_SAMPLE_ANSWER


test = unittest.main
