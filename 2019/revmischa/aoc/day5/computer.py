import os
import sys

PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401

POSITION = 0
IMMEDIATE = 1

ADD = 1
MUL = 2
IN = 3
OUT = 4
JNZ = 5
JZ = 6
LT = 7
EQ = 8
EXIT = 99

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
    EXIT: 0,
}


class Day5(Computer):
    pwd: str = PWD

    def __init__(self, structure, inputs, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.orig_mem = structure
        self.inputs = inputs
        self.outputs = []
        self.prev_op = 0

    @classmethod
    def parse_input(cls, input_str: str):
        print("str", input_str)
        return [int(i) for i in input_str.split(",")]

    def run_program(self, orig_mem):
        self.pc = 0
        mem = [*orig_mem]
        while True:
            # import ipdb; ipdb.set_trace()
            pc = self.pc
            op = mem[pc]
            if op in OPERAND_COUNT:  # simple op code
                operand_count = OPERAND_COUNT[op]
                # make list of parameters to operation
                # print("op", op, mem[pc + 1 : pc + operand_count + 1])
                operands = [mem[mem[pc + 1 + i]] for i in range(operand_count - 1)]
                if operand_count:
                    operands.append(mem[pc + operand_count])
                # print("operands", operands)
                self.eval(mem, op, operands)
            else:
                # assume it is an immediate-mode op
                chars = str(op)
                # print("immediate", chars)
                # get opcode
                op = int(chars[-2:])
                params = chars[:-2]
                # set param modes
                operand_count = OPERAND_COUNT[op]
                while len(params) < operand_count:
                    params = f"0{params}"  # left-pad with 0s
                # gather operands
                operands = []
                for idx in range(operand_count):
                    val = mem[self.pc + 1 + idx]
                    mode = int(params[operand_count - 1 - idx])  # 0 or 1, pos or imm
                    # print(
                    #     "idx",
                    #     idx,
                    #     "chars",
                    #     chars,
                    #     mem[self.pc + 1 + idx],
                    #     "operand count",
                    #     operand_count,
                    # )
                    if (
                        mode == IMMEDIATE or (idx == operand_count - 1 and op not in (JNZ, JZ))
                    ):  # final op (dest) should be address
                        # print("immediate , idx=", idx, "params=", params)
                        operands.append(val)
                    else:
                        # print("positional, idx=", idx, "params=", params)
                        operands.append(mem[val])
                print("chars", chars, "op", op, "params", params, "mem", mem[pc+1:pc+1+operand_count], "operands", operands)
                self.eval(mem, int(op), operands)

            if op == EXIT:
                return

            self.prev_op = op

    def eval(self, mem, op, o):
        print("eval", op, o)
        operand_count = OPERAND_COUNT[op]

        if op == ADD:  # 1
            # add
            mem[o[2]] = o[0] + o[1]
            # print(f"mem[{o[2]}]={mem[o[2]]}")
        elif op == MUL:  # 2
            # mul
            mem[o[2]] = o[0] * o[1]
            # print(f"mem[{o[2]}]={mem[o[2]]}")
        elif op == IN:  # 3
            # input
            print("input, operand=", o[0], "mem=", mem[o[0]])
            mem[o[0]] = self.inputs[0]
            # print(f"mem[{o[0]}]={mem[o[0]]}")
        elif op == OUT:  # 4
            # output
            print("output, operand=", o[0], "mem=", mem[o[0]])
            self.outputs.append(mem[o[0]])
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
        elif op == EXIT:  # 99
            print("last op", self.prev_op)
            if self.prev_op != 4:
                raise Exception("Did not output before halting")
        else:
            raise Exception(f"unknown op {op}")

        self.pc += 1 + operand_count

    def run_part1(self):
        self.run_program(self.orig_mem)
        return self.outputs

    def run_part2(self):
        self.run_program(self.orig_mem)
        return self.outputs


if __name__ == "__main__":
    print(Day5.part1_result(inputs=[1], debug=False))
    print(Day5.part2_result(inputs=[5], debug=False))
