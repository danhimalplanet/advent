import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
import numpy as np


class DayN(Computer):
    pwd = PWD

    def __init__(self, stepsize, inserts):
        """Construct solver with puzzle input."""
        super().__init__()
        self.stepsize = stepsize
        self.stepcount = inserts
        self.pos = 0
        # self.buf = np.zeros((self.stepcount + 1, 1), dtype=int)
        self.buf = [0]
        self.length = 1

    def run_part1(self):
        ln = self.length

        def wrap(i):
            if ln == 0:
                return 0
            if i > ln:
                return i % ln
            return i

        for step in range(1, self.stepcount + 1):
            insert_idx = wrap(self.stepsize + self.pos)
            ln += 1
            insert_idx = wrap(insert_idx + 1)
            self.buf.insert(insert_idx, step)
            self.pos = insert_idx

        idx = self.pos + 1
        # print(self.buf)
        return self.buf[idx]

    def run_part2(self):
        self.run_part1()
        for i in self.buf:
            if self.buf[i] == 0:
                return(self.buf[i+1])


if __name__ == '__main__':
    comp1 = DayN(stepsize=324, inserts=2017)
    print(comp1.run_part1())
    # comp1 = DayN(stepsize=324, inserts=50000000)
    comp1 = DayN(stepsize=324, inserts=500000)
    print(comp1.run_part2())
