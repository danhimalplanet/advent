import os
import sys
from collections import Counter


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint
import numpy as np
from time import time
from itertools import islice, cycle

OPEN = '.'
TREES = '|'
LUMBERYARD = '#'
IGNORE = ' '


class Day18(Computer):
    pwd = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.input = structure

    @classmethod
    def parse_input(cls, input_str: str):
        mat = None
        col_count = None
        row = 0
        for line in input_str.splitlines():
            # create matrix if needed
            col_count = len(line)
            if mat is None:
                mat = np.ndarray((col_count, col_count), 'U1')

            col = 0
            for c in line:
                mat[row, col] = c
                col += 1

            row += 1
        return mat

    def count_adj(self, c, padded, row, col) -> Counter:
        # get 3x3 matrix of adjacent cells
        adj = padded[row-1:row+2, col-1:col+2]
        # count types
        counter = Counter(adj.flatten())
        # subtract c from count because we don't count current cell
        counter[c] -= 1
        return counter

    def iter(self) -> np.ndarray:
        mat = self.input
        next_mat = mat.copy()

        # pad matrix to account for edges
        padded = np.pad(mat, 1, 'constant', constant_values=IGNORE)

        for row, col in np.ndindex(padded.shape):
            c = padded[row, col]
            if c == IGNORE:  # hit padding
                continue

            # count adjacent cells
            counter = self.count_adj(c, padded, row, col)

            # get next state of cell
            next_mat[row-1, col-1] = self.get_next(c, counter)

        return next_mat

    def get_next(self, c, counter) -> str:
        if c == IGNORE:
            raise Exception("get_next() called on non-cell")

        if c == OPEN:
            # An open acre will become filled with trees if three or more adjacent acres contained trees
            return TREES if counter[TREES] >= 3 else c

        if c == TREES:
            # An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards
            return LUMBERYARD if counter[LUMBERYARD] >= 3 else c

        if c == LUMBERYARD:
            # An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open
            if counter[LUMBERYARD] >= 1 and counter[TREES] >= 1:
                return c
            else:
                return OPEN

        raise Exception(f"unknown cell {c}")

    def run_part1(self, iterations=10):
        start = time()
        seen = []
        for i in range(iterations):
            next_m = self.iter()
            self.input = next_m

            # print timing
            if i % 100 == 0 and i != 0:
                rate = time() - start
                completion = iterations / rate
                print(f"Iteration {i} in {rate}s. will finish in {completion/3600}hr")
                start = time()

            # compare to old
            for j in range(len(seen)):
                seen_mat = seen[j]
                if np.array_equal(next_m, seen_mat):  # we've seen this before
                    cycle_len = i - j
                    print(f"Cycle detected after {i} iterations, cycle len = {cycle_len}")

                    # how many times to continue cycle
                    gen = iterations - j - 1
                    cycle_idx = gen % cycle_len
                    mat_cycle = seen[j:]
                    mat = mat_cycle[cycle_idx]

                    # output answer (part2)
                    return self.count_answer(mat)

            # one step
            seen.append(next_m)

        # part 1
        return self.count_answer(self.input)

    def run_part2(self):
        return self.run_part1(iterations=1000000000)

    def count_answer(self, mat):
        print(mat)
        counter = Counter(mat.flatten())
        print(counter)
        return counter[TREES] * counter[LUMBERYARD]


if __name__ == '__main__':
    print(Day18.part1_result(debug=False))
    print(Day18.part2_result(debug=False))
