#!/usr/bin/env python

from collections import defaultdict
import sys


def allconnectedto(c, prog):
    seen = set()
    count = 0
    queue = [prog]
    for p in queue:
        if p in seen:
            continue
        seen.add(p)
        count += 1
        queue.extend(c[p])

    return count, list(seen)


def one(c):
    return allconnectedto(c, "0")


def two(c):
    groups = 0
    while len(c):
        start = c.keys()[0]
        count, seen = allconnectedto(c, start)
        if count:
            groups += 1
            del c[start]
            for p in seen:
                if p in c:
                    del c[p]

    return groups


def main(args):
    c = defaultdict(list)

    lines = [line.strip() for line in open(args[0]).readlines()]
    for line in lines:
        prog, _ignore, other = line.split(" ", 2)
        other = other.split(", ")
        c[prog].extend(other)
        for p in other:
            if prog not in c[p]:
                c[p].append(prog)

    print(one(c)[0])
    print(two(c))


if __name__ == "__main__":
    main(sys.argv[1:])
