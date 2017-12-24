import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer
from pprint import pprint
from collections import defaultdict, OrderedDict
from typing import Dict, List, Any
from time import sleep


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure, a_init=0):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure
        self.regs: List[tuple] = defaultdict(int)
        self.regs['a'] = a_init
        self.a_init = a_init
        self.pc = 0
        self.mul_count = 0
        self.inst_exec_count: Dict[str, int] = OrderedDict()
        self.jumps_taken: Dict[str, int] = defaultdict(int)

    def __getitem__(self, reg):
        if reg not in list('abcdefgh'):
            raise Exception(f"invalid register {reg}")
        if reg in self.regs:
            return self.regs[reg]
        return 0

    def __setitem__(self, reg, val):
        if reg not in list('abcdefgh'):
            raise Exception(f"invalid register {reg}")
        self.regs[reg] = val

    @classmethod
    def parse_input(cls, input_str: str):
        lines = input_str.split("\n")
        insts = []
        for line in lines:
            code = line.split(' ')
            op: str = code[0]
            reg: str = code[1]

            if not reg.isalpha():
                reg = int(reg)

            operand: Any = None
            if len(code) == 3:
                if code[2].isalpha():
                    operand = code[2]
                else:
                    operand = int(code[2])
            insts.append((op, reg, operand))
        return insts

    def run(self):
        count = 0
        for i in range(len(self.input)):
            (op, reg, operand) = self.input[i]
            op_str: str = f"{i}: {op} {reg} {operand}"
            self.inst_exec_count[op_str] = 0
        while self.pc < len(self.input):
            i = self.input[self.pc]
            (op, reg, operand) = i
            op_str: str = f"{self.pc}: {op} {reg} {operand}"
            self.inst_exec_count[op_str] += 1
            if type(operand) is str:
                operand = self[operand]

            # print(f"[{self.p}]  -  {i} reg: {reg}, operand: {operand}")
            # print(f"[{self.p}]  -  {i} reg: {reg}, val: {self[reg]}, operand: {operand}")

            if op == 'set':
                self[reg] = operand
            elif op == 'sub':
                self[reg] = self[reg] - operand
            elif op == 'mul':
                self[reg] = self[reg] * operand
                self.mul_count += 1
            elif op == 'jnz':
                v = self[reg] if type(reg) is str else reg
                self.jumps_taken[op_str] += 0
                if v != 0:
                    self.jumps_taken[op_str] += 1
                    self.pc += operand
                    continue
            elif op == 'jgz':
                # print(f"reg: {reg}, type: {type(reg)}")
                v = self[reg] if type(reg) is str else reg
                self.jumps_taken[op_str] += 0
                if v > 0:
                    self.jumps_taken[op_str] += 1
                    self.pc += operand
                    continue
            else:
                print(f"Unknown op {op}")

            self.pc += 1
            count += 1
            if self.a_init == 1 and count % 500000 == 0:
            # if self.a_init == 1:
                # sleep(.5)
                pprint(self.inst_exec_count)
                pprint(self.regs)
                pprint(self.jumps_taken)
                print(f"h: {self['h']}")
            # if count % 10000000 == 0:
                # break
        print(f"RAN TO END")

    def run_part1(self):
        self.run()
        return self.mul_count

    def run_part2(self):
        self.run()
        # branch if e*d == b
        return self['h']


if __name__ == '__main__':
    # comp1 = DayN.new_from_puzzle_input()
    # print(comp1.run_part1())
    comp2 = DayN.new_from_puzzle_input(a_init=1)
    print(comp2.run_part2())
