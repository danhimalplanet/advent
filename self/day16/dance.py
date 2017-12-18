#!/usr/bin/env python

import os.path
from string import lowercase
import sys


def dance(moves, programs):
    for move in moves:
        if move[0] == "s":
            amount = int(move[1:], 10)
            programs = programs[len(programs) - amount:] + programs[:len(
                programs) - amount]
        elif move[0] == "x":
            a, b = [int(pos, 10) for pos in move[1:].split("/")]
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == "p":
            a, b = move[1:].split("/")
            ia = programs.index(a)
            ib = programs.index(b)
            programs[ia], programs[ib] = programs[ib], programs[ia]

    return programs


def one(moves, programs):
    programs = dance(moves, programs)

    return "".join(programs)


def two(moves, programs):
    """this code is not a code of honor."""

    first = dance(moves, programs)
    outputs = [first[:]]
    programs = first[:]
    cycle = -1
    while True:
        programs = dance(moves, programs)
        outputs.append(programs[:])
        if programs == first:
            # add one here because "first" is the first output, not
            # the first one in the sequence (starting with abcde...)
            cycle = len(outputs) + 1
            break

    # _after_ 1 billion cycles
    mod = 1000000001 % cycle
    print("cycle at %d mod %d" % (cycle, mod))

    return "".join(outputs[mod])


def main(args):
    if os.path.exists(args[0]):
        inval = open(args[0]).readline().strip().split(",")
    else:
        inval = args[0].split(",")

    programs = list(lowercase[0:16])
    print(one(inval, programs))
    programs = list(lowercase[0:16])
    print(two(inval, programs))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
