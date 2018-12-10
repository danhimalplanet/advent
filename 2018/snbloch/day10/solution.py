import io
import numpy as np

def part1():
    positions = []
    velocities = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            position_x = int(line[10:16].strip())
            position_y = int(line[18:24].strip())
            velocity_x = int(line[36:38].strip())
            velocity_y = int(line[40:42])
            positions.append([position_x, position_y])
            velocities.append((velocity_x, velocity_y))
    finished = False
    while finished == False:
        counter = 0
        while counter < len(positions):
            positions[counter][0] += velocities[counter][0]
            positions[counter][1] += velocities[counter][1]
            counter += 1
        rows = set()
        for i in positions:
            rows.add(i[1])
        if len(rows) == 10:
            finished = True
    grid = np.full((1000, 1000), '.')
    for i in positions:
        grid[i[1]][i[0]] = '#'
    np.savetxt('output.txt', grid, '%s')
    print 'Part 1: look in output.txt'

def part2():
    ticks = 0
    positions = []
    velocities = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            position_x = int(line[10:16].strip())
            position_y = int(line[18:24].strip())
            velocity_x = int(line[36:38].strip())
            velocity_y = int(line[40:42])
            positions.append([position_x, position_y])
            velocities.append((velocity_x, velocity_y))
    finished = False
    while finished == False:
        ticks += 1
        counter = 0
        while counter < len(positions):
            positions[counter][0] += velocities[counter][0]
            positions[counter][1] += velocities[counter][1]
            counter += 1
        rows = set()
        for i in positions:
            rows.add(i[1])
        if len(rows) == 10:
            finished = True
    print 'Part 2: message took',ticks,'seconds to appear'

if __name__ == '__main__':
    part1()
    part2()
