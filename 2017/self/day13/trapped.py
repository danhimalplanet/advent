#!/usr/bin/env python

from copy import deepcopy
from pprint import pprint
import sys


class Scanner():
    def __init__(self, depth, range_):
        self.depth = depth
        self.range = range_
        self.reset()
    def reset(self):
        self.position = 0
        # 1 down, -1 up
        self.direction = 1
    def move(self):
        if self.position < self.range:
            self.position += self.direction
        if self.position == 0:
            self.direction = 1
        elif self.position == self.range - 1:
            self.direction = -1
    def severity(self):
        if self.position == 0:
            return self.depth * self.range
        return 0
    def __repr__(self):
        ls = [" "] * self.range
        ls[self.position] = "S"
        return str(ls)


def advance(firewall, packetlevel, reportcollision=False):
    severity = 0
    for i in range(len(firewall)):
        if firewall[i]:
            if packetlevel == i and firewall[i].position == 0:
                if reportcollision:
                    return True
                severity += firewall[i].severity()
            firewall[i].move()

    return severity


def newfirewall(dr):
    maxlevel = max(dr.keys())
    firewall = []
    for i in range(maxlevel+1):
        if i in dr:
            firewall.append(Scanner(i, dr[i]))
        else:
            firewall.append([])

    return maxlevel, firewall


def traverse(firewall, packetlevel, reportcollision=False):
    retval = advance(firewall, packetlevel, reportcollision)

    return retval, packetlevel+1


def one(dr):
    maxlevel, firewall = newfirewall(dr)
    packetlevel = 0
    severity = 0

    while packetlevel <= maxlevel:
        s, packetlevel = traverse(firewall, packetlevel)
        severity += s

    return severity


def two(dr):
    maxlevel, firewall = newfirewall(dr)
    saved = deepcopy(firewall)
    delay = 0

    while True:
        packetlevel = 0
        failed = False

        if delay:
            advance(firewall, -1)
            saved = deepcopy(firewall)

        while packetlevel <= maxlevel:
            collision, packetlevel = traverse(firewall, packetlevel, reportcollision=True)
            if collision:
                failed = True
                if delay % 10000 == 0:
                    print("failed at delay %d" % delay)
                break
        if not failed:
            return delay
        firewall = deepcopy(saved)
        delay += 1

    return delay


def main(args):
    lines = [line.strip() for line in open(args[0]).readlines()]
    dr = {}
    for line in lines:
        parts = [int(l, 10) for l in line.split(": ")]
        dr[parts[0]] = parts[1]

    print(one(dr))
    print(two(dr))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
