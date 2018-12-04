#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter, defaultdict
from os.path import join


def part1(input):
    guards = defaultdict(Counter)
    sleeptime = Counter()
    curguard = None
    startminute = None
    endminute = None
    for line in input:
        ls = line.split()
        minute = int(ls[1].split(":")[1].replace("]", ""), 10)
        if ls[2] == "Guard":
            curguard = ls[3]
        elif ls[2] == "falls":
            startminute = minute
        elif ls[2] == "wakes":
            endminute = minute
            for m in range(startminute, endminute):
                guards[curguard][m] += 1
            sleeptime[curguard] += (endminute - startminute)

    item = sleeptime.most_common()[0]
    iguard = int(item[0][1:], 10)
    mintimes = guards[item[0]].most_common()

    return guards, sleeptime, iguard * mintimes[0][0]


def part2(guards, sleeptime):
    wantedg = None
    wantedgslept = 0
    wantedgmin = 0
    for item in sleeptime.most_common():
        iguard = int(item[0][1:], 10)
        mintimes = guards[item[0]].most_common()
        if mintimes[0][1] > wantedgslept:
            wantedg = iguard
            wantedgslept = mintimes[0][1]
            wantedgmin = mintimes[0][0]

    return wantedg * wantedgmin


if __name__ == "__main__":
    input = [line.strip() for line in open(join("resources", "input.txt"))]
    input.sort()
    guards, sleeptime, wanted = part1(input)
    print(wanted)
    print(part2(guards, sleeptime))


# eof
