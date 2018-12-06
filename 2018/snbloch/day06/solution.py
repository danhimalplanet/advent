import io
import numpy as np

def part1():
    rows = 1000
    columns = 1000
    grid = np.full((rows, columns), None)
    counter = 0
    possible_winners = []
    areas = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            possible_winners.append(counter)
            pos_x = int(line.strip().split(', ')[0])
            pos_y = int(line.strip().split(', ')[1])
            cur_y = 0
            while cur_y < rows:
                cur_x = 0
                while cur_x < columns:
                    manhattan = abs(pos_y - cur_y) + abs(pos_x - cur_x)
                    if grid[cur_y][cur_x] is None:
                        grid[cur_y][cur_x] = (counter, manhattan)
                    elif grid[cur_y][cur_x][0] == 'eq':
                        if manhattan < grid[cur_y][cur_x][1]:
                            grid[cur_y][cur_x] = (counter, manhattan)
                    elif manhattan < grid[cur_y][cur_x][1]:
                        grid[cur_y][cur_x] = (counter, manhattan)
                    elif manhattan == grid[cur_y][cur_x][1]:
                        grid[cur_y][cur_x] = ('eq', manhattan)
                    cur_x += 1
                cur_y += 1
            counter += 1
    cur_y = 0
    while cur_y < rows:
        if grid[cur_y][0][0] in possible_winners:
            possible_winners.remove(grid[cur_y][0][0])
        if grid[cur_y][columns - 1][0] in possible_winners:
            possible_winners.remove(grid[cur_y][columns - 1][0])
        cur_y += 1
    cur_x = 0
    while cur_x < columns:
        if grid[0][cur_x][0] in possible_winners:
            possible_winners.remove(grid[0][cur_x][0])
        if grid[rows - 1][cur_x][0] in possible_winners:
            possible_winners.remove(grid[rows - 1][cur_x][0])
        cur_x += 1
    for i in possible_winners:
        area = 0
        cur_y = 0
        while cur_y < rows:
            cur_x = 0
            while cur_x < columns:
                if grid[cur_y][cur_x][0] == i:
                    area += 1
                cur_x += 1
            cur_y += 1
        areas.append(area)
    print 'Part 1: max area is',max(areas)

def part2():
    rows = 1000
    columns = 1000
    target = 10000
    grid = np.full((rows, columns), None)
    coordinates = []
    area = 0
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            pos_x = int(line.strip().split(', ')[0])
            pos_y = int(line.strip().split(', ')[1])
            coordinates.append((pos_x, pos_y))
        cur_y = 0
        while cur_y < rows:
            cur_x = 0
            while cur_x < columns:
                total_distance = 0
                for i in coordinates:
                    manhattan = abs(cur_y - i[1]) + abs(cur_x - i[0])
                    total_distance += manhattan
                if total_distance < target:
                    grid[cur_y][cur_x] = 'win'
                cur_x += 1
            cur_y += 1
    cur_y = 0
    while cur_y < rows:
        cur_x = 0
        while cur_x < columns:
            if grid[cur_y][cur_x] == 'win':
                area += 1
            cur_x += 1
        cur_y += 1
    print 'Part 2: total area is',area

if __name__ == '__main__':
    part1()
    part2()
