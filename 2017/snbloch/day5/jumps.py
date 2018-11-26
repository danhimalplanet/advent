import io

f = open('input.txt', mode='r')

instructions = []
for line in f:
    instructions.append(int(line.strip()))

num_instructions = len(instructions)
position = 0
steps = 0

while position >= 0 and position < num_instructions:
    jump = instructions[position]
    instructions[position] = instructions[position] + 1
    position += jump
    steps += 1

print steps
