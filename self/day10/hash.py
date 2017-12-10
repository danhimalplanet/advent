#!/usr/bin/env python

import os.path
import sys


def hashround(lengths, rounds, arr=None, pos=0, skip=0):
    if not arr:
        arr = []
        for i in range(256):
            arr.append(i)

    llen = len(arr)

    for l in lengths:
        newls = []
        for i in range(l):
            newls.append(arr[(pos+i) % llen])
        newls.reverse()
        for i in range(l):
            arr[(pos+i) % llen] = newls[i]
        pos = (pos + l + skip) % llen
        skip = (skip + 1) % llen

    if rounds == 1:
        return arr
    else:
        return hashround(lengths, rounds-1, arr, pos, skip)


def densehash(arr):
    dense = []
    for i in range(16):
        xored = arr[i*16]
        for j in range(1, 16):
            xored = xored ^ arr[i*16+j]
        dense.append(xored)

    return dense


def main(args):
    if os.path.exists(args[0]):
        inval = open(args[0]).readline().strip()
    else:
        inval = args[0]

    # part 1
    # inside a try/catch block because some of the test input for part 2
    # won't work here
    try:
        lengths = [int(l, 10) for l in inval.split(",")]
        after = hashround(lengths, rounds=1)
        print(after[0] * after[1])
    except Exception as exc:
        print("input not valid for part 1: %s" % str(exc))

    # part 2
    lengths = [ord(str(l)) for l in inval]
    lengths.extend([17, 31, 73, 47, 23])
    arr = hashround(lengths, rounds=64)
    hexval = "".join(["%02x" % i for i in densehash(arr)])
    print(hexval)


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
