#!/usr/bin/env python

import os.path
import sys


def both(line):
    llen = len(line)
    idx = 0
    state = 0
    score = 0
    ingarbage = False
    garbagechars = 0

    while idx < llen:
        while ingarbage:
            char = line[idx]
            if char == "!":
                idx += 2
            elif char == ">":
                idx += 1
                ingarbage = False
            else:
                idx += 1
                garbagechars += 1
            continue
        char = line[idx]
        if char == "<":
            ingarbage = True
            idx += 1
            continue
        elif char == "{":
            state += 1
            idx += 1
        elif char == "}":
            score += state
            state -= 1
            idx += 1
        elif char == ",":
            idx += 1
            continue

    return score, garbagechars


def main(args):
    input = args[0]

    if os.path.exists(args[0]):
        input = open(args[0]).read().strip()

    print(both(input))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
