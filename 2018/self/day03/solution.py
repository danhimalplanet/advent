#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from os.path import join


def part1(claims):
    fabric = []
    for i in range(2000):
        fabric.append([0] * 2000)
    for claim in claims:
        ls = claim.split()
        lt = [int(i) for i in ls[2].replace(":", "").split(",")]
        wh = [int(i) for i in ls[3].split("x")]
        for y in range(lt[1], lt[1] + wh[1]):
            for x in range(lt[0], lt[0] + wh[0]):
                fabric[y][x] += 1

    overlap = 0
    for y in range(2000):
        for x in range(2000):
            if fabric[y][x] > 1:
                overlap += 1

    return overlap, fabric


def part2(claims, fabric):
    for claim in claims:
        ls = claim.split()
        lt = [int(i) for i in ls[2].replace(":", "").split(",")]
        wh = [int(i) for i in ls[3].split("x")]
        totalsize = wh[0] * wh[1]
        overlap = 0
        for y in range(lt[1], lt[1] + wh[1]):
            for x in range(lt[0], lt[0] + wh[0]):
                overlap += fabric[y][x]
        if overlap == totalsize:
            return ls[0]


if __name__ == "__main__":
    claims = [line.strip() for line in open(join("resources", "input.txt"))]
    overlap, fabric = part1(claims)
    print(overlap)
    print(part2(claims, fabric))


# eof
