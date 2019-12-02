import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401


class DayN(Computer):
    pwd: str = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.input = structure

    @classmethod
    def parse_input(cls, input_str: str):
        return Computer.parse_input(input_str)

    def run_part1(self):
        return 0

    def run_part2(self):
        return 0

if __name__ == '__main__':
    print(DayN.part1_result(debug=False))
    print(DayN.part2_result(debug=False))
