#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from os.path import join


def part1(boxids):
    two = 0
    three = 0
    for boxid in boxids:
        vals = list(Counter(boxid).values())
        if vals.count(2) > 0:
            two += 1
        if vals.count(3) > 0:
            three += 1
    return two * three


def part2(boxids):
    lenc = len(boxids) - 1
    lenb = len(boxids[0])
    for i in range(lenc):
        for j in range(i+1, lenc):
            diff = [l == r for l, r in zip(boxids[i], boxids[j])]
            if diff.count(False) == 1:
                common = [boxids[i][idx] for idx in range(lenb) if diff[idx]]
                return "".join(common)


if __name__ == "__main__":
    boxids = [line.strip() for line in open(join("resources", "input.txt"))]
    print(part1(boxids))
    print(part2(boxids))


# eof
