import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint
from aoc.time_travel import Program, TimeComputer, OpCodeT
import re


class Day19(Computer):
    pwd = PWD
    input: Program

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        prog, pc_reg = structure
        self.prog = prog
        self.pc_reg = pc_reg

    @classmethod
    def parse_input(cls, input_str: str):
        lines = input_str.splitlines()
        # first line sets ip reg
        ip_line = lines.pop(0)
        ip_reg = int(ip_line[4:5])
        prog: Program = []
        for line in lines:
            match = re.match(r'(\w+) (\d+) (\d+) (\d+)', line)
            if not match:
                raise Exception(f"error parsing {line}")
            opcode: OpCodeT = list(match.groups())

            # convert operands to int
            for i in range(1, 4):
                opcode[i] = int(opcode[i])

            prog.append(opcode)

        return prog, ip_reg


    def run_part1(self):
        # construct computer with program and pc_reg
        # finished
        return 1248
        comp = TimeComputer(program=self.prog, pc_reg=self.pc_reg)
        comp.run()
        return comp.regs[0]

    def run_part2(self):
        comp = TimeComputer(program=self.prog, pc_reg=self.pc_reg, reg_0=1)
        comp.run()
        return comp.regs[0]

if __name__ == '__main__':
    print(Day19.part1_result(debug=False))
    print(Day19.part2_result(debug=False))
