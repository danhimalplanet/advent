import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
import numpy as np
from typing import List, Tuple


Pattern = List[str]
Rule = Tuple[Pattern, Pattern]  # (rule in, rule out)
RuleList = List[Rule]  # list of rules


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure: RuleList, iterations: int):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.rules: RuleList = structure
        self.iterations = iterations
        self.size = 3
        self.pattern: Pattern = ['.#.', '..#', '###']

    @classmethod
    def parse_input(cls, input_str: str) -> RuleList:
        rules_str = input_str.split("\n")
        rules: RuleList = list()
        for r in rules_str:
            i, o = r.split(' => ')
            i_rows = i.split('/')
            o_rows = o.split('/')
            rules.append((i_rows, o_rows))
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
        new_row_idx = 0
        new_square_size = None
        for i in range(0, self.size, divisor):
            # get n rows
            sub_pattern_rows = self.pattern[i:i+divisor]
            print(f"r: {sub_pattern_rows}")
            # get n cols at a time
            sub_pattern: Pattern = []
            for j in range(0, self.size, divisor):
                sub_pattern_cols = [row[j:j+divisor] for row in sub_pattern_rows]
                print(f"[{j}:{j}+{divisor}]sub cols: {sub_pattern_cols}")
                sub_pattern = self.apply_rules(sub_pattern_cols, divisor)

                # update new pattern
                print("new sub pattern:")
                print(sub_pattern)
                new_square_size = len(sub_pattern)
                for r_i in range(0, new_square_size):
                    r_i_ = r_i + new_row_idx
                    print(f"r_i_: {r_i_}")
                    if r_i_ not in new_pattern:
                        new_pattern.append('')
                    new_pattern[r_i_] += sub_pattern[r_i]
                new_pattern_squares.append(sub_pattern)

            # increase rows
            new_row_idx += new_square_size
            new_size += divisor + 1
        print("new pattern squares:")
        print(new_pattern_squares)
        new_pattern = new_pattern[0:new_size]
        print("new pattern: ")
        print(new_pattern)

        new_divisor = 3 if divisor == 2 else 3
        self.size = new_size
        print(f"new size: {new_size}, new pattern:")
        print(new_pattern)

        return new_pattern

    def flip_x(self, p: Pattern) -> Pattern:
        return list(reversed(p))

    def flip_y(self, p: Pattern) -> Pattern:
        return [''.join(reversed(row)) for row in p]

    def rotate(self, p: Pattern) -> Pattern:
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

    def apply_rules(self, square: Pattern, divisor: int):
        square_str = '\n'.join(square)
        for rule in self.rules:
            rule_in, rule_out = rule
            # rule is the wrong size
            desired_rule_len = divisor
            # print(f"desired rule len: {desired_rule_len}, rule in len: {len(rule_in[0])}")
            # print("matching:")
            # print(square_str)
            if len(rule_in[0]) != desired_rule_len:
                continue

            rule_matches = [rule_in, self.flip_x(rule_in), self.flip_y(rule_in)]
            rule_matches.append(self.flip_x(self.rotate(rule_in)))
            rule_matches.append(self.flip_y(self.rotate(rule_in)))
            rule_matches.append(self.rotate(rule_in))
            rule_matches.append(self.rotate(self.rotate(self.rotate(rule_in))))

            for rci in rule_matches:
                # print(f"RC => {rco}")
                # print(rci)
                rc_str = '\n'.join(rci)
                if rc_str == square_str:
                    # matched
                    # print(f"matched rule!")
                    # print(rc_str)
                    # print(square)
                    return rule_out
        print("no match:")
        print(square_str)
        raise Exception()

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
    main(DayN, iterations=5)
