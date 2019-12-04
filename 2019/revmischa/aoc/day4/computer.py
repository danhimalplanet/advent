import os
import sys

PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401


class Day4(Computer):
    pwd: str = PWD
    input = map(int, "123257-647015".split("-"))

    def run_part1(self):
        start, end = self.input
        count = 0
        for pw in range(start, end):
            chars = str(pw)
            if "".join(sorted(chars)) != chars:
                continue
            ok = False
            for c in chars:
                ccount = chars.count(c)
                if ccount == 2:
                    ok = True
            if not ok:
                continue
            count += 1
            print(pw)
        return count

    def run_part2(self):
        return 0


if __name__ == "__main__":
    print(Day4.part1_result(debug=False))
    print(Day4.part2_result(debug=False))
