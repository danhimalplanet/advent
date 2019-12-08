import os
import sys

PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401
from more_itertools import chunked


class Day8(Computer):
    pwd: str = PWD

    def __init__(self, structure, w: int, h: int, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.input = structure
        self.w = w
        self.h = h

    @classmethod
    def parse_input(cls, input_str: str):
        return input_str

    def run_part1(self):
        layer_size = self.w * self.h

        zero_count = 1000000
        zl = 0
        i = 0
        layer_chunks = list(chunked(self.input, layer_size))
        for layer in layer_chunks:
            zc = layer.count("0")
            if zc < zero_count:
                zero_count = zc
            i += 1
        l = layer_chunks[zl]
        return l.count("1") * l.count("2")

    def run_part2(self):
        layer_size = self.w * self.h
        layer_chunks = list(chunked(self.input, layer_size))
        out_img = []

        for y in range(self.h):
            row = []
            for x in range(self.w):
                pixel = self.calc_pixel(layer_chunks, x, y)
                row.append(pixel)
                pixel = "█" if pixel == '1' else " "
                print(pixel, end="")
            out_img.append(row)
            print("")

        return out_img

    def calc_pixel(self, layer_chunks, x, y):
        for layer in layer_chunks:
            # get pixel at x, y
            lv = layer[y * self.w + x]
            if lv != "2":  # not transparent
                return lv

        return 2


if __name__ == "__main__":
    print(Day8.part1_result(w=25, h=6, debug=False))
    print(Day8.part2_result(w=25, h=6, debug=False))
