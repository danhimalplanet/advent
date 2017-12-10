import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pyparsing import Suppress, Group, OneOrMore, ZeroOrMore, CharsNotIn, Forward, Optional, Regex, nestedExpr, NoMatch, Literal, printables, Word, OnlyOnce, SkipTo
import re


class Parser(object):
    def __init__(self):
        """Parser for instruction.

        Example:
            {{<a>},{<a>},{<a>},{<a>}}
            {{<!>},{<!>},{<!>},{<a>}}
            <{o"i!a,<{i<a>
        """
        debug = False
        self.garbo_count = 0

        LBRACK, RBRACK, LBRACE, RBRACE, BANG = map(Suppress, "<>{}!")
        nonspecial = CharsNotIn('<>{}!')
        ignored = Word('!', printables, exact=2)
        enclosed_garbo = SkipTo(Literal('>'), ignore=ignored)

        val_str = Forward()
        garbo_str = Forward()
        item = Forward()

        # a parsed item
        item = (ignored | garbo_str | val_str | nonspecial).setDebug(debug)

        # stuff in {}s
        val_str << nestedExpr('{', '}', content=item, ignoreExpr=None).setDebug(debug)
        # stuff in <>s (suppressed)
        garbo_str << (LBRACK + Optional(enclosed_garbo) + RBRACK).setDebug(debug)

        def cvt_list(toks):
            return toks.asList()
        val_str.setParseAction(cvt_list)

        def take_garbo(s, loc, toks):
            m = toks[0]
            ig_str = re.sub(r'!.', '', m)
            ln = len(ig_str)
            self.garbo_count += ln
            return f"<GARBO: {ln}>"

        enclosed_garbo.setParseAction(take_garbo)
        ignored.setParseAction(lambda: '!IGNORED')

        # pattern build
        self._pattern = item

    def parse(self, line: str):
        self.garbo_count = 0
        parsed = self._pattern.parseString(line, parseAll=True)
        # print(f"parsed: {parsed}")
        return parsed

parser = Parser()


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.parsed = structure
        self.garbo_count = 0

    @classmethod
    def parse_input(cls, input_str: str):
        """Convert input to a list of strings."""
        return parser.parse(input_str)

    def run_part1(self):
        def des(parsed, depth):
            res = 0
            # print(f"DEPTH: {depth} CUR: {parsed}")
            for p in parsed:
                # print(f"type({p}): {type(p)}")
                if type(p) is list:
                    # print("found list")
                    res += depth + des(p, depth + 1)
            return res
        # return 1
        return des(self.parsed, 1)

    def run_part2(self):
        return parser.garbo_count

if __name__ == '__main__':
    main(DayN)
