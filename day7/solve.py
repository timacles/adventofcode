from dataclasses import dataclass
from functools import cmp_to_key


SAMPLE = "sample.txt"
INPUT = "input.txt"
CARDS = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2, 1".split(", ")

FIVEKND = "Five Of A Kind"
FOURKND = "Four Of A Kind"
FULLHSE = "Full House"
THREEKND = "Three Of A Kind"
TWOPAIR = "Two Pair"
ONEPAIR = "One Pair"
HIGHCARD = "High Card"

TYPES = [
    HIGHCARD,
    ONEPAIR,
    TWOPAIR,
    THREEKND,
    FULLHSE,
    FOURKND,
    FIVEKND,
]

def rank_and_solve(data):
    i = 0
    vals = []
    for t in TYPES:
        for entry in data[t]:
            i += 1
            win = i * entry.bet
            vals.append(win)
            #print(i, entry, win)
    return sum(vals)

def order(types):
    ordered = {}
    for type, entries in types.items():
        ordered[type] = sorted(entries, key=cmp_to_key(compare))
    return ordered

def compare(entry_a, entry_b):
    for i, card in enumerate(entry_a.hand):
        rank1 = card_rank(card)
        rank2 = card_rank(entry_b.hand[i])
        if rank1 > rank2:
            return 1
        elif rank1 < rank2:
            return -1
    raise Exception(
        f"Unable to determine higher hand"
        f"{entry_a}{entry_b}")

def classify(data):
    out = {k: [] for k in TYPES}
    for entry in data:
        out[entry.type].append(entry)
    return out    
        

@dataclass 
class Entry:
    hand: str
    bet: int = 0
    
    def __post_init__(self):
        self.type = evaluate(self.hand)
        self.rank = TYPES.index(self.type)

    def __repr__(self):
        return "Entry(hand={}, bet={}, type={})".format(
            self.hand, self.bet, self.type)

    def __getitem__(self, idx):
        return self.hand[idx]

            
    
def evaluate(hand):
    counts = enumerate_cards(hand)
    for card, count in counts.items():
        if count == 5:
            return FIVEKND
        elif count == 4:
            return FOURKND
        elif count == 3 and 2 in counts.values():
            return FULLHSE
        elif count == 3:
            return THREEKND
        elif count == 2 and 2 in [y for x, y in counts.items() if x != card]:
            return TWOPAIR
        elif count == 2:
            return ONEPAIR
        else:
            return HIGHCARD
    raise NotImplementedError(f"Card Type Not Found for Eval: `{hand}`")

def enumerate_cards(cards):
    counter = {}
    for card in cards:
        try:
            counter[card] += 1
        except:
            counter[card] = 1
    return {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)}


def card_rank(card):
    return len(CARDS) - CARDS.index(card) 

def parse(raw):
    data = []
    for line in raw:
        cards, bet = line.split(' ')
        entry = Entry(cards, int(bet.strip()))
        data.append(entry)
    return data
    
def calc(elem):
    pass

def load_file(f):
    with open(f) as f:
        data = f.readlines()
    return data
