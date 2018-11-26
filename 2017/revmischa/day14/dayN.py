import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
from revmischa.day10.dayN import DayN as Day10
from scipy.ndimage.measurements import label
import numpy as np


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.hash = structure

    def knot_hash(self, key: str) -> str:
        lengths = list(map(ord, key[:]))
        comp = Day10(lengths, 256)
        return comp.run_part2(key[:])

    @classmethod
    def parse_input(cls, input_str: str):
        return input_str

    def line_to_bitmap(self, line: str):
        bitmap = ''
        for c in line[:]:
            h = int(c, 16)
            b = "{:04b}".format(h)
            # print(f"c: {c}, h: {h}, b: {b}")
            bitmap += b
        return bitmap

    def get_bitmap(self):
        bitmap = []
        for row in range(0, 128):
            hi = f"{self.hash}-{row}"
            knot = self.knot_hash(hi)
            bitmap.append(self.line_to_bitmap(knot))
        return bitmap


    def run_part1(self):
        filled = 0
        for line in self.get_bitmap():
            filled += line.count('1')
        return filled

    def run_part2(self):
        bitmap = self.get_bitmap()
        nda = []
        for row in bitmap:
            nda.append(list(map(int, row[:])))
        a = np.array(nda)
        labeled_array, num_features = label(a)
        print(f"labeled_array: {labeled_array}, num_features: {num_features}")

if __name__ == '__main__':
    main(DayN)
