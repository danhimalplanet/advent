import itertools
import os
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue, Empty
from typing import Optional


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401
from typing import List

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


class Day7(Computer):
    pwd: str = PWD
    inputs: Optional[List[int]]
    outputs: List[int]
    prev_op: int
    halted: bool = False
    in_q: Optional[Queue]
    out_q: Optional[Queue]

    def __init__(self, structure, in_q: Queue = None, out_q: Queue = None, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.orig_mem = structure
        self.mem = [*self.orig_mem]
        self.prev_op = 0
        self.in_q = in_q
        self.out_q = out_q

    @classmethod
    def parse_input(cls, input_str: str):
        # print("str", input_str)
        return [int(i) for i in input_str.split(",")]

    def run_program(self, orig_mem, inputs: List[int] = None):
        self.pc = 0
        self.outputs = []
        self.inputs = inputs
        self.halted = False
        mem = self.mem
        done = False
        while not done:
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
                    if mode == IMMEDIATE or (
                        idx == operand_count - 1 and op not in (JNZ, JZ)
                    ):  # final op (dest) should be address
                        operands.append(val)
                    else:
                        operands.append(mem[val])
                # print("chars", chars, "op", op, "params", params, "mem", mem[pc+1:pc+1+operand_count], "operands", operands)
                self.eval(mem, int(op), operands)

            if op == EXIT:
                self.halted = True
                done = True

            self.prev_op = op

            if pc >= len(mem):
                raise Exception("END?")

        # assert len(self.outputs) == 1
        return self.outputs[0] if self.outputs else None

    def eval(self, mem, op, o):
        # print("eval", op, o)
        operand_count = OPERAND_COUNT[op]

        if op == ADD:  # 1
            # add
            mem[o[2]] = o[0] + o[1]
        elif op == MUL:  # 2
            # mul
            mem[o[2]] = o[0] * o[1]
        elif op == IN:  # 3
            # input
            if self.in_q:
                # print("read input...")
                val = self.in_q.get()
                # print("read", val)
            else:
                val = self.inputs.pop(0)
            mem[o[0]] = val
        elif op == OUT:  # 4
            # output
            val = mem[o[0]]
            if self.out_q:
                self.out_q.put(val)
                # print("output", val)
            else:
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
        elif op == EXIT:  # 99
            # print("last op", self.prev_op)
            # if self.prev_op != 4:
            # raise Exception("Did not output before halting")
            pass
        else:
            raise Exception(f"unknown op {op}")

        self.pc += 1 + operand_count

    def run_amps(self, phases: List[int]) -> int:
        last_output = 0
        for amp in range(5):
            inputs = [phases[amp], last_output]
            last_output = self.run_program(self.orig_mem, inputs=[*inputs])
        return last_output

    def run_amps_feedback(self, phases: List[int]) -> int:
        last_in = None
        last_out = Queue()
        comps = []
        for a in range(5):
            if last_in:
                last_in.put(phases[a])
            comp = Day7(self.orig_mem, in_q=last_in, out_q=last_out)
            last_in = last_out
            last_out = Queue()
            comps.append(comp)

        # wire last output to first input
        comps[0].in_q = comps[4].out_q
        comps[0].in_q.put(phases[0])
        comps[0].in_q.put(0)

        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.run_computer, comps)

        val = 0
        try:
            while True:
                val = comps[4].out_q.get(block=False)
        except Empty:
            pass
        return val

    def run_computer(self, computer: "Day7"):
        return computer.run_program(orig_mem=self.orig_mem)

    def run_part1(self):
        best_amp = 0
        # test every combination of inputs
        for comb in itertools.permutations(range(5)):
            out = self.run_amps(phases=comb)
            if out > best_amp:
                best_amp = out
        return best_amp

    def run_part2(self):
        best_amp = 0
        # test every combination of inputs
        for comb in itertools.permutations(range(5, 10)):
            out = self.run_amps_feedback(phases=comb)
            # if not out:
            # continue
            if out > best_amp:
                best_amp = out
        return best_amp


if __name__ == "__main__":
    print(Day7.part1_result(debug=False))
    print(Day7.part2_result(debug=False))
