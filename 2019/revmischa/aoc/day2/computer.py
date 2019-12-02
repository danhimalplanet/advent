import os
import sys

PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint


class Day2(Computer):
    pwd = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.orig_mem = structure

    @classmethod
    def lambda_handler(cls, event):
        """Entry point for distributed computations."""
        arg = event["arg"]
        return f"got event {arg}"

    @classmethod
    def parse_input(cls, input_str: str):
        return [int(i) for i in input_str.split(",")]

    def run_program(self, orig_mem):
        self.pc = 0
        mem = [*orig_mem]
        while True:
            pc = self.pc
            op = mem[pc]
            if op == 1:
                # add
                mem[mem[pc + 3]] = mem[mem[pc + 1]] + mem[mem[pc + 2]]
                self.pc += 4
            elif op == 2:
                # mul
                mem[mem[pc + 3]] = mem[mem[pc + 1]] * mem[mem[pc + 2]]
                self.pc += 4
            elif op == 99:
                return mem
            else:
                raise Exception(f"unknown opcode {op}")

    def run_part1(self):
        return self.run_program(self.orig_mem)

    def run_part2(self):
        target = 19690720
        noun = 0
        out = 0
        while noun < 100:
            verb = 0
            while verb < 100:
                out = self.run_with(noun=noun, verb=verb)
                if out[0] == target:
                    return 100 * noun + verb
                verb += 1
            noun += 1
        return -1

    def run_with(self, noun, verb):
        mem = [*self.orig_mem]
        mem[1] = noun
        mem[2] = verb
        return self.run_program(mem)


if __name__ == "__main__":
    print(Day2.part1_result(debug=False))
    print(Day2.part2_result(debug=False))
