#!/usr/bin/env python


from os.path import join


def loop1(input, start=0):
    children = input[start]
    mdcount = input[start+1]

    if children == 0:
        return sum(input[start+2:start+2+mdcount]), start+2+mdcount

    newstart = start + 2
    mdsum = 0
    for child in range(children):
        s, newstart = loop1(input, newstart)
        mdsum += s

    return mdsum + sum(input[newstart:newstart+mdcount]), newstart + mdcount


def part1(input):
    return loop1(input)[0]


def loop2(input, start=0):
    children = input[start]
    mdcount = input[start+1]

    if children == 0:
        return sum(input[start+2:start+2+mdcount]), start+2+mdcount

    newstart = start + 2
    mdsum = 0
    mdsums = {}
    for child in range(children):
        s, newstart = loop2(input, newstart)
        mdsums[child+1] = s

    metadata = input[newstart:newstart+mdcount]

    for child in metadata:
        mdsum += mdsums.get(child, 0)

    return mdsum, newstart + mdcount


def part2(input):
    return loop2(input)[0]


if __name__ == "__main__":
    input = [int(x, 10) for x in open(join("resources", "input.txt")).readline().split()]
    print(part1(input))
    print(part2(input))

# eof
