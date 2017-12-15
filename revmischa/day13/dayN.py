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
        self.fw = structure
        self.size = max(structure.keys())

    @classmethod
    def parse_input(cls, input_str: str):
        fw = {}
        for line in input_str.split('\n'):
            d, r = line.split(': ')
            fw[int(d)] = int(r)
        return fw

    def run_part1(self, delay=0):
        # pprint(self.fw)
        sev = 0
        for n in range(0, self.size + 1):
            if n not in self.fw:
                continue
            r = self.fw[n]
            res = (n + delay) % ((r - 1) * 2)
            # print(f"N: {n} - R: {r}   ==   res={res}")
            caught = 0 == res
            if caught:
                sev += n * r + delay
        return sev

    def run_part2(self):
        cnt = 0
        while self.run_part1(cnt) != 0:
            cnt += 1
        return cnt

if __name__ == '__main__':
    main(DayN)
