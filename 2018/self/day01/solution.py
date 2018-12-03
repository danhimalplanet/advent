#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import cycle
from os.path import join


def part1(input):
    return sum(input)


def part2(input):
    freq = 0
    seen = set([freq])

    for i in cycle(input):
        freq += i
        if freq in seen:
            return freq
        seen.add(freq)


if __name__ == "__main__":
    input = [int(line.strip(), 10) for line in open(join("resources", "input.txt")).readlines()]
    print(part1(input))
    print(part2(input))

# eof
