#!/usr/bin/env python

import sys

TURNS = {".": "left",
         "W": "same",
         "#": "right",
         "F": "reverse"
}

CHANGE1 = {"#": ".",
           ".": "#"
}

CHANGE2 = {".": "W",
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


def move(r, c, newdir):
    if newdir == "up":
        return r - 1, c
    elif newdir == "down":
        return r + 1, c
    elif newdir == "left":
        return r, c - 1
    elif newdir == "right":
        return r, c + 1


def both(d, size, CHANGE, bursts):
    r = c = size / 2
    infectcount = 0
    direction = "up"

    while bursts > 0:
        turn = TURNS[d[(r, c)]]

        d[(r, c)] = CHANGE[d[(r, c)]]
        if d[(r, c)] == "#":
            infectcount += 1

        direction = MOVES[direction][turn]
        r, c = move(r, c, direction)
        if (r, c) not in d:
            d[(r, c)] = "."
        bursts -= 1

    return infectcount


def main(args):
    """./virus.py 22.input 10000000"""

    input = [line.strip() for line in open(sys.argv[1]).readlines()]

    d = {}

    for r in range(len(input)):
        for c, cell in enumerate(input[r]):
            d[(r, c)] = cell

    print(both(d.copy(), len(input), CHANGE1, 10000))
    print(both(d.copy(), len(input), CHANGE2, 10000000))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
