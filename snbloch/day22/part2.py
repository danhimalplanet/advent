import io

input_grid = []

file = open('input.txt', 'r')
for line in file:
    input_grid.append(list(line.replace('\n', '')))

infinite_grid = []
width = 10000
height = 10000
count = 0
while count < height:
    infinite_grid.append(list('.' * width))
    count += 1

cur_y = (height / 2) - (len(input_grid) / 2)
count_y = 0
while count_y < len(input_grid):
    cur_x = (width / 2) - (len(input_grid[0]) / 2)
    count_x = 0
    while count_x < len(input_grid[0]):
        infinite_grid[cur_y][cur_x] = input_grid[count_y][count_x]
        count_x += 1
        cur_x += 1
    count_y += 1
    cur_y += 1

cur_x = (width / 2)
cur_y = (height / 2)

cur_direction = 'up'
infected_by_carrier = 0
iterator = 0

def turn(cur_direction, state):
    if cur_direction == 'up' and state == 'infected':
        return 'right'
    elif cur_direction == 'right' and state == 'infected':
        return 'down'
    elif cur_direction == 'down' and state == 'infected':
        return 'left'
    elif cur_direction == 'left' and state == 'infected':
        return 'up'
    elif cur_direction == 'up' and state == 'clean':
        return 'left'
    elif cur_direction == 'left' and state == 'clean':
        return 'down'
    elif cur_direction == 'down' and state == 'clean':
        return 'right'
    elif cur_direction == 'right' and state == 'clean':
        return 'up'
    elif cur_direction == 'up' and state == 'flagged':
        return 'down'
    elif cur_direction == 'left' and state == 'flagged':
        return 'right'
    elif cur_direction == 'down' and state == 'flagged':
        return 'up'
    elif cur_direction == 'right' and state == 'flagged':
        return 'left'
    elif cur_direction == 'up' and state == 'weakened':
        return 'up'
    elif cur_direction == 'left' and state == 'weakened':
        return 'left'
    elif cur_direction == 'down' and state == 'weakened':
        return 'down'
    elif cur_direction == 'right' and state == 'weakened':
        return 'right'

def move(cur_direction):
    global cur_x
    global cur_y
    if cur_direction == 'up':
        cur_y -= 1
    elif cur_direction == 'right':
        cur_x += 1
    elif cur_direction == 'down':
        cur_y += 1
    elif cur_direction == 'left':
        cur_x -= 1

def infect_or_clean(node):
    global infected_by_carrier
    if node == '.':
        return 'W'
    elif node == 'W':
        infected_by_carrier += 1
        return '#'
    elif node == '#':
        return 'F'
    elif node == 'F':
        return '.'

while iterator < 10000000:
    if infinite_grid[cur_y][cur_x] == '.':
        state = 'clean'
    elif infinite_grid[cur_y][cur_x] == '#':
        state = 'infected'
    elif infinite_grid[cur_y][cur_x] == 'W':
        state = 'weakened'
    elif infinite_grid[cur_y][cur_x] == 'F':
        state = 'flagged'
    cur_direction = turn(cur_direction, state)
    infinite_grid[cur_y][cur_x] = infect_or_clean(infinite_grid[cur_y][cur_x])
    move(cur_direction)
    iterator += 1

print infected_by_carrier
