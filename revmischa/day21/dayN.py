import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
from typing import List, Tuple, Dict
from functools import partial
from concurrent.futures import ThreadPoolExecutor


Pattern = List[str]
Rule = Tuple[Pattern, Pattern]  # (rule in, rule out)
RuleList = List[Rule]  # list of rules


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure: RuleList, iterations: int):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.rules: RuleList = structure
        self.rules_2: RuleList = []
        self.rules_3: RuleList = []
        for rule in self.rules:
            if len(rule[0]) == 2:
                self.rules_2.append(rule)
            elif len(rule[0]) == 3:
                self.rules_3.append(rule)
            else:
                raise Exception("you f'd up")
        self.iterations = iterations
        self.size = 3
        self.pattern: Pattern = ['.#.', '..#', '###']
        self.executor = ThreadPoolExecutor(max_workers=100)
        self.pattern_cache: Dict[str] = {}

    @classmethod
    def parse_input(cls, input_str: str) -> RuleList:
        rules_str = input_str.split("\n")
        rules: RuleList = list()
        for r in rules_str:
            i, o = r.split(' => ')
            rule_in = i.split('/')
            o_rows = o.split('/')

            # a smart thing to do here would be to pre-flip/rotate the rules for faster matching later
            rule_matches = [rule_in, cls.flip_x(rule_in), cls.flip_y(rule_in)]
            rule_matches.append(cls.flip_x(cls.rotate(rule_in)))
            rule_matches.append(cls.flip_y(cls.rotate(rule_in)))
            rule_matches.append(cls.rotate(rule_in))
            rule_matches.append(cls.rotate(cls.rotate(cls.rotate(rule_in))))
            for rule_transformed in rule_matches:
                rules.append((rule_transformed, o_rows))

        return rules

    def subdivide(self) -> Pattern:
        if self.size % 2 == 0:
            # self.pattern = self.subdivide_by(self.pattern, int(max(2, self.size / 2)))
            self.pattern = self.subdivide_by(self.pattern, 2)
        elif self.size % 3 == 0:
            # self.pattern = self.subdivide_by(self.pattern, int(max(3, self.size / 3)))
            self.pattern = self.subdivide_by(self.pattern, 3)
        else:
            raise Exception("can't do math")

    def subdivide_by(self, pattern: Pattern, divisor: int) -> Pattern:
        new_pattern_squares: List[Pattern] = []
        new_size = 0
        new_pattern: Pattern = []

        # divide into nxn segments
        sub_patterns: List[Pattern] = []  # subdivided squares
        for i in range(0, self.size, divisor):
            # get n rows
            sub_pattern_rows = self.pattern[i:i+divisor]
            # print(f"r: {sub_pattern_rows}")
            # get n cols at a time
            sub_pattern: Pattern = []
            for j in range(0, self.size, divisor):
                sub_pattern_cols = [row[j:j+divisor] for row in sub_pattern_rows]
                sub_patterns.append(sub_pattern_cols)
            new_size += divisor + 1

        # rule match / transform
        if divisor == 2:
            rules = self.rules_2
        elif divisor == 3:
            rules = self.rules_3
        else:
            raise Exception("you f'd up")
        apply_partial = partial(self.apply_rules, divisor=divisor, rules=rules)

        new_squares: List[Pattern] = []
        # option I: threaded
        # new_squares = list(self.executor.map(apply_partial, sub_patterns))
        # option II: not threaded
        for sub_pattern_cols in sub_patterns:
            sub_pattern = apply_partial(sub_pattern_cols)
            new_squares.append(sub_pattern)

        # stitch together
        i = 0
        new_row_idx = 0
        new_square_size = None
        for sub_pattern in new_squares:
            new_square_size = len(sub_pattern)
            # print(f"new square size: {new_square_size}")
            for r_i in range(0, new_square_size):
                r_i_ = r_i + new_row_idx
                # print(f"r_i_: {r_i_}")
                if r_i_ not in new_pattern:
                    new_pattern.append('')
                    new_pattern[r_i_] += sub_pattern[r_i]
                    new_pattern_squares.append(sub_pattern)

                i += 1
                # increase rows
                if i % new_size == 0:
                    # print(f"new row increase @ {i}")
                    new_row_idx += new_square_size

        # print("new pattern squares:")
        # print(new_pattern_squares)
        new_pattern = new_pattern[0:new_size]
        # print("new pattern: ")
        # print(new_pattern)

        new_divisor = 3 if divisor == 2 else 3
        self.size = new_size
        print(f"new size: {new_size}, new pattern:")
        # print(new_pattern)

        return new_pattern

    @classmethod
    def flip_x(cls, p: Pattern) -> Pattern:
        return list(reversed(p))

    @classmethod
    def flip_y(cls, p: Pattern) -> Pattern:
        return [''.join(reversed(row)) for row in p]

    @classmethod
    def rotate(cls, p: Pattern) -> Pattern:
        new_rows: Pattern = []
        matrix: List[List[str]] = []
        for row in p:
            matrix.append(list(row))
        # rotate matrix
        # via SO
        rotated = list(zip(*matrix[::-1]))
        for row in rotated:
            new_rows.append(''.join(row))
        return new_rows

    def apply_rules(self, square: Pattern, divisor: int, rules: RuleList):
        square_str = '\n'.join(square)
        if square_str in self.pattern_cache:
            return self.pattern_cache[square_str]
        for rule in rules:
            rule_in, rule_out = rule
            if rule_in == square:
                self.pattern_cache[square_str] = rule_out
                return rule_out
        print("no match:")
        print(square_str)
        raise Exception("i suck")

        return square

    def run_part1(self):
        # print(self.rules)
        # print(self.pattern)
        for i in range(self.iterations):
            self.subdivide()
            # print(self.pattern)
        on = 0
        for r in self.pattern:
            on += r.count('#')
        return on

    def run_part2(self):
        return 0

if __name__ == '__main__':
    print(DayN.part1_result(iterations=5))
    print(DayN.part1_result(iterations=13))
