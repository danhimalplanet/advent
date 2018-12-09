#!/usr/bin/env python


from collections import Counter
from os.path import join


def play(players, target):
    scores = Counter()

    marbles = [0, 1]
    curpos = 1
    moves = 1
    nextmarble = 1
    curplayer = 1
    while True:
        curplayer = (curplayer + 1) % players
        nextmarble += 1

        if nextmarble % 23 == 0:
            scores[curplayer] += nextmarble
            find7 = curpos - 7
            if find7 < 0:
                fromright = 7 - curpos
                find7 = len(marbles) - fromright
            scores[curplayer] += marbles.pop(find7)
            curpos = find7
        else:
            nextpos = curpos + 2
            if nextpos < len(marbles):
                marbles.insert(nextpos, nextmarble)
                curpos = nextpos
            else:
                marbles.append(nextmarble)
                curpos = -1

        moves += 1
        if nextmarble == target:
            break

    return scores.most_common()[0]


if __name__ == "__main__":
    print("part1: %d" % play(424, 71144)[1])
    print("part2: %d" % play(424, 7114400)[1])

# eof
