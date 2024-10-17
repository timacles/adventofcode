import unittest
from solve import *
from pprint import pprint



class Part2(unittest.TestCase):
    def test_part2_try1(self):
        pass
        #result = solve_part2(INPUT)
        #result = solve_part2(SAMPLE3)

    def test_part2(self):
        #result = solve_part2(INPUT)
        result = solve_part2_try2(INPUT)
        #result = solve_part2(SAMPLE3)
        print(f"\n=== Part2 ===\n")
        print(f" - Result: {result}")
        assert result == 18625484023687

class Sample3(unittest.TestCase):
    def test_part1(self):
        result = solve_part2(SAMPLE3)
        print(result)

class Part1(unittest.TestCase):
    def test_part1(self):
        result = solve_part1(INPUT)
        print(result)

class Sample1(unittest.TestCase):
    def test_sample1(self):
        assert solve_part1(SAMPLE1) == 2

    def test_sample2(self):
        assert solve_part1(SAMPLE2) == 6
    
class Generator(unittest.TestCase):
    def test_gen(self):
        raw = load_file(SAMPLE3) 
        data = parse(raw)
        for inst in data.next_instr():
            print(inst)
        
if __name__ == '__main__':
    unittest.main()
