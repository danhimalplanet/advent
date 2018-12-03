import os
import re
import sys
from collections import defaultdict

from dataclasses import dataclass


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint

@dataclass
class Claim:
    id: int
    x: int
    y: int
    width: int
    height: int

    def intersect_tiles(self, other: 'Claim') -> int:
        # x/y ranges for self
        sxr = range(self.x, self.x + self.width)
        syr = range(self.y, self.y + self.height)

        # x/y ranges for other
        oxr = range(other.x, other.x + other.width)
        oyr = range(other.y, other.y + other.height)

        # have to intersect at least 1 x and 1 y coord
        return (set(sxr) & set(oxr)), (set(syr) & set(oyr))

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __le__(self, other):
        return self.id < other.id
    def __ge__(self, other):
        return self.id > other.id


class Day3(Computer):
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
        in_re = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        claims = []
        # parse input into Claims
        for line in input_str.splitlines():
            match = in_re.match(line)
            parts = map(int, match.groups())
            claims.append(Claim(*parts))
        return claims

    def run_part1(self):
        claims = self.input
        overlaps = defaultdict(dict)
        compared = set()
        found_overlap = set()
        for claim in claims:
            compared.add(claim)
            # look for overlaps, don't compare to self or ones already checked
            for other in [c for c in claims if c != claim and c not in compared]:
                xs, ys = claim.intersect_tiles(other)
                found = False
                for x in xs:
                    for y in ys:
                        found_overlap.add(other)
                        found_overlap.add(claim)
                        overlaps[x][y] = True
        total = 0
        for x, ys in overlaps.items():
            for y in ys:
                total += 1
        print(f"no overlaps: {compared - found_overlap}")
        return total

    def run_part2(self):
        return 0

if __name__ == '__main__':
    print(Day3.part1_result(debug=False))
    print(Day3.part2_result(debug=False))
