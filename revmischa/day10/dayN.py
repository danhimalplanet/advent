import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from itertools import cycle, islice
from functools import reduce


class DayN(Computer):
    pwd = PWD

    def __init__(self, lengths, size):
        """Construct solver with puzzle input."""
        super().__init__(lengths)
        self.c = cycle(range(0, size))
        self.cur_pos = 0
        self.size = size
        self.lengths = lengths
        self.skip = 0

    @classmethod
    def parse_input(cls, s):
        return list(map(int, s.split(',')))

    def one_loop(self):
        # current length
        ln = self.lengths.pop(0)

        start = self.cur_pos
        stop = self.cur_pos + ln

        # print(f"cur: {self.cur_pos}, {start}:{stop} len={ln} lc = {list(islice(self.c, 0, self.size))}")

        lc = list(islice(self.c, 0, self.size))
        # print(lc)

        sublist = list(islice(self.c, start, stop))
        sublist = list(reversed(sublist))

        # splice
        if ln + self.cur_pos > self.size:
            sub_end_i = self.size - start
            overflow = (stop) % self.size
            lc[start:self.size] = sublist[0:sub_end_i]
            lc_orig = lc[:]
            lc[0:overflow] = sublist[sub_end_i:sub_end_i + overflow]
            lc[overflow:self.size] = lc_orig[overflow:self.size]
        else:
            lc[start:stop] = sublist
        self.c = cycle(lc)
        self.cur_pos += ln + self.skip
        self.skip += 1
        self.cur_pos %= self.size

    def get_c(self):
        return list(islice(self.c, 0, self.size))

    def run_part1(self):
        while self.lengths:
            self.one_loop()
        final = self.get_c()
        first = final[0]
        second = final[1]
        return first * second

    def run_part2(self):
        lengths_ascii = list(map(ord, "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"))
        lengths_ascii += [17, 31, 73, 47, 23]
        self.lengths = lengths_ascii[:]
        for r in range(0, 64):
            self.lengths = lengths_ascii[:]
            while self.lengths:
                self.one_loop()

        c = self.get_c()

        # xor combine 16 item blocks
        dense_hash = []
        for i in range(0, 16):
            block = c[i * 16:i * 16 + 16]
            reduced = reduce(lambda x, y: x ^ y, block)
            dense_hash.append(reduced)
        print(self.get_c())
        print(dense_hash)

        h = ""
        for d in dense_hash:
            h_ = "{:02x}".format(d)
            print(h_)
            h += hex(d)[2:]

        print(h)

        return 0

if __name__ == '__main__':
    main(DayN, size=256)
