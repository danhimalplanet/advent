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

def turn(cur_direction, infected):
    if cur_direction == 'up' and infected == True:
        return 'right'
    elif cur_direction == 'right' and infected == True:
        return 'down'
    elif cur_direction == 'down' and infected == True:
        return 'left'
    elif cur_direction == 'left' and infected == True:
        return 'up'
    elif cur_direction == 'up' and infected == False:
        return 'left'
    elif cur_direction == 'left' and infected == False:
        return 'down'
    elif cur_direction == 'down' and infected == False:
        return 'right'
    elif cur_direction == 'right' and infected == False:
        return 'up'

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
        infected_by_carrier += 1
        return '#'
    elif node == '#':
        return '.'

while iterator < 10000:
    if infinite_grid[cur_y][cur_x] == '.':
        infected = False
    elif infinite_grid[cur_y][cur_x] == '#':
        infected = True
    cur_direction = turn(cur_direction, infected)
    infinite_grid[cur_y][cur_x] = infect_or_clean(infinite_grid[cur_y][cur_x])
    move(cur_direction)
    iterator += 1

print infected_by_carrier
