import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
import numpy as np


class DayN(Computer):
    pwd = PWD

    def __init__(self, a, b):
        """Construct solver with puzzle input."""
        super().__init__()
        self.a_init = a
        self.b_init = b
        self.matches = 0

    def a_gen(self):
        a = self.a_init
        while True:
            a_1 = a * 16807
            a_2 = a_1 % 2147483647
            a = a_2
            yield a

    def b_gen(self):
        b = self.b_init
        while True:
            b_1 = b * 48271
            b_2 = b_1 % 2147483647
            b = b_2
            yield b

    async def run(self):
        iters = 100
        iters = 5000000
        ad = np.ndarray(shape=(iters, 1), dtype=int)
        bd = np.ndarray(shape=(iters, 1), dtype=int)

        def calc_a():
            a_gen = self.a_gen()
            for i in range(0, iters):
                n = next(a_gen)
                while n % 4 != 0:
                    n = next(a_gen)
                ad[i] = n

        def calc_b():
            b_gen = self.b_gen()
            for i in range(0, iters):
                n = next(b_gen)
                while n % 8 != 0:
                    n = next(b_gen)
                bd[i] = n

        with ThreadPoolExecutor(max_workers=3) as e:
            af = e.submit(calc_a)
            bf = e.submit(calc_b)
            if af.exception():
                print(af.exception)
            if bf.exception():
                print(bf.exception)

        def compare(blk_slice):
            (i, j) = blk_slice
            ads = ad[i:j]
            bds = bd[i:j]
            for i in range(0, iters):
                a = ads[i]
                b = bds[i]
                a_lo = (2**16-1) & a
                b_lo = (2**16-1) & b
                if a_lo == b_lo:
                    self.matches += 1

        compare_blocks = 40
        stride = int(iters / compare_blocks)
        blocks = []
        for i in range(0, compare_blocks):
            blocks.append([
                i*stride, i*stride+stride,
            ])
        with ThreadPoolExecutor(max_workers=compare_blocks) as e:
            e.map(compare, blocks)

            # print(f"a: {a}  b: {b}")
            # print("alo: {:0b}   blo: {:0b}".format(int(a_lo), int(b_lo)))

    def run_part1(self):
        start = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run())
        print(f"Took {time.time() - start} seconds.")
        return self.matches

    def run_part2(self):
        return 0

if __name__ == '__main__':
    print(DayN(618, 814).run_part1())
