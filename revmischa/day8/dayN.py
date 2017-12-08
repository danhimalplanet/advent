import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pyparsing import Word, Literal, nums, Optional, alphas, Combine
from collections import namedtuple, defaultdict
from typing import Dict, List
import operator


class Instruction(namedtuple('Instruction', ['operand', 'operator', 'magnitude', 'conditional_lhs', 'comparator', 'conditional_rhs'])):
    pass


class InstructionParser(object):
    def __init__(self):
        """Parser for instruction.

        Example:
            v inc 491 if z >= -1
        """
        # register
        reg = Word(alphas)

        # operator
        inc = Literal("inc")
        dec = Literal("dec")
        op = inc | dec

        # number
        ints = Word(nums)
        plusorminus = Literal('+') | Literal('-')
        integer = Combine(Optional(plusorminus) + ints)

        # comparison op
        comparator = Word('=' + '<' + '>' + '!')

        # pattern build
        self._pattern = reg + op + integer + Literal("if").suppress() + reg + comparator + integer

    def parse(self, line: str) -> Instruction:
        # print(f"line: '{line}'")
        parsed = self._pattern.parseString(line, parseAll=True)
        return Instruction(
            operand=parsed[0],
            operator=parsed[1],
            magnitude=int(parsed[2]),
            conditional_lhs=parsed[3],
            comparator=parsed[4],
            conditional_rhs=int(parsed[5]),
        )

parser = InstructionParser()


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.regs: Dict[str, int] = defaultdict(int)
        self.instructions: List[Instruction] = structure
        self.largest = 0

    @classmethod
    def parse_input(cls, input_str: str):
        """Convert input to a list of strings"""
        parsed = list(
            map(
                parser.parse,
                filter(lambda n: n is not None and n is not "",
                       input_str.split('\n'))
            )
        )
        return parsed

    def step(self, inst: Instruction) -> None:
        self.update_max()
        # do compare
        lhs = inst.conditional_lhs
        rhs = inst.conditional_rhs
        reg = inst.operand

        # look up value of lhs
        lhs_val = self.regs[lhs]

        ops = {
            '<': operator.lt,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne,
            '>=': operator.ge,
            '>': operator.gt
        }

        comp = inst.comparator
        if comp not in ops:
            raise Exception(f"unknown comparator {comp}")

        op = ops[comp]
        res = op(lhs_val, int(rhs))
        if not res:
            return

        # comparison true
        if inst.operator == 'inc':
            self.regs[reg] += inst.magnitude
        elif inst.operator == 'dec':
            self.regs[reg] -= inst.magnitude
        else:
            raise Exception(f"unknown operator {inst.operand}")
        self.update_max()

    def update_max(self):
        vals = self.regs.values()
        if not vals:
            return
        curmax = max(vals)
        if curmax > self.largest:
            self.largest = curmax

    def run_part1(self):
        for inst in self.instructions:
            self.step(inst)

        vals = self.regs.values()
        return max(vals)

    def run_part2(self):
        for inst in self.instructions:
            self.step(inst)
        return self.largest

if __name__ == '__main__':
    main(DayN)
