#!/usr/bin/env python

import sys


def redistribute(banks):
    numbanks = len(banks)
    blocksidx = -1
    blocks = -1
    for i in range(numbanks):
        if banks[i] > blocks:
            blocks = banks[i]
            blocksidx = i

    banks[blocksidx] = 0
    while blocks > 0:
        blocksidx = (blocksidx+1) % numbanks
        banks[blocksidx] += 1
        blocks -= 1

    return banks


def one(banks):
    seen = set()
    cycles = 0

    while True:
        if tuple(banks) in seen:
            return cycles
        else:
            seen.add(tuple(banks))
        banks = redistribute(banks)
        cycles += 1


def two(banks):
    seen = {}
    cycles = 0

    while True:
        if tuple(banks) in seen:
            return cycles - seen[tuple(banks)]
        else:
            seen[tuple(banks)] = cycles
        banks = redistribute(banks)
        cycles += 1


def main(args):
    # banks = [0, 2, 7, 0]
    banks = [int(b, 10) for b in open(args[0]).readline().strip().split()]

    print(one(banks))
    print(two(banks))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
