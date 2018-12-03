import numpy as np

d = open('input.txt').readlines()

# For easy reference
X=0; Y=1; W=2; H=3
claims = np.zeros((4,len(d)), dtype=np.int)

# Populate claims table
for i, s in enumerate(d):
    claims[X][i] = int(s.split()[2][:-1].split(',')[0])
    claims[Y][i] = int(s.split()[2][:-1].split(',')[1])
    claims[W][i] = int(s.split()[3].split('x')[0])
    claims[H][i] = int(s.split()[3].split('x')[1])

# get max coords
x_max = int(max(claims[X] + claims[W]))
y_max = int(max(claims[Y] + claims[H]))

# create cloth
cloth = np.zeros((x_max, y_max), dtype=np.int8)

# populate cloth
for i in range(claims.shape[1]):
    x1 = claims[X][i]
    x2 = claims[X][i] + claims[W][i]
    y1 = claims[Y][i]
    y2 = claims[Y][i] + claims[H][i]
    cloth[x1:x2,y1:y2] += 1

# Count overlapping claims
x = cloth > 1
print(sum(x.flatten()))

# part2
for i in range(claims.shape[1]):
    x1 = claims[X][i]
    x2 = claims[X][i] + claims[W][i]
    y1 = claims[Y][i]
    y2 = claims[Y][i] + claims[H][i]
    s = sum(cloth[x1:x2,y1:y2].flatten())
    if s == claims[W][i] * claims[H][i]:
        print(i+1)
        break
