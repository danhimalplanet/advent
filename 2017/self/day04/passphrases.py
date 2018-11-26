#!/usr/bin/env python

import sys

def countunique(phrases, anagram=False):
    valid = 0
    for phrase in phrases:
        d = {}
        isunique = True
        for word in phrase.split():
            if anagram:
                word = "".join(sorted([l for l in word]))
            if word in d:
                isunique = False
                break
            else:
                d[word] = True
        if isunique:
            valid += 1

    return valid


def main(args):
    phrases = [line.strip() for line in open(args[0]).readlines()]

    print(countunique(phrases))
    print(countunique(phrases, anagram=True))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
