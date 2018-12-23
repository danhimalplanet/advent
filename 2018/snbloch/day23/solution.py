import io
from collections import Counter

x_coords = []
y_coords = []
z_coords = []
ranges = []

with open('input.txt', 'r') as inputfile:
    for line in inputfile:
        position = line.strip().split('<')[1].split('>')[0].split(',')
        r = int(line.strip().split('r=')[1])
        x_coords.append(int(position[0]))
        y_coords.append(int(position[1]))
        z_coords.append(int(position[2]))
        ranges.append(r)

def part1():
    strongest_nanobot = None
    counter = 0
    while counter < len(ranges):
        if strongest_nanobot == None or ranges[counter] > ranges[strongest_nanobot]:
            strongest_nanobot = counter
        counter += 1
    in_range = 0
    counter = 0
    while counter < len(ranges):
        if abs(x_coords[strongest_nanobot] - x_coords[counter]) + abs(y_coords[strongest_nanobot] - y_coords[counter]) + abs(z_coords[strongest_nanobot] - z_coords[counter]) <= ranges[strongest_nanobot]:
            in_range += 1
        counter += 1
    print 'Part 1:', in_range, 'in range'

if __name__ == '__main__':
    part1()
