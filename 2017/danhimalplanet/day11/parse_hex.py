#!/usr/bin/env python3

from collections import defaultdict

f = open("in.txt", "r")

vals = f.readline()

vals = vals.strip('\n').split(",")

directions1=['ne', 'ne', 'ne']
directions2=['ne', 'ne', 'sw', 'sw']
directions3=['ne', 'ne', 's', 's']
directions4=['se', 'sw', 'se', 'sw', 'sw']

def parse_hex_directions(directions):

    x = 0 
    y = 0
    z = 0

    distance = []

    for direction in directions:
        if direction == "ne":
            x += 1
            z -= 1
        if direction == "sw":
            x -= 1
            z += 1
        if direction == "n":
            y += 1
            z -= 1
        if direction == "s":
            y -= 1
            z += 1
        if direction == "nw":
            x -= 1
            y += 1
        if direction == "se":
            x += 1
            y -= 1
    print(abs(x))
    print(abs(y))
    print(abs(z))

    distance.append(abs(x))
    distance.append(abs(y))
    distance.append(abs(z))
    #print(distance)

#    print(abs(x) + abs(y) + abs(z)  / 2)
#    print(max(distance))

    return max(distance)

print("ANSWER SHOULD BE 3")
print("Final score:", parse_hex_directions(directions1))
print("ANSWER SHOULD BE 0")
print("Final score:", parse_hex_directions(directions2))
print("ANSWER SHOULD BE 2")
print("Final score:", parse_hex_directions(directions3))
print("ANSWER SHOULD BE 3")
print("Final score:", parse_hex_directions(directions4))

print("part 1:")
print("Final score:", parse_hex_directions(vals))
