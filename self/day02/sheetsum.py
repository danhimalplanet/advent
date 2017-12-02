#!/usr/bin/env python

import os.path
import sys


def calcsum1(sheet):
    checksum = 0

    for row in sheet:
        irow = [int(item, 10) for item in row.split()]
        checksum += max(irow) - min(irow)

    return checksum


def calcdiv2(sheet):
    checksum = 0

    for idx, row in enumerate(sheet):
        irow = [int(item, 10) for item in row.split()]
        irow.sort()
        for i in range(len(irow)):
            found = False
            for j in range(i+1, len(irow)):
                if irow[j] % irow[i] == 0:
                    checksum += irow[j] / irow[i]
                    found = True
                    break
            if found:
                break

    return checksum


def main(args):
    if len(args) == 1 and os.path.exists(args[0]):
        sheet = [line.strip() for line in open(args[0]).readlines()]

    print(calcsum1(sheet))
    print(calcdiv2(sheet))


if __name__ == "__main__":
    main(sys.argv[1:])
