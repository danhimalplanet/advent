import io

f = open('input.txt', mode='r')
for line in f:
    directions = line
f.close()

steps = []

for i in directions.split(','):
    steps.append(i.strip())

coords_x = 0
coords_y = 0
coords_z = 0
max_distance = 0

def take_step(i):
    global coords_x
    global coords_y
    global coords_z
    if i == 'n':
        coords_y += 1
        coords_z -= 1
    elif i == 's':
        coords_y -= 1
        coords_z += 1
    elif i == 'ne':
        coords_x += 1
        coords_z -= 1
    elif i == 'sw':
        coords_x -= 1
        coords_z += 1
    elif i == 'nw':
        coords_x -= 1
        coords_y += 1
    elif i == 'se':
        coords_x += 1
        coords_y -= 1

for i in steps:
    take_step(i)
    total_distance = (abs(coords_x) + abs(coords_y) + abs(coords_z)) / 2
    if total_distance > max_distance:
        max_distance = total_distance

print 'Total Distance: ', total_distance
print 'Maximum Distance: ', max_distance
