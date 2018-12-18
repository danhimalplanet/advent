import io
import numpy as np

width = 50
height = 50
open_space = '.'
tree = '|'
lumberyard = '#'

def transform(grid):
    new_grid = np.full((height, width), None)
    cur_y = 0
    while cur_y < height:
        cur_x = 0
        while cur_x < width:
            if grid[cur_y][cur_x] == open_space:
                tree_count = 0
                if cur_y >= 1 and cur_y < height - 1:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    else:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                elif cur_y >= 1:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    else:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                else:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    else:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == tree:
                                    tree_count += 1
                if tree_count >= 3:
                    new_grid[cur_y][cur_x] = tree
                else:
                    new_grid[cur_y][cur_x] = grid[cur_y][cur_x]
            if grid[cur_y][cur_x] == tree:
                lumberyard_count = 0
                if cur_y >= 1 and cur_y < height - 1:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                    else:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                if grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                elif cur_y >= 1:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                    else:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                else:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                    else:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                if lumberyard_count >= 3:
                    new_grid[cur_y][cur_x] = lumberyard
                else:
                    new_grid[cur_y][cur_x] = grid[cur_y][cur_x]
            if grid[cur_y][cur_x] == lumberyard:
                lumberyard_count = 0
                tree_count = 0
                if cur_y >= 1 and cur_y < height - 1:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    else:
                        for y in range(cur_y - 1, cur_y + 2):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                elif cur_y >= 1:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    else:
                        for y in range(cur_y - 1, cur_y + 1):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                else:
                    if cur_x >= 1 and cur_x < width - 1:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    elif cur_x >= 1:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x - 1, cur_x + 1):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                    else:
                        for y in range(cur_y, cur_y + 2):
                            for x in range(cur_x, cur_x + 2):
                                if y == cur_y and x == cur_x:
                                    continue
                                elif grid[y][x] == lumberyard:
                                    lumberyard_count += 1
                                elif grid[y][x] == tree:
                                    tree_count += 1
                if lumberyard_count >= 1 and tree_count >= 1:
                    new_grid[cur_y][cur_x] = grid[cur_y][cur_x]
                else:
                    new_grid[cur_y][cur_x] = open_space
            cur_x += 1
        cur_y += 1
    return new_grid

def part1():
    grid = np.full((height, width), None)
    with open('input.txt', 'r') as inputfile:
        cur_y = 0
        for line in inputfile:
            cur_x = 0
            for i in line.strip():
                grid[cur_y][cur_x] = i
                cur_x += 1
            cur_y += 1
    generation_count = 0
    while generation_count < 10:
        grid = transform(grid)
        generation_count += 1
    tree_count = 0
    lumberyard_count = 0
    cur_y = 0
    while cur_y < height:
        cur_x = 0
        while cur_x < width:
            if grid[cur_y][cur_x] == tree:
                tree_count += 1
            elif grid[cur_y][cur_x] == lumberyard:
                lumberyard_count += 1
            cur_x += 1
        cur_y += 1
    print 'Part 1: total resource count is',tree_count * lumberyard_count

def part2():
    grid = np.full((height, width), None)
    with open('input.txt', 'r') as inputfile:
        cur_y = 0
        for line in inputfile:
            cur_x = 0
            for i in line.strip():
                grid[cur_y][cur_x] = i
                cur_x += 1
            cur_y += 1
    generation_count = 0
    print 'Part 2:'
    while generation_count < 1000:
        grid = transform(grid)
        generation_count += 1
        tree_count = 0
        lumberyard_count = 0
        cur_y = 0
        while cur_y < height:
            cur_x = 0
            while cur_x < width:
                if grid[cur_y][cur_x] == tree:
                    tree_count += 1
                elif grid[cur_y][cur_x] == lumberyard:
                    lumberyard_count += 1
                cur_x += 1
            cur_y += 1
        print 'Generation:',generation_count,'Resource count:',tree_count * lumberyard_count
    '''
    pattern starts after generation 566
    cycle of 28

    999999434 cycles of pattern to make 1000000000 total generations
    999999434 % 28 == 14

    15th element of cycle (14 after zeroth) is 219919
    '''
if __name__ == '__main__':
    part1()
    part2()
