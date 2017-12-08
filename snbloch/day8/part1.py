import io

registers = {}

f = open('input.txt', mode='r')
for line in f:
    registers[line.split(' ')[0]] = 0
    registers[line.split(' ')[4]] = 0
f.close()

f = open('input.txt', mode='r')
for line in f:
    reg = line.split(' ')[0]
    action = line.split(' ')[1]
    value = int(line.split(' ')[2])
    condition_reg = line.split(' ')[4]
    condition = line.split(' ')[5]
    condition_value = int(line.split(' ')[6])
    if action == 'inc':
        if condition == '<':
            if registers[condition_reg] < condition_value:
                registers[reg] += value
        if condition == '<=':
            if registers[condition_reg] <= condition_value:
                registers[reg] += value
        if condition == '==':
            if registers[condition_reg] == condition_value:
                registers[reg] += value
        if condition == '>=':
            if registers[condition_reg] >= condition_value:
                registers[reg] += value
        if condition == '>':
            if registers[condition_reg] > condition_value:
                registers[reg] += value
        if condition == '!=':
            if registers[condition_reg] != condition_value:
                registers[reg] += value
    if action == 'dec':
        if condition == '<':
            if registers[condition_reg] < condition_value:
                registers[reg] -= value
        if condition == '<=':
            if registers[condition_reg] <= condition_value:
                registers[reg] -= value
        if condition == '==':
            if registers[condition_reg] == condition_value:
                registers[reg] -= value
        if condition == '>=':
            if registers[condition_reg] >= condition_value:
                registers[reg] -= value
        if condition == '>':
            if registers[condition_reg] > condition_value:
                registers[reg] -= value
        if condition == '!=':
            if registers[condition_reg] != condition_value:
                registers[reg] -= value

max_value = None
for r in registers:
    if max_value == None:
        max_value = registers[r]
    elif registers[r] > max_value:
        max_value = registers[r]

print max_value
