import math
import numpy

direction = ''
n = 325489
width = n
height = n
cur_x = width / 2
cur_y = height / 2
min_x = width / 2
min_y = height / 2
max_x = width / 2
max_y = height / 2
grid = numpy.zeros(shape=(width, height), dtype=int)
grid[cur_x][cur_y] = 1
sum = 1
while sum < n:
        print 'max_x: ', min_x, 'cur_x: ', cur_x, 'max_x: ', max_x, 'min_y: ', min_y, 'cur_y: ', cur_y, 'max_y: ', max_y, direction, sum
        if cur_x <= min_x and cur_y == min_y:
            if direction != 'right':
                direction = 'right'
                max_x += 1
        if cur_x == max_x and cur_y <= max_y:
            if direction != 'up':
                direction = 'up'
                max_y += 1
        if cur_x > min_x and cur_y == max_y:
            if direction != 'left':
                direction = 'left'
                min_x -= 1
        if cur_x == min_x and cur_y > min_y:
            if direction != 'down':
                direction = 'down'
                min_y -= 1
        if direction == 'right':
            cur_x += 1
        if direction == 'up':
            cur_y += 1
        if direction == 'left':
            cur_x -= 1
        if direction == 'down':
            cur_y -= 1
        grid[cur_x][cur_y] = grid[cur_x - 1][cur_y - 1] + grid[cur_x - 1][cur_y] + grid[cur_x - 1][cur_y + 1] + grid[cur_x][cur_y - 1] + grid[cur_x][cur_y + 1] + grid[cur_x + 1][cur_y - 1] + grid[cur_x + 1][cur_y] + grid[cur_x + 1][cur_y + 1]
        sum = grid[cur_x][cur_y]

print sum
