import itertools
import os
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue, Empty
from typing import Optional
import numpy as np


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401
from typing import List

# arg modes
POSITION = 0
IMMEDIATE = 1
RELATIVE = 2

ADD = 1
MUL = 2
IN = 3
OUT = 4
JNZ = 5
JZ = 6
LT = 7
EQ = 8
OFFSET = 9
EXIT = 99

DIRECT_MEM_OPS = (ADD, MUL, LT, EQ, IN)  # ops that take a pointer as last operand

# mapping of operation to number of parameters
OPERAND_COUNT = {
    ADD: 3,
    MUL: 3,
    IN: 1,
    OUT: 1,
    JNZ: 2,
    JZ: 2,
    LT: 3,
    EQ: 3,
    OFFSET: 1,
    EXIT: 0,
}


class Day9(Computer):
    pwd: str = PWD
    inputs: Optional[List[int]]
    outputs: List[int]
    prev_op: int
    halted: bool = False
    base: int

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.orig_mem = structure
        self.mem = np.zeros(100000000, dtype=int)
        for i in range(len(self.orig_mem)):
            self.mem[i] = self.orig_mem[i]
        self.prev_op = 0
        self.base = 0

    @classmethod
    def parse_input(cls, input_str: str):
        return [int(i) for i in input_str.split(",")]

    def run_program(self, inputs: List[int] = [1]):
        self.pc = 0
        self.outputs = []
        self.inputs = inputs
        self.halted = False
        mem = self.mem
        done = False
        self.debug("\nSTART\n")
        while not done:
            pc = self.pc
            op = mem[pc]
            if op in OPERAND_COUNT:  # simple op code
                operand_count = OPERAND_COUNT[op]
                # make list of parameters to operation
                operands = [mem[mem[pc + 1 + i]] for i in range(operand_count - 1)]
                if operand_count:
                    # last value maybe immediate?
                    val = mem[pc + operand_count]
                    if op not in DIRECT_MEM_OPS:
                        val = mem[val]
                    operands.append(val)
                self.eval(mem, op, operands)
            else:
                # immediate or relative immediate
                chars = str(op)
                # get opcode
                op = int(chars[-2:])
                params = chars[:-2]
                self.debug(op, params)
                # set param modes
                operand_count = OPERAND_COUNT[op]
                while len(params) < operand_count:
                    params = f"0{params}"  # left-pad with 0s
                # gather operands
                operands = []
                for idx in range(operand_count):
                    val = mem[self.pc + 1 + idx]
                    mode = int(
                        params[operand_count - 1 - idx]
                    )  # 0 or 1 or 2, pos or imm or rel
                    self.debug("op", op, "mode", mode, "val", val)
                    if mode == RELATIVE:
                        self.debug("rel", val, self.base, operands, "pc", self.pc)
                        operands.append(mem[val + self.base])
                    elif mode == IMMEDIATE or (
                        idx + 1 == operand_count and op in DIRECT_MEM_OPS
                    ):
                        operands.append(val)
                    else:
                        operands.append(mem[val])
                # self.debug("chars", chars, "op", op, "params", params, "mem", mem[pc+1:pc+1+operand_count], "operands", operands)
                self.eval(mem, int(op), operands)

            if op == EXIT:
                self.halted = True
                done = True

            self.prev_op = op

            if pc >= len(mem):
                raise Exception("END?")

        return self.outputs

    def eval(self, mem, op, o):
        self.debug("eval", op, o)
        operand_count = OPERAND_COUNT[op]

        if op == ADD:  # 1
            # add
            mem[o[2]] = o[0] + o[1]
        elif op == MUL:  # 2
            # mul
            mem[o[2]] = o[0] * o[1]
        elif op == IN:  # 3
            # input
            val = self.inputs.pop(0)
            mem[o[0]] = val
        elif op == OUT:  # 4
            # output
            val = o[0]
            # self.debug("output", val, mem[val])
            self.outputs.append(val)
        elif op == JNZ:  # 5
            if o[0] != 0:
                self.pc = o[1]
                return
        elif op == JZ:  # 6
            if o[0] == 0:
                self.pc = o[1]
                return
        elif op == LT:  # 7
            mem[o[2]] = 1 if o[0] < o[1] else 0
        elif op == EQ:  # 8
            mem[o[2]] = 1 if o[0] == o[1] else 0
        elif op == OFFSET:  # 9
            self.base += o[0]
            self.debug("new base", self.base)
        elif op == EXIT:  # 99
            pass
        else:
            raise Exception(f"unknown op {op}")

        self.pc += 1 + operand_count

    def run_part1(self):
        return self.run_program()

    def run_part2(self):
        return 0


if __name__ == "__main__":
    print(Day9.part1_result(debug=False))
    print(Day9.part2_result(debug=False))
