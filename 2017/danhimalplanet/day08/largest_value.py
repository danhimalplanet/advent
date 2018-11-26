#!/usr/bin/env python3

"""
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""

import operator

globvar = 0

f = open("sample_input.txt", 'r')
#f = open("puzzle_input.txt", 'r')

instructions = []

for i in f:
    instructions.append(i.strip('\n'))

registers = {}
bigmax = 0

def parse(instruction):
    global bigmax
    raw = instruction.split()
    compare = raw[4]
    value = int(raw[6])

    if compare not in registers:
        registers[compare] = 0

    ops = { '>': operator.gt(registers[compare], value),
            '<': operator.lt(registers[compare], value),
            '>=': operator.ge(registers[compare], value),
            '<=': operator.le(registers[compare], value),
            '==': operator.eq(registers[compare], value),
            '!=': operator.ne(registers[compare], value),
            }

    if ops[raw[5]]:
        target = raw[0]
        if target not in registers:
            registers[target] = 0
        if raw[1] == "inc":
            bigsum = registers[target] + int(raw[2])
            registers[target] = bigsum
            if bigsum > bigmax:
                bigmax = bigsum
        else:
            bigsum = registers[target] - int(raw[2])
            registers[target] = bigsum
            if bigsum > bigmax:
                bigmax = bigsum

for instruction in instructions:
    parse(instruction)

#print(registers)

v, k = max((v, k) for k, v in registers.items())

print(v)
print(bigmax)
