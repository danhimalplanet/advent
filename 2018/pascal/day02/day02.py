import collections

c = [x.strip() for x in open('input.txt').readlines()]

# part1
c1 = [collections.Counter(x).values() for x in c]
c2 = [(2 in x, 3 in x) for x in c1]
c3 = list(zip(*c2))
print(sum(c3[0] * sum(c3[1])))

# part2
# I suspect this has edge cases due to ambiguities in
# input constraints
import numpy as np

d1 = np.array( [ list(map(ord, x)) for x in c ] )
u1 = set(d1[:,0])
u1c = []

for u in u1:
    x = list(filter(lambda f: f[0] == u, d1))
    comp = np.tril_indices(len(x), -1)
    for i, j in zip(*comp):
        delta = np.nonzero(x[i] - x[j])
        if len(delta[0]) == 1:
            u1c.append((x[i], delta[0][0]))
            u1c.append((x[j], delta[0][0]))

x = list(u1c[0][0])
x.pop(u1c[0][1])
print(''.join(map(chr, x)))
