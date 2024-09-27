import unittest
from solve import *
from pprint import pprint


class Units(unittest.TestCase):
    def test_card_rank(self):
        assert card_rank("A") == 14
        assert card_rank("K") == 13
        assert card_rank("2") == 2
        assert card_rank("3") == 3

    def test_hand_type(self):
        hands = {
            "22222": FIVEKND,
            "AAJJJ": FULLHSE,
            "23333": FOURKND,
            "22333": FULLHSE,
            "A2JJJ": THREEKND,
            "AA5JJ": TWOPAIR,
            "AA52J": ONEPAIR,
            "A45QJ": HIGHCARD,
        }
        for hand, correct_type in hands.items():
            entry = Entry(hand)
            assert entry.type == correct_type

    def test_hand_rank(self):
        hands = {
            "33333": "3333A",
            "AAJJJ": "AA2TT",
            "22333": "33A22",
            "22A33": "25T33",
            "A24JJ": "JATQ9",
        }
        for gt, lt in hands.items():
            a = Entry(gt).rank
            b = Entry(lt).rank
            if not a > b:
                print("Hand Rank Not Greater than.")
                print("HANDS:", gt, lt, "RANKS:", a,b)
                raise AssertionError

    def _test_hand_rank_level2(self):
        hands = {
            "44444": "33333",
            "A4444": "A3333",
            "A3333": "Q4444",
        }
        for gt, lt in hands.items():
            a = Entry(gt)
            b = Entry(lt)
            if not a > b:
                print("Matching Hand Rank Not Greater than.")
                print(a,b)
                raise AssertionError

class Sample(unittest.TestCase):
    def test_sample(self):
        raw = load_file(SAMPLE)
        data = parse(raw)
        types = classify(data)
        ordered = order(types)
        result = rank_and_solve(ordered)
        assert result == 6440

class Part1(unittest.TestCase):
    def test_part1(self):
        raw = load_file(INPUT)
        data = parse(raw)
        types = classify(data)
        ordered = order(types)
        result = rank_and_solve(ordered)
        print(result)

if __name__ == '__main__':
    unittest.main()
