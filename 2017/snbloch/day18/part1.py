import io

instructions = []
registers = {}
played = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
position = 0

file = open('input.txt', 'r')
for line in file:
    if line.split(' ')[1].strip() in alpha:
        if registers.get(line.split(' ')[1].strip()) == None:
            registers[line.split(' ')[1].strip()] = 0
file.close()

file = open('input.txt', 'r')
for line in file:
    instructions.append(line)

def execute(position):
    global alpha
    global registers
    global played
    line = instructions[position]
    operation = line.split(' ')[0].strip()
    if len(line.split(' ')) > 2:
        reg = line.split(' ')[1].strip()
        val = line.split(' ')[2].strip()
    else:
        reg_or_val = line.split(' ')[1].strip()

    if operation == 'snd':
        if reg_or_val in alpha:
            played.append(int(registers[reg_or_val]))
        else:
            played.append(int(reg_or_val))
        position += 1

    elif operation == 'set':
        if val in alpha:
            val = registers[val]
        registers[reg] = int(val)
        position += 1

    elif operation == 'add':
        if val in alpha:
            val = registers[val]
        registers[reg] += int(val)
        position += 1

    elif operation == 'mul':
        if val in alpha:
            val = registers[val]
        registers[reg] *= int(val)
        position += 1

    elif operation == 'mod':
        if val in alpha:
            val = registers[val]
        registers[reg] %= int(val)
        position += 1

    elif operation == 'rcv':
        if reg_or_val in alpha:
            reg_or_val = registers[reg_or_val]
        if int(reg_or_val) != 0:
            recovered = played[len(played) - 1]
            print 'Recovered: ', recovered
        position += 1

    elif operation == 'jgz':
        if reg in alpha:
            reg = registers[reg]
        if int(reg) > 0:
            position += int(val)
        else:
            position += 1

    return position

while position >= 0 and position < len(instructions):
    position = execute(position)
