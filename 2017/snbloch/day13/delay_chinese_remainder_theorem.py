import io, sys
file = open('input.txt', 'r')

input = {}

for line in file:
    depth = int(line.split(': ')[0])
    range_value = int(line.split(': ')[1])
    input[depth] = range_value

delay = 0
caught_bool = True
while caught_bool == True:
    caught_bool = False
    for i in input.keys():
        if (i + delay) % (2 * (input[i] - 1)) == 0:
            caught_bool = True
            delay += 1
            break

print delay
