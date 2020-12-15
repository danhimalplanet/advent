def part1():
    values = [0,12,6,13,20,1,17]
    turn_counter = 1
    used = {}

    for i in values:
        used[i] = [turn_counter]
        turn_counter += 1
    
    while turn_counter < 2021:
        if len(used[values[-1]]) == 1:
            values.append(0)
            if 0 in used:
                used[0].append(turn_counter)
            else:
                used[0] = [turn_counter]
        else:
            diff = used[values[-1]][-1] - used[values[-1]][-2]
            values.append(diff)
            if diff in used:
                used[diff].append(turn_counter)
            else:
                used[diff] = [turn_counter]
        turn_counter += 1 
    
    print(values[-1])

def part2():
    values = [0,12,6,13,20,1,17]
    turn_counter = 1
    used = {}

    for i in values:
        used[i] = [turn_counter]
        turn_counter += 1
    
    while turn_counter < 30000001:
        if len(used[values[-1]]) == 1:
            values.append(0)
            if 0 in used:
                used[0].append(turn_counter)
            else:
                used[0] = [turn_counter]
        else:
            diff = used[values[-1]][-1] - used[values[-1]][-2]
            values.append(diff)
            if diff in used:
                used[diff].append(turn_counter)
            else:
                used[diff] = [turn_counter]
        turn_counter += 1 
    
    print(values[-1])

if __name__ == '__main__':
    part1()
    part2()