import numpy as np

import collections

d = np.loadtxt('input.txt', dtype=np.int, delimiter=',')

max_x = d.T[0].max()
max_y = d.T[1].max()
EDGE = 10000

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1]-b[1])

def closest(a):
    x = [ dist(a, b) for b in d ]
    amin = np.argmin(x)
    min = x[amin]

    if x.count(min) > 1:
        return EDGE, sum(x)
    return amin, sum(x)


grid = np.zeros((max_x, max_y), dtype=np.int)
sgrid = np.zeros((max_x, max_y), dtype=np.int)
for x in range(max_x):
    for y in range(max_y):
        grid[x, y], sgrid[x, y] = closest((x,y))

cnt = collections.Counter(grid.flatten())

# Build list of all numbers touching edges
edges = [ grid[0, :], grid[-1, :], grid[:,  0], grid[:, -1] ]
edges = list(set(np.array(edges).flatten()))
edges.append(EDGE)

sorts = cnt.items()
sorts = list(filter(lambda f: f[0] not in edges, sorts))
sorts.sort(key=lambda k: k[1])

# part1
print(sorts[-1][1])

# part2
print(sum(sgrid.flatten()<EDGE))
