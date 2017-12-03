direction = ''
n = 325489
cur_x = 0
cur_y = 0
min_x = 0
min_y = 0
max_x = 0
max_y = 0
for i in range(1, n):
    print i, 'min_x: ', min_x, 'cur_x: ', cur_x, 'max_x: ', max_x, 'min_y: ', min_y, 'cur_y: ', cur_y, 'max_y: ', max_y, direction
    if cur_x <= max_x and cur_y == min_y:
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

print 'Manhattan Distance = ', abs(cur_x) + abs(cur_y)
