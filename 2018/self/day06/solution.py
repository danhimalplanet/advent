#!/usr/bin/env python

from collections import Counter
from os.path import join


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def calcarea(grid, minx, maxx, miny, maxy):
    # check (minx, miny), (minx + 1, miny) ... (maxx, miny)
    # anything we find there means the "owning" point has infinite area
    # same for (minx, maxy) to (maxx, maxy), etc
    infinites = set()

    for y in (miny, maxy-1):
        for x in range(minx, maxx):
            already = grid.get((x, y))
            if already and already[1] != -1 and already[0] not in infinites:
                infinites.add(already[0])

    for x in (minx, maxx-1):
        for y in range(miny, maxy):
            already = grid.get((x, y))
            if already and already[1] != -1 and already[0] not in infinites:
                infinites.add(already[0])

    areas = Counter()

    for x in range(minx, maxx):
        for y in range(miny, maxy):
            already = grid[(x, y)]
            if already[1] == -1 or already[0] in infinites:
                continue
            areas[already[0]] += 1

    return areas.most_common()[0][1]


def part1(points):
    minx = min(p[0] for p in points) - 1
    maxx = max(p[0] for p in points) + 2
    miny = min(p[1] for p in points) - 1
    maxy = max(p[1] for p in points) + 1

    # key: (x, y), value: (point that owns it, distance from point)
    grid = {}

    for idx, point in enumerate(points):
        grid[tuple(point)] = (idx, 0)

    for idx, point in enumerate(points):
        for x in range(minx, maxx):
            for y in range(miny, maxy):
                dist = distance(point, (x, y))
                if dist == 0:
                    continue
                already = grid.get((x, y))
                if not already:
                    grid[(x, y)] = (idx, dist)
                elif already[1] == 0:
                    pass
                elif dist < already[1]:
                    grid[(x, y)] = (idx, dist)
                elif already[1] == dist:
                    grid[(x, y)] = (-1, -1)

    return calcarea(grid, minx, maxx, miny, maxy)


def part2(points):
    minx = min(p[0] for p in points) - 1
    maxx = max(p[0] for p in points) + 2
    miny = min(p[1] for p in points) - 1
    maxy = max(p[1] for p in points) + 1

    distsum = Counter()
    for point in points:
        distsum[tuple(point)] = 0

    for idx, point in enumerate(points):
        for x in range(minx, maxx):
            for y in range(miny, maxy):
                dist = distance(point, (x, y))
                distsum[(x, y)] += dist

    return len([point for point in distsum if distsum[point] < 10000])


if __name__ == "__main__":
    input = [[int(x, 10) for x in line.strip().split(", ")] for line in open(join("resources", "input.txt"))]
    print(part1(input))
    print(part2(input))

# eof
