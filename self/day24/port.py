#!/usr/bin/env python

import sys


def chainsum(chain):
    s = 0
    for part in chain:
        s += part[0]
        s += part[1]
    print("DONE %d %d" % (s, len(chain)))


def findlink(part1, part2):
    if part1[0] == part2[0] or part1[1] == part2[0]:
        return part2[1]
    if part1[0] == part2[1] or part1[1] == part2[1]:
        return part2[0]


def findnext(parts, nextlink):
    possible = []
    for p in parts:
        if p[0] == nextlink or p[1] == nextlink:
            possible.append(p)

    return possible


def buildchain(start, parts, chain):
    chain.append(start)
    if len(chain) == 1:
        nextlink = max(start[0], start[1])
    else:
        nextlink = findlink(chain[-2], chain[-1])
    parts.remove(start)

    nextparts = findnext(parts, nextlink)
    if not nextparts:
        return chainsum(chain)
    else:
        for part in nextparts:
            buildchain(part, parts[:], chain[:])


def both(parts):
    startingparts = [p for p in parts if p[0] == 0 or p[1] == 0]
    for s in startingparts:
        ret = buildchain(s, parts[:], [])


def main(args):
    lines = [line.strip() for line in open(args[0]).readlines()]
    parts2 = [x.split("/") for x in lines]
    parts = [(int(x, 10), int(y, 10)) for x,y  in parts2]

    both(parts)


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
