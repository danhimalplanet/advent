#!/usr/bin/env python

import sys

TURNS = {
    ".": "left",
    "W": "same",
    "#": "right",
    "F": "reverse"
}

CHANGE1 = {
    "#": ".",
    ".": "#"
}

CHANGE2 = {
    ".": "W",
    "W": "#",
    "#": "F",
    "F": "."
}

MOVES = {
    "up": {
        "left": "left",
        "right": "right",
        "reverse": "down",
        "same": "up"
    },
    "down": {
        "left": "right",
        "right": "left",
        "reverse": "up",
        "same": "down"
    },
    "left": {
        "left": "down",
        "right": "up",
        "reverse": "right",
        "same": "left"
    },
    "right": {
        "left": "up",
        "right": "down",
        "reverse": "left",
        "same": "right"
    }
}


def move(r, c, direction, turn):
    newdir = MOVES[direction][turn]

    if newdir == "up":
        return r - 1, c, newdir
    elif newdir == "down":
        return r + 1, c, newdir
    elif newdir == "left":
        return r, c - 1, newdir
    elif newdir == "right":
        return r, c + 1, newdir


def printgrid(grid, direction, r, c, more=""):
    for i in range(len(grid)):
        row = grid[i][:]
        if r == i:
            row[c] = "!"
        print("".join(row))

    print(direction)
    print(r, c)
    if more:
        print(more)


def expand(r, c, grid):
    if c < 0:
        c = 0
        r += 1
    if r < 0:
        r = 0
        c += 1
    row = ["."] * len(grid[0])
    grid.insert(0, row[:])
    grid.append(row[:])
    for i in range(len(grid)):
        grid[i].insert(0, ".")
        grid[i].append(".")


    return r, c, grid


def one(grid, bursts):
    r = c = len(grid) / 2
    infectcount = 0
    direction = "up"

    while bursts > 0:
        turn = TURNS[grid[r][c]]

        grid[r][c] = CHANGE1[grid[r][c]]
        if grid[r][c] == "#":
            infectcount += 1

        r, c, direction = move(r, c, direction, turn)
        if r < 0 or r == len(grid) or c < 0 or c == len(grid):
            r, c, grid = expand(r, c, grid)
        bursts -= 1

    # printgrid(grid, direction, -1, -1)

    return infectcount


def two(t, size, bursts):
    r = c = size / 2
    infectcount = 0
    direction = "up"

    while bursts > 0:
        turn = TURNS[t[(r, c)]]

        t[(r, c)] = CHANGE2[t[(r, c)]]
        if t[(r, c)] == "#":
            infectcount += 1

        r, c, direction = move(r, c, direction, turn)
        if (r, c) not in t:
            t[(r, c)] = "."
        bursts -= 1

    return infectcount


def main(args):
    """./virus.py 22.input 10000000"""

    input = [line.strip() for line in open(sys.argv[1]).readlines()]

    t = {}

    grid = []
    for r in range(len(input)):
        row = input[r]
        cellrow = []
        for c, cell in enumerate(row):
            t[(r, c)] = cell
            cellrow.append(cell)
        grid.append(cellrow)

    print(one(grid, int(sys.argv[2], 10)))
    # print(two(t, len(input), int(sys.argv[2], 10)))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
