#!/usr/bin/env python

import sys


def one(steps, rounds=2017, afterzero=False):
    pos = 0
    curval = 0
    buf = [curval]
    lbuf = len(buf)

    for v in range(rounds):
        pos = (pos + steps) % lbuf + 1
        curval += 1
        buf.insert(pos, curval)
        lbuf += 1

    return buf[(pos + 1) % lbuf]


def main(args):
    print(one(int(args[0], 10), rounds=2017))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
