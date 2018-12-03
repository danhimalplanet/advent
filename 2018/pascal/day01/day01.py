d = list(map(int, open('input.txt').readlines()))

#part1
print(sum(d))

#part2
f = 0
h = {}
r = None
while r is None:
    for a in d:
        if f in h:
            r = f
            break
        h[f] = True
        f += a
print(r)