import os
import sys

PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint
import math


class Day1(Computer):
    pwd = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.input = structure

    @classmethod
    def lambda_handler(cls, event):
        """Entry point for distributed computations."""
        arg = event["arg"]
        return f"got event {arg}"

    @classmethod
    def parse_input(cls, input_str: str):
        return Computer.parse_input(input_str)

    def run_part1(self):
        total = 0

        def add_module(module):
            return math.floor(module / 3) - 2

        for module in self.input:
            total += add_module(module)
        return total

    def run_part2(self):
        total = 0

        def add_module(module, sub=0):
            fuel = math.floor(module / 3) - 2
            if fuel < 0:
                fuel = 0
                return sub
            sub += fuel
            return add_module(fuel, sub)

        for module in self.input:
            total += add_module(module)
        return total


if __name__ == "__main__":
    print(Day1.part1_result(debug=False))
    print(Day1.part2_result(debug=False))
