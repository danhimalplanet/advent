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

    def __init__(self, structure, size=16, moves=1):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure
        self.moves = moves
        chars = [chr(x) for x in range(ord('a'), ord('a') + size)]
        self.l_ = np.asarray(chars)

    @classmethod
    def parse_input(cls, input_str: str):
        insts = input_str.split(',')
        return insts

    def do_inst(self, inst):
        if inst.startswith('s'):
            spin = int(inst[1:])
            self.spin(spin)
        elif inst.startswith('x'):
            swap_a, swap_b = inst[1:].split('/')
            self.swap_idx(int(swap_a), int(swap_b))
        elif inst.startswith('p'):
            a, b = inst[1:].split('/')
            self.swap_ele(a, b)

    def spin(self, n):
        self.l_ = np.roll(self.l_, n)

    def swap_idx(self, a, b):
        self.l_[b], self.l_[a] = self.l_[a], self.l_[b]

    def index(self, item):
        return next(i for i, x_i in enumerate(self.l_) if x_i == item)

    def swap_ele(self, a, b):
        a = self.index(a)
        b = self.index(b)
        self.l_[b], self.l_[a] = self.l_[a], self.l_[b]

    def __repr__(self):
        r = ""
        for i in self.l_:
            r += str(i)
        return r

    def run_part1(self):
        for inst in self.input:
            self.do_inst(inst)
        return str(self)

    def run_part2(self):
        for _ in range(0, self.moves):
            for inst in self.input:
                self.do_inst(inst)
        return str(self)

if __name__ == '__main__':
    main(DayN, moves=1000000000)
