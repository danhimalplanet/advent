import numpy as np

depth = 11820
target_x = 7
target_y = 782

def compute_geologic_index(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == target_x and y == target_y:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosion_levels[y][x-1] * erosion_levels[y-1][x]

def compute_erosion_level(x, y):
    return (geologic_indexes[y][x] + depth) % 20183

def determine_type(x, y):
    if erosion_levels[y][x] % 3 == 0:
        return 'rocky'
    elif erosion_levels[y][x] % 3 == 1:
        return 'wet'
    elif erosion_levels[y][x] % 3 == 2:
        return 'narrow'

def part1():
    risk_level = 0
    global geologic_indexes
    global erosion_levels
    geologic_indexes = np.zeros((target_y + 1, target_x + 1))
    erosion_levels = np.zeros((target_y + 1, target_x + 1))
    types = np.full((target_y + 1, target_x + 1), None)
    cur_y = 0
    while cur_y <= target_y:
        cur_x = 0
        while cur_x <= target_x:
            geologic_indexes[cur_y][cur_x] = compute_geologic_index(cur_x, cur_y)
            erosion_levels[cur_y][cur_x] = compute_erosion_level(cur_x, cur_y)
            types[cur_y][cur_x] = determine_type(cur_x, cur_y)
            if types[cur_y][cur_x] == 'wet':
                risk_level += 1
            elif types[cur_y][cur_x] == 'narrow':
                risk_level += 2
            cur_x += 1
        cur_y += 1
    print 'Part 1: Total risk level is',risk_level

if __name__ == '__main__':
    part1()
