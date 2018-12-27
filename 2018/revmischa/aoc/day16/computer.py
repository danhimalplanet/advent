import os
import sys
from collections import defaultdict
from typing import Dict

from aoc.time_travel import OpCode


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint
from aoc.time_travel import ALL_OPCODES, TimeComputer, Regs, OpCodeT
from dataclasses import dataclass
from typing import List, Set
import re


@dataclass
class OpTest:
    regs_before: Regs
    regs_after: Regs
    opcode: OpCodeT

    def candidates(self):
        # try all operations
        ret = []
        for op_type in ALL_OPCODES:
            # check if this op matches test
            op = op_type(self.opcode)
            if op.test(self.regs_before, self.regs_after):
                ret.append(op_type)
        return ret


class Day16(Computer):
    pwd = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.input: List[OpTest] = structure

    @classmethod
    def lambda_handler(cls, event):
        """Entry point for distributed computations."""
        arg = event['arg']
        return f"got event {arg}"

    @classmethod
    def parse_input(cls, input_str: str):
        lines = input_str.splitlines()
        tests = []
        for i in range(0, len(lines), 4):
            if lines[i].startswith('Before'):
                before, op, after, _ = lines[i:i+4]
                # print(f"before: {before}\nafter: {after}\nop:{op}")

                before = list(map(int, re.match(r'Before: \[(\d+), (\d+), (\d+), (\d+)\]', before).groups()))
                after = list(map(int, re.match(r'After: \s*\[(\d+), (\d+), (\d+), (\d+)\]', after).groups()))
                opcode = list(map(int, re.match(r'(\d+) (\d+) (\d+) (\d+)', op).groups()))
                tests.append(OpTest(regs_before=before, regs_after=after, opcode=opcode))
            else:
                print(f"cannot parse input {lines[i]}")

        return tests

    def run_part1(self):
        answers = []
        for op_test in self.input:
            candidates = op_test.candidates()
            # matched 3 or more operations
            if len(candidates) >= 3:
                answers.append(candidates)
        return len(answers)


    def run_part2(self):
        op_candidates: Dict[int, Set[OpCode]] = defaultdict(set)  # op number -> {candidates}
        for op_test in self.input:
            # get all candidates for this opcode
            candidates = op_test.candidates()
            op_id = op_test.opcode[0]
            # add candidates found
            op_candidates[op_id].update(candidates)

        # answer map of op id -> OpCode
        op_mapping: Dict[int, OpCode] = {}

        while len(op_mapping.keys()) != 16:

            for id in range(16):
                candidates = op_candidates[id]
                if len(candidates) == 1:
                    # only one possible answer for this op id
                    op = candidates.pop()
                    print(f"Matched {id} with {op}")
                    op_mapping[id] = op

                    # remove this candidate from all possibilities
                    for candidates in op_candidates.values():
                        if op in candidates:
                            candidates.remove(op)

                # print(f"{id}: {op_candidates[id]}")
        print(op_mapping)

        # now read in test program
        test_prog: List[OpCodeT] = []
        with open(os.path.join(self.__class__.pwd, 'input2')) as testh:
            # parse line
            lines = testh.readlines()
            for line in lines:
                inst = list(map(int, line.split(" ")))
                if not inst:
                    continue
                test_prog.append(inst)

        # now execute
        comp = TimeComputer(program=test_prog)
        comp.run(inst_mapping=op_mapping)
        return comp.regs[0]


if __name__ == '__main__':
    print(Day16.part1_result(debug=False))
    print(Day16.part2_result(debug=False))
