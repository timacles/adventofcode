SAMPLE_1 ="""\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

SAMPLE_2 = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


PART_1_SAMPLE_ANSWER = 161
PART_2_SAMPLE_ANSWER = 48   

DAY_PATH = __file__


from utils import set_debug, debug, load_input_file
import unittest


def solve_part_two(input):
    set_debug(True)
    parser = Parser(input)
    expressions = parser.parse_part_2()
    debug(f"  RESULT: {expressions}")
    total = 0
    for left, right in expressions:
        total += left * right
        #debug(f"  exp: {left} * {right}")
    return total


MUL = 'mul'
DO = 'do'
DONT = "don't"
LPAR = '('
RPAR = ')'
COMMA = ','
JUNK = 'JUNK'


def solve_part_one(input, dbg=True):
    set_debug(dbg)
    parser = Parser(input)
    expressions = parser.parse_exp()
    total = 0
    for left, right in expressions:
        total += left * right
        #debug(f"  exp: {left} * {right}")
    return total


def parse(input):
    data = []
    tokens = []
    token = None
    i = 0
    return data


class Parser:
    tokens = []

    def __init__(self, input):
        self.input = input
        debug(f"INPUT: {input}")
        self.pos = 0 

    def peek(self):
        if self.pos < len(self.input):
            return self.input[self.pos]
        return None

    def eat(self):
        if self.pos < len(self.input):
            ch = self.input[self.pos]
            self.pos += 1
            return ch
        return None

    def parse_number(self):
        out = ""
        while (ch := self.peek()) is not None and ch.isdigit():
            out += self.eat()
        if out != "":
            return int(out)
        raise ValueError("expected number")

    def parse_identifier(self):
        out = ""
        while (ch := self.peek()) is not None and (ch.isalpha() or ch == "_"):
            out += self.eat()
        return out

    def parse_token(self):
        ''' parses input and returns tokens '''
        while (ch := self.peek()) is not None:
            if ch.isalpha():
                return self.parse_identifier()
            elif ch.isdigit():
                return self.parse_number()
            elif ch in "(),'":
                return self.eat()
            else: 
                return self.eat()

    def parse_part_2(self):
        exps = []
        left = None
        right = None
        flag = True
        while (tok := self.parse_token()) is not None:
            debug(f"  tok: {tok}")
            if is_str(tok) and tok.endswith('do'):
                if self.parse_token() == LPAR: 
                    if self.parse_token() == RPAR: 
                        debug('  toggle on')
                        flag = True
            if tok == "don":
                if self.parse_token() == "'":
                    if self.parse_token() == "t":
                        if self.parse_token() == LPAR: 
                            if self.parse_token() == RPAR: 
                                debug('  toggle off')
                                flag = False
            if not is_mul(tok): continue
            if self.parse_token() != LPAR: continue
            if (left := self.parse_token()) and not is_int(left): 
                continue
            if self.parse_token() != COMMA: continue
            if (right := self.parse_token()) and not is_int(right): 
                continue
            if self.parse_token() != RPAR: continue
            if flag:
                exps.append((left, right))
            #self.pr_debug()
        return exps

    def parse_exp(self):
        exps = []
        left = None
        right = None
        while (tok := self.parse_token()) is not None:
            if not is_mul(tok): continue
            if self.parse_token() != LPAR: continue
            if (left := self.parse_token()) and not is_int(left): 
                continue
            if self.parse_token() != COMMA: continue
            if (right := self.parse_token()) and not is_int(right): 
                continue
            if self.parse_token() != RPAR: continue
            exps.append((left, right))
            self.pr_debug()
        return exps

    def pr_debug(self):
        str = self.input[self.pos - 20:self.pos]
        debug(f" [{self.pos}] BACK TRACK: {str}")
    

def is_str(tok):
    return isinstance(tok, str)

def is_int(tok):
    return isinstance(tok, int)

def is_mul(tok):
    return isinstance(tok, str) and tok.endswith(MUL)



class Sample(unittest.TestCase):
    def test_sample_one(self):
        ''' Test Sample One '''
        result = solve_part_one(SAMPLE_1, False)
        assert result == PART_1_SAMPLE_ANSWER

    def test_sample_two(self):
        ''' Test Sample Two '''
        result = solve_part_two(SAMPLE_2)
        assert result == PART_2_SAMPLE_ANSWER

    def test_edge_1(self):
        '''test incorrect case'''
        #set_debug(True)
        s = "mul(830,184~)"
        parser = Parser(s)
        exp = parser.parse_exp()
        assert len(exp) == 0

test = unittest.main



shift   = lambda inp: bool(inp) and (inp[0], inp[1:])
nothing = lambda inp: (None, inp)
filt = lambda predicate: (
         lambda parser:
           lambda inp: (m:=parser(inp)) and predicate(m[0]) and m)
