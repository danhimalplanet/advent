#!/usr/bin/env python

import os.path
import sys


def calcsum1(thing):
    s = 0
    cur = thing[0]
    thing = thing[1:] + cur
    for i in range(len(thing)):
        next = thing[i]
        if cur == next:
            s += int(cur, 10)
        cur = next

    return s


def calcsum2(thing):
    s = 0
    mid = len(thing)/2
    for idx, num in enumerate(thing):
        if num == thing[(idx+mid)%len(thing)]:
            s += int(num, 10)

    return s


def main(args):
    if len(args) == 1:
        if os.path.exists(args[0]):
            data = open(args[0]).read().strip()
        else:
            data = args[0]

    print(calcsum1(data))
    print(calcsum2(data))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
