#!/usr/bin/env python

from os.path import join
from string import lowercase, uppercase


def compare(a, b):
    if a in lowercase and b in uppercase:
        return a.upper() == b
    elif a in uppercase and b in lowercase:
        return a.lower() == b


def part1(input):
    ls = [c for c in input]

    while True:
        i = 0
        llen = len(ls)-1
        changed = False
        while i < llen:
            if compare(ls[i], ls[i+1]):
                ls.pop(i)
                ls.pop(i)
                changed = True
                llen -= 2
            else:
                i += 1
        if not changed:
            return "".join(ls)


def part2(input):
    letters = set()
    for c in input:
        letters.add(c.lower())
    lowest = len(input)
    for w in list(letters):
        ls = [c for c in input if c not in (w, w.upper())]
        slen = len(part1(ls))
        print("removing %s: %d => %d: %d" % (w, len(input), len(ls), slen))
        if slen < lowest:
            lowest = slen
    return lowest


if __name__ == "__main__":
    input = open(join("resources", "input.txt")).read().strip()
    print(len(part1(input)))
    print(part2(input))


# eof
