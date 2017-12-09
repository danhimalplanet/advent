#!/usr/bin/env python

from collections import defaultdict
import operator
from pprint import pprint
import sys


OPS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
    "inc": operator.iadd,
    "dec": operator.isub
}


def one(lines):
    regs = defaultdict(int)

    for line in lines:
        opreg, incdec, amount, _ignore, testreg, op, testamount = line.split()
        amount = int(amount, 10)
        testamount = int(testamount, 10)
        if OPS[op](regs[testreg], testamount):
            regs[opreg] = OPS[incdec](regs[opreg], amount)

    return max(regs.values())


def two(lines):
    regs = defaultdict(int)
    maxval = 0

    for line in lines:
        opreg, incdec, amount, _ignore, testreg, op, testamount = line.split()
        amount = int(amount, 10)
        testamount = int(testamount, 10)
        if OPS[op](regs[testreg], testamount):
            regs[opreg] = OPS[incdec](regs[opreg], amount)
        maxval = max(maxval, *regs.values())

    return maxval


def main(args):
    print(one((line.strip() for line in open(args[0]).readlines())))
    print(two((line.strip() for line in open(args[0]).readlines())))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
