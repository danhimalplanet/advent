#!/usr/bin/env python

from os.path import join
from re import compile


POSVELRE = compile(r"position=<\s*([-\d]+),\s*([-\d]+)> velocity=<\s*([-\d]+),\s*([-\d]+)>")


def move2(workposv, velv):
    numpos = len(workposv)
    seconds = 0

    minx = int(min([pos.real for pos in workposv]))
    maxx = int(max([pos.real for pos in workposv]))
    miny = int(min([pos.imag for pos in workposv]))
    maxy = int(max([pos.imag for pos in workposv]))

    minwidth = abs(maxx - minx)
    minheight = abs(maxy - miny)
    maxarea = minwidth * minheight
    # print(seconds, maxarea)

    while True:
        seconds += 1
        for i in range(numpos):
            workposv[i] += velv[i]

        minx = int(min([pos.real for pos in workposv]))
        maxx = int(max([pos.real for pos in workposv]))
        miny = int(min([pos.imag for pos in workposv]))
        maxy = int(max([pos.imag for pos in workposv]))

        width = abs(maxx - minx)
        height = abs(maxy - miny)
        area = width * height

        if area < maxarea:
            minwidth = width
            minheight = height
            maxarea = area
        else:
            # done
            seconds -= 1
            for i in range(numpos):
                workposv[i] -= velv[i]
            return workposv, seconds


def move(posv, velv):
    workposv, seconds = move2(posv[:], velv)

    minx = int(min([pos.real for pos in workposv]))
    maxx = int(max([pos.real for pos in workposv]))
    miny = int(min([pos.imag for pos in workposv]))
    maxy = int(max([pos.imag for pos in workposv]))

    xcols = abs(maxx - minx + 1)
    yrows = abs(maxy - miny + 1)

    width = [" "] * xcols

    grid = []
    for _ in range(yrows):
        grid.append(width[:])

    for pos in workposv:
        grid[int(pos.imag) - miny][int(pos.real) - minx] = "X"

    print("")
    for row in grid:
        print(" ".join(row))
    print("")

    return seconds


def doit(input):
    posv = []
    velv = []

    for pvline in input:
        match = POSVELRE.search(pvline)
        (x, y, dx, dy) = match.groups()
        posv.append(complex(int(x, 10), int(y, 10)))
        velv.append(complex(int(dx, 10), int(dy, 10)))

    return move(posv, velv)



if __name__ == "__main__":
    POSVEC = [line.strip() for line in open(join("resources", "input.txt"))]
    print(doit(POSVEC))

# eof
