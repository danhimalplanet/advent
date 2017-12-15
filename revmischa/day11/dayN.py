import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
import math


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure
        self.cx = 0
        self.cy = 0
        self.maxdist = 0

    @classmethod
    def parse_input(cls, i):
        return i.split(',')

    def step(self, d):
        diag = .5
        if d == 'n':
            self.cy += 1
        elif d == 'ne':
            self.cx += diag
            self.cy += diag
        elif d == 'se':
            self.cx += diag
            self.cy -= diag
        elif d == 's':
            self.cy -= 1
        elif d == 'sw':
            self.cx -= diag
            self.cy -= diag
        elif d == 'se':
            self.cx += diag
            self.cy -= diag
        elif d == 'nw':
            self.cx -= diag
            self.cy += diag
        else:
            raise Exception(f"unknown direction '{d}'")
        if self.distance() > self.maxdist:
            self.maxdist = self.distance()

    def distance(self):
        return abs(self.cx) + abs(self.cy)

    def run_part1(self):
        for s in self.input:
            self.step(s)
        print(f"cx: {self.cx}, cy: {self.cy}")
        return self.distance()

    def run_part2(self):
        for s in self.input:
            self.step(s)
        return self.maxdist

if __name__ == '__main__':
    main(DayN)
