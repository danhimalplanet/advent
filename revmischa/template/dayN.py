import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure

    @classmethod
    def parse_input(cls, input_str: str):
        return Computer.parse_input(input_str)

    def run_part1(self):
        return 0

    def run_part2(self):
        return 0

if __name__ == '__main__':
    main(DayN)
