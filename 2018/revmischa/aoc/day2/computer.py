import os
import sys
from collections import Counter, defaultdict
from typing import Dict, Set


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint


class Day2(Computer):
    pwd = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.input = structure

    @classmethod
    def lambda_handler(cls, event):
        """Entry point for distributed computations."""
        arg = event['arg']
        return f"got event {arg}"

    @classmethod
    def parse_input(cls, input_str: str):
        return input_str.splitlines()

    def run_part1(self):
        repeat_2 = 0
        repeat_3 = 0
        for line in self.input:
            c = Counter(line)
            repeats: Dict[int, Set] = defaultdict(set)
            [repeats[count].add(char) for char, count in c.items()]
            if repeats[2]:
                repeat_2 += 1
            if repeats[3]:
                repeat_3 += 1

        return repeat_2 * repeat_3

    def run_part2(self):
        seen = []
        last = None
        for line in self.input:
            matcher = [s for s in seen if self.diff_count(s, line) == 1]
            if matcher:
                print(matcher)
                print(line)
                return ''.join(sorted(set(matcher[0]) & set(line)))
            seen.append(line)

    def diff_count(self, str1, str2) -> int:
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return diff

if __name__ == '__main__':
    print(Day2.part1_result(debug=False))
    print(Day2.part2_result(debug=False))
