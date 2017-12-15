import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from collections import defaultdict
from pprint import pprint


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure
        self.group_count = 0

    @classmethod
    def parse_input(cls, input_str: str):
        s = {}
        for line in input_str.split("\n"):
            i, links = line.split(' <-> ')
            ip = int(i)
            linksp = list(map(int, links.split(', ')))
            s[ip] = linksp
        return s

    def run(self):
        seen = defaultdict(int)

        def t(links):
            for cur in links:
                if cur in self.input and not seen[cur]:
                    seen[cur] += 1
                    n = self.input[cur]
                    del self.input[cur]
                    t(n)
        k = list(self.input.keys())
        n = self.input[k[0]]
        seen[k[0]] = 1
        del self.input[k[0]]
        t(n)
        return seen

    def run_part1(self):
        seen = self.run()
        pprint(seen)
        return len(seen.keys())

    def run_part2(self):
        while self.input:
            self.group_count += 1
            print("RUN")
            self.run()
        return self.group_count

if __name__ == '__main__':
    main(DayN)
