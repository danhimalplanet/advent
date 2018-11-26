#!/usr/bin/env python

from string import uppercase
import sys


def next(r, c, direction):
    if direction == "down":
        r += 1
    elif direction == "up":
        r -= 1
    elif direction == "right":
        c += 1
    else:
        c -= 1

    return r, c, direction


def switchdir(r, c, direction, territory):
    lrows = len(territory)
    lcols = len(territory[0])

    maybe = [(r + 1, c, "down"),
             (r - 1, c, "up"),
             (r, c + 1, "right"),
             (r, c - 1, "left")]
    for cell in maybe:
        if cell[0] < 0 or cell[0] == lrows or cell[1] < 0 or cell[1] == lcols:
            continue
        if (direction in ("up", "down") and
            cell[2] in ("left", "right") and
            territory[cell[0]][cell[1]] != " "):
            r, c, direction = cell
            break
        elif (direction in ("left", "right") and
              cell[2] in ("up", "down") and
              territory[cell[0]][cell[1]] != " "):
            r, c, direction = cell
            break

    return r, c, direction


def both(territory):
    letters = []

    moves = 0
    r = 0
    c = 0
    direction = "down"

    # find starting "|"
    while territory[r][c] != "|":
        c += 1

    while True:
        moves += 1
        curcell = territory[r][c]
        if curcell in ("|", "-"):
            r, c, direction = next(r, c, direction)
        elif curcell in uppercase:
            letters.append(curcell)
            r, c, direction = next(r, c, direction)
        elif curcell == "+":
            r, c, direction = switchdir(r, c, direction, territory)
        else:
            return "".join(letters), moves - 1


def main(args):
    input = [line[:-1] for line in open(sys.argv[1]).readlines()]

    territory = []
    for r in range(len(input)):
        row = input[r]
        cellrow = []
        for cell in row:
            cellrow.append(cell)
        territory.append(cellrow)

    print(both(territory))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
