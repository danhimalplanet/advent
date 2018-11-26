#!/usr/bin/env python

from json import dump, load
import os.path
import sys

sys.path.append("../day10")

# in retrospect, badly named
from hash import hashround, densehash


def hextobin(hexstr):
    binls = []
    for i in hexstr:
        b = bin(int(i, 16)).replace("0b", "")
        while len(b) != 4:
            b = "0" + b
        binls.append(b)

    return binls


def h(binstr):
    """print rows with hashes and dots instead of ones and zeros."""
    ls = []
    for b in binstr:
        if b == "1":
            ls.append("#")
        else:
            ls.append(".")

    return "".join(ls)


def printdisk(disk):
    for row in disk:
        print(h("".join(row)))


def makedisk(hashprefix):
    # i don't want to recalculate this a lot, so cache on disk
    if os.path.exists("%s.json" % hashprefix):
        return load(open("%s.json" % hashprefix))

    rows = []
    for suffix in range(128):
        rowval = hashprefix + "-%d" % suffix
        lengths = [ord(str(l)) for l in rowval]
        lengths.extend([17, 31, 73, 47, 23])
        arr = hashround(lengths, rounds=64)
        binval = hextobin("".join(["%02x" % i for i in densehash(arr)]))
        # print("%s %s" % (h("".join(binval)), rowval))
        rows.append(binval)

    with open("%s.json" % hashprefix, "w") as w:
        dump(rows, w)

    return rows


def one(hashprefix):
    disk = makedisk(hashprefix)
    # printdisk(disk)
    onecount = 0
    for row in disk:
        onecount += "".join(row).count("1")

    return onecount


def connectedcells(disk, row, column):
    def possiblecells(row, column):
        possible = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
        retlist = []
        for p in possible:
            if p[0] < 0 or p[1] < 0 or p[0] > 127 or p[1] > 127:
                continue
            if disk[p[0]][p[1]] == "1":
                retlist.append(p)
        return retlist

    visited = [(row, column)]
    tovisit = possiblecells(row, column)
    cell = None
    while len(tovisit):
        cell = tovisit.pop(0)
        visited.append(cell)
        maybe1 = possiblecells(cell[0], cell[1])
        maybe = []
        for cell in maybe1:
            if cell not in visited and cell not in tovisit:
                maybe.append(cell)
        if len(maybe) or len(tovisit):
            tovisit.extend(maybe)

    return visited


def zero(disk, cells):
    for cell in cells:
        disk[cell[0]][cell[1]] = "0"


def two(hashprefix):
    # could be cleaner
    disk = []
    for row in makedisk(hashprefix):
        disk.append([cell for cell in "".join(row)])
    regioncount = 0
    r = 0
    c = 0
    while r < 128:
        # find first "1"
        while disk[r][c] == "0":
            c += 1
            if c == 128:
                c = 0
                r += 1
                if r == 128:
                    return regioncount
        possible = connectedcells(disk, r, c)
        if len(possible):
            regioncount += 1
        # zero out the region
        zero(disk, possible)
        c += 1
        if c == 128:
            c = 0
            r += 1

    return regioncount


def main(args):
    if os.path.exists(args[0]):
        inval = open(args[0]).readline().strip()
    else:
        inval = args[0]

    print(one(inval))
    print(two(inval))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
