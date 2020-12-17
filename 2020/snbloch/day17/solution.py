from itertools import product

def part1():
    values = {}
    with open('input.txt', 'r') as inputfile:
        y = 0
        for line in inputfile:
            x = 0
            for i in line.strip():
                values[(x,y,0)] = i
                x += 1
            y += 1
    for _ in range(6):
        result = []
        new_values = values.copy()
        for i in values:
            for x,y,z in product(range(i[0] - 1, i[0] + 2), range(i[1] - 1, i[1] + 2), range(i[2] - 1, i[2] + 2)):
                if (x,y,z) not in new_values:
                    new_values[(x,y,z)] = '.'
        for i in new_values:
            neighbors_active = 0
            for x,y,z in product(range(i[0] - 1, i[0] + 2), range(i[1] - 1, i[1] + 2), range(i[2] - 1, i[2] + 2)):
                if (x,y,z) not in new_values:
                    continue
                elif (x,y,z) == (i[0],i[1],i[2]):
                    continue
                elif new_values[(x,y,z)] == '#':
                    neighbors_active += 1
            result.append((i[0], i[1], i[2], new_values[(i[0], i[1], i[2])], neighbors_active))
        for i in result:
            if i[3] == '#':
                if i[4] != 2 and i[4] != 3:
                    new_values[(i[0],i[1],i[2])] = '.'
            elif i[3] == '.':
                if i[4] == 3:
                    new_values[(i[0],i[1],i[2])] = '#'
        values = new_values
    active_at_end = 0
    for i in values:
        if values[i] == '#':
            active_at_end += 1
    print(active_at_end)

def part2():
    values = {}
    with open('input.txt', 'r') as inputfile:
        y = 0
        for line in inputfile:
            x = 0
            for i in line.strip():
                values[(x,y,0,0)] = i
                x += 1
            y += 1
    for _ in range(6):
        result = []
        new_values = values.copy()
        for i in values:
            for x,y,z,w in product(range(i[0] - 1, i[0] + 2), range(i[1] - 1, i[1] + 2), range(i[2] - 1, i[2] + 2), range(i[3] - 1, i[3] + 2)):
                if (x,y,z,w) not in new_values:
                    new_values[(x,y,z,w)] = '.'
        for i in new_values:
            neighbors_active = 0
            for x,y,z,w in product(range(i[0] - 1, i[0] + 2), range(i[1] - 1, i[1] + 2), range(i[2] - 1, i[2] + 2), range(i[3] - 1, i[3] + 2)):
                if (x,y,z,w) not in new_values:
                    continue
                elif (x,y,z,w) == (i[0],i[1],i[2],i[3]):
                    continue
                elif new_values[(x,y,z,w)] == '#':
                    neighbors_active += 1
            result.append((i[0], i[1], i[2], i[3], new_values[(i[0], i[1], i[2], i[3])], neighbors_active))
        for i in result:
            if i[4] == '#':
                if i[5] != 2 and i[5] != 3:
                    new_values[(i[0],i[1],i[2],i[3])] = '.'
            elif i[4] == '.':
                if i[5] == 3:
                    new_values[(i[0],i[1],i[2],i[3])] = '#'
        values = new_values
    active_at_end = 0
    for i in values:
        if values[i] == '#':
            active_at_end += 1
    print(active_at_end)

if __name__ == '__main__':
    part1()
    part2()