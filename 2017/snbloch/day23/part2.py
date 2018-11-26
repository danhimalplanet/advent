import io

instructions = []
registers = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'
position = 0
mul_counter = 0

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
    global mul_counter
    line = instructions[position]
    operation = line.split(' ')[0].strip()
    if len(line.split(' ')) > 2:
        reg = line.split(' ')[1].strip()
        val = line.split(' ')[2].strip()
    else:
        reg_or_val = line.split(' ')[1].strip()

    if operation == 'set':
        if val in alpha:
            val = registers[val]
        registers[reg] = int(val)
        position += 1

    elif operation == 'sub':
        if val in alpha:
            val = registers[val]
        registers[reg] -= int(val)
        position += 1

    elif operation == 'mul':
        if val in alpha:
            val = registers[val]
        registers[reg] *= int(val)
        position += 1
        mul_counter += 1

    elif operation == 'jnz':
        if reg in alpha:
            reg = registers[reg]
        if val in alpha:
            val = registers[val]
        if int(reg) != 0:
            position += int(val)
        else:
            position += 1

    return position

registers['a'] = 1
counter = 0

# Magic numbers here correspond to my own b and c registers when the
# program is seemingly caught in an infinite loop, but in reality
# the program is counting composite numbers between registers b and c,
# in jumps of size 17
for num in range(106500,123500 + 1,17):
  for i in range(2,num):
    if (num % i) == 0:
      counter += 1
      break
print counter
