#!/usr/bin/env python

import sys


def one(insn):
    maxloc = len(insn)
    ip = 0
    steps = 0

    while True:
        j = insn[ip]
        insn[ip] += 1
        ip += j
        steps += 1
        if ip >= maxloc or ip < 0:
            return steps


def two(insn):
    maxloc = len(insn)
    ip = 0
    steps = 0

    while True:
        j = insn[ip]
        if j >= 3:
            insn[ip] -= 1
        else:
            insn[ip] += 1
        ip += j
        steps += 1
        if ip >= maxloc or ip < 0:
            return steps


def main(args):
    insn = [int(line.strip(), 10) for line in open(args[0]).readlines()]

    print(one(insn[:]))
    print(two(insn[:]))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
