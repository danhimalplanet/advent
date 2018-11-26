#!/usr/bin/env python

import os.path
import sys


NEXT = {"r": "u",
        "u": "l",
        "l": "d",
        "d": "r"}


def nextcell(cell, nextdir):
    if nextdir == "r":
        return (cell[0]+1, cell[1])
    elif nextdir == "l":
        return (cell[0]-1, cell[1])
    elif nextdir == "u":
        return (cell[0], cell[1]+1)
    else:
        return (cell[0], cell[1]-1)


def makeupto(target):
    grid = [(0, 0)]
    nextdir = "r"
    dist = (0, 1)
    numcells = dist[1]

    while target != len(grid):
        grid.append(nextcell(grid[-1], nextdir))
        numcells -= 1
        if numcells == 0:
            nextdir = NEXT[nextdir]
            dist = (dist[1], dist[0]+1)
            numcells = dist[1]

    return grid


def manhattan(grid, target):
    xdis = abs(grid[target-1][0] - grid[0][0])
    ydis = abs(grid[target-1][1] - grid[0][1])

    return xdis + ydis


def distancefrom(target):
    grid = makeupto(target)

    return manhattan(grid, target)


def largerthan(target):
    cell = (0, 0)
    nextdir = "r"
    dist = (0, 1)
    numcells = dist[1]
    # cell -> value
    cellval = {cell: 1}

    # ugh
    def sumvals(cell):
        return sum([cellval.get((cell[0], cell[1]-1), 0),
                    cellval.get((cell[0], cell[1]+1), 0),
                    cellval.get((cell[0]-1, cell[1]), 0),
                    cellval.get((cell[0]+1, cell[1]), 0),
                    cellval.get((cell[0]+1, cell[1]+1), 0),
                    cellval.get((cell[0]-1, cell[1]-1), 0),
                    cellval.get((cell[0]-1, cell[1]+1), 0),
                    cellval.get((cell[0]+1, cell[1]-1), 0)])

    while cellval[cell] < target:
        cell = nextcell(cell, nextdir)
        cellval[cell] = sumvals(cell)
        numcells -= 1
        if numcells == 0:
            nextdir = NEXT[nextdir]
            dist = (dist[1], dist[0]+1)
            numcells = dist[1]

    return cellval[cell]


def main(args):
    print(distancefrom(int(args[0], 10)))
    print(largerthan(int(args[0], 10)))


if __name__ == "__main__":
    main(sys.argv[1:])
