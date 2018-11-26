#!/usr/bin/env python

import os.path
import sys

# this didn't work
C2 = {
    "ne": complex(1, 1),
    "n": complex(0, 1),
    "nw": complex(-1, 1),
    "se": complex(1, -1),
    "s": complex(0, -1),
    "sw": complex(-1, -1)
}

C = {
    "ne": complex(0.5, 0.5),
    "n": complex(0, 1),
    "nw": complex(-0.5, 0.5),
    "se": complex(0.5, -0.5),
    "s": complex(0, -1),
    "sw": complex(-0.5, -0.5)
}


def one(path):
    s = sum([C[p] for p in path])
    return int(abs(s.real) + abs(s.imag))


def two(path):
    ls = []
    maxsum = 0
    for p in path:
        ls.append(C[p])
        s = sum(ls)
        a = abs(s.real) + abs(s.imag)
        if a > maxsum:
            maxsum = a

    return int(maxsum)


def main(args):
    if os.path.exists(args[0]):
        path = open(args[0]).readline().strip().split(",")
    else:
        path = args[0].split(",")

    print(one(path))
    print(two(path))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
