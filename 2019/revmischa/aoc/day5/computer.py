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


class Day5(Computer):
    pwd: str = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.orig_mem = structure
        self.inputs = [1]
        self.outputs = []
        self.prev_op = 0

    @classmethod
    def parse_input(cls, input_str: str):
        return [int(i) for i in input_str.split(",")]

    def run_program(self, orig_mem):
        self.pc = 0
        mem = [*orig_mem]
        while True:
            pc = self.pc
            op = mem[pc]
            op1 = mem[pc + 1]
            if op >= 1 and op <= 2:
                op2 = mem[pc + 2]
                op3 = mem[pc + 3]
                self.eval(mem, op, mem[op1], mem[op2], op3)
            elif op == 3 or op == 4:
                self.eval(mem, op, op1)

            # elif op == 3:
            #     # input
            #     mem[op1] = self.inputs[0]
            #     self.pc += 2
            # elif op == 4:
            #     # output
            #     val = mem[op1]
            #     if val != 0:
            #         raise Exception()
            #     self.outputs.append(val)
            #     self.pc += 2
            elif op == 99:
                print("last op", self.prev_op)
                if self.prev_op != 4:
                    raise Exception("Did not output before halting")
                return mem
            else:
                # assume it is an immediate-mode op
                chars = str(op)
                print("immediate", chars)
                # get opcode
                op = int(chars[-2:])
                if op > 4:
                    raise Exception(f"unexpected op: {chars}")
                params = chars[:-2]
                # get count of operands
                is_io = op == 3 or op == 4
                op_count = 1 if is_io else 3
                # set param modes
                while len(params) < op_count:
                    params = f"0{params}"  # left-pad with 0s
                # gather operands
                operands = []
                for idx in range(op_count):
                    val = mem[self.pc + 1 + idx]
                    mode = int(params[op_count - 1 - idx])  # 0 or 1, pos or imm
                    # print("idx", idx, "chars", chars, mem[self.pc + 1 + idx])
                    if op == 3 or mode == IMMEDIATE:
                        # print("immediate , idx=", idx, "params=", params)
                        operands.append(val)
                    else:
                        # print("positional, idx=", idx, "params=", params)
                        operands.append(mem[val])
                # print("chars", chars, "op", op, "params", params, "operands", operands)
                self.eval(mem, int(op), *operands)

            self.prev_op = op

    def eval(self, mem, op, *operands):
        print("eval ", op, operands)
        if op == 1:
            # add
            mem[operands[2]] = operands[0] + operands[1]
            print(f"mem[{operands[2]}]={mem[operands[2]]}")
            self.pc += 4
        elif op == 2:
            # mul
            mem[operands[2]] = operands[0] * operands[1]
            print(f"mem[{operands[2]}]={mem[operands[2]]}")
            self.pc += 4
        elif op == 3:
            # input
            print("input, operand=", operands[0], "mem=", mem[operands[0]])
            mem[operands[0]] = self.inputs[0]
            self.pc += 2
        elif op == 4:
            # output
            print("output, operand=", operands[0], "mem=", mem[operands[0]])
            self.outputs.append(operands[0])
            self.pc += 2

        else:
            raise Exception(f"unknown op {op}")

    def run_part1(self):
        self.run_program(self.orig_mem)
        return self.outputs

    def run_part2(self):
        return 0


if __name__ == "__main__":
    print(Day5.part1_result(debug=False))
    print(Day5.part2_result(debug=False))
