import os
import sys

PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401
from typing import List, Dict
from itertools import chain

Grid = List[List[bool]]

SIZE = 5  # grid size


class Day24(Computer):
    pwd: str = PWD
    grid: Grid

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.grid = structure

    @classmethod
    def parse_input(cls, input_str: str):
        rows: Grid = []
        for line in input_str.split("\n"):
            col: List[bool] = []
            for c in line:
                col.append(True if c == "#" else False)
            rows.append(col)
        return rows

    def grid_biodiversity_rating(self, grid: Grid) -> int:
        pow2 = 1
        tot = 0
        for row in grid:
            for col in row:
                if col:
                    tot += pow2
                pow2 *= 2
        return tot

    def run_part1(self):
        seen_grids: Dict[int, bool] = {}
        while True:
            next_frame = self.next_frame(self.grid)
            rating = self.grid_biodiversity_rating(next_frame)
            if rating in seen_grids:  # seen this before
                return rating
            seen_grids[rating] = True
            self.grid = next_frame

    def print_grid(self, grid: Grid):
        for row in grid:
            for col in row:
                print("#" if col else ".", end="")
            print("")
        print("")

    def next_frame(self, cur_frame: Grid) -> Grid:
        nf: Grid = []
        for y, row in enumerate(cur_frame):
            nr: List[bool] = []
            for x, val in enumerate(row):
                # count neighbors
                ncount = self.count_neighbors(cur_frame, x, y)

                if val:
                    # bug dies unless exactly one neighbor
                    nr.append(True if ncount == 1 else False)
                else:
                    # bug spawns if 1 or 2 bugs next to space
                    nr.append(True if ncount == 1 or ncount == 2 else False)
            nf.append(nr)
        return nf

    def count_neighbors(self, grid: Grid, x: int, y: int):
        count = 0
        if x > 0:
            if grid[y][x - 1]:
                count += 1
        if x < SIZE - 1:
            if grid[y][x + 1]:
                count += 1
        if y > 0:
            if grid[y - 1][x]:
                count += 1
        if y < SIZE - 1:
            if grid[y + 1][x]:
                count += 1
        return count

    def run_part2(self):
        # part 2 sucks i don't wanna do it
        for _ in range(10):
            self.grid = self.next_frame(self.grid)
        return self.count_bugs(self.grid)

    # def count_bugs(self):
    #     count = 0
    #     for row in grid:
    #         for col in row:
    #             if row ==



if __name__ == "__main__":
    print(Day24.part1_result(debug=False))
    print(Day24.part2_result(debug=False))
