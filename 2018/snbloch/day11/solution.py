import numpy as np

grid_serial = 2694

def compute_power(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial
    power_level *= rack_id
    power_level = str(power_level)
    if len(power_level) < 3:
        power_level = 0
    else:
        power_level = int(power_level[-3])
    power_level -= 5
    return power_level

def part1():
    width = 300
    height = 300
    grid = np.zeros((width + 1, height + 1))
    cur_y = 1
    while cur_y <= height:
        cur_x = 1
        while cur_x <= width:
            grid[cur_y][cur_x] = compute_power(cur_x, cur_y)
            cur_x += 1
        cur_y += 1
    max_subgrid = None
    max_x = None
    max_y = None
    cur_y = 0
    while cur_y <= height - 2:
        cur_x = 0
        while cur_x <= width - 2:
            cur_subgrid = grid[cur_y][cur_x] + grid[cur_y][cur_x + 1] + grid[cur_y][cur_x + 2] + grid[cur_y + 1][cur_x] + grid[cur_y + 1][cur_x + 1] + grid[cur_y + 1][cur_x + 2] + grid[cur_y + 2][cur_x] + grid[cur_y + 2][cur_x + 1] + grid[cur_y + 2][cur_x + 2]
            if max_subgrid is None:
                max_subgrid = cur_subgrid
                max_x = cur_x
                max_y = cur_y
            elif cur_subgrid > max_subgrid:
                max_subgrid = cur_subgrid
                max_x = cur_x
                max_y = cur_y
            cur_x += 1
        cur_y += 1
    print 'Part 1: Max power level of any 3x3 grid starts at:',max_x,',',max_y

def part2():
    width = 300
    height = 300
    grid = np.zeros((width + 1, height + 1))
    cur_y = 1
    while cur_y <= height:
        cur_x = 1
        while cur_x <= width:
            grid[cur_y][cur_x] = compute_power(cur_x, cur_y)
            cur_x += 1
        cur_y += 1
    max_subgrid = None
    max_x = None
    max_y = None
    max_size = None
    size = 1
    while size <= width:
        cur_y = 1
        while cur_y <= height - size:
            cur_x = 1
            while cur_x <= width - size:
                cur_subgrid = int(np.sum(grid[cur_y:cur_y + size, cur_x:cur_x + size]))
                if max_subgrid is None:
                    max_subgrid = cur_subgrid
                    max_x = cur_x
                    max_y = cur_y
                    max_size = size
                elif cur_subgrid > max_subgrid:
                    max_subgrid = cur_subgrid
                    max_x = cur_x
                    max_y = cur_y
                    max_size = size
                cur_x += 1
            cur_y += 1
        size += 1
    print 'Part 2: Max power level of any grid has coordinates:',max_x,',',max_y,',',max_size

if __name__ == '__main__':
    part1()
    part2()
