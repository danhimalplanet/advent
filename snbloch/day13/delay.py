import io
file = open('input.txt', 'r')

input = {}
scanners_pos = {}
scanners_direction = {}

for line in file:
    depth = int(line.split(': ')[0])
    range = int(line.split(': ')[1])
    input[depth] = range

delay = 0
firewall_length = max(input.iterkeys())

caught_bool = True
while caught_bool == True:
    for i in input.iterkeys():
        scanners_pos[i] = 1
        scanners_direction[i] = 'down'
    curr_depth = -1 - (delay)
    caught = []
    while curr_depth <= firewall_length:
        curr_depth += 1
        if scanners_pos.get(curr_depth) == 1:
            caught.append(curr_depth)
        for depth, range in input.iteritems():
            if scanners_pos[depth] == range and scanners_direction[depth] == 'down':
                scanners_direction[depth] = 'up'
                scanners_pos[depth] -= 1
            elif scanners_direction[depth] == 'down':
                scanners_pos[depth] += 1
            elif scanners_pos[depth] == 1 and scanners_direction[depth] == 'up':
                scanners_direction[depth] = 'down'
                scanners_pos[depth] += 1
            elif scanners_direction[depth] == 'up':
                scanners_pos[depth] -= 1
    if len(caught) == 0:
        caught_bool = False
        print delay
    else:
        delay += 1
