import io

instructions = []
prog0_registers = {}
prog1_registers = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'
prog0_position = 0
prog1_position = 0

prog0_queue = []
prog1_queue = []

prog0_running = True
prog1_running = True
prog0_sent_count = 0
prog1_sent_count = 0

file = open('input.txt', 'r')
for line in file:
    if line.split(' ')[1].strip() in alpha:
        if prog0_registers.get(line.split(' ')[1].strip()) == None:
            prog0_registers[line.split(' ')[1].strip()] = 0
file.close()

file = open('input.txt', 'r')
for line in file:
    if line.split(' ')[1].strip() in alpha:
        if prog1_registers.get(line.split(' ')[1].strip()) == None:
            prog1_registers[line.split(' ')[1].strip()] = 0
file.close()

prog0_registers['p'] = 0
prog1_registers['p'] = 1

file = open('input.txt', 'r')
for line in file:
    instructions.append(line)

def execute(program, position):
    global alpha
    global prog0_registers
    global prog1_registers
    global prog0_position
    global prog1_position
    global prog0_queue
    global prog1_queue
    global prog0_running
    global prog1_running
    global prog0_sent_count
    global prog1_sent_count
    line = instructions[position]
    operation = line.split(' ')[0].strip()
    if len(line.split(' ')) > 2:
        reg = line.split(' ')[1].strip()
        val = line.split(' ')[2].strip()
    else:
        reg_or_val = line.split(' ')[1].strip()

    if operation == 'snd':
        if program == 0:
            if reg_or_val in alpha:
                reg_or_val = int(prog0_registers[reg_or_val])
            else:
                reg_or_val = int(reg_or_val)
            prog1_queue.append(reg_or_val)
            prog0_sent_count += 1
            prog0_position += 1
        elif program == 1:
            if reg_or_val in alpha:
                reg_or_val = int(prog1_registers[reg_or_val])
            else:
                reg_or_val = int(reg_or_val)
            prog0_queue.append(reg_or_val)
            prog1_sent_count += 1
            prog1_position += 1

    elif operation == 'set':
        if program == 0:
            if val in alpha:
                val = prog0_registers[val]
            prog0_registers[reg] = int(val)
            prog0_position += 1
        elif program == 1:
            if val in alpha:
                val = prog1_registers[val]
            prog1_registers[reg] = int(val)
            prog1_position += 1

    elif operation == 'add':
        if program == 0:
            if val in alpha:
                val = prog0_registers[val]
            prog0_registers[reg] += int(val)
            prog0_position += 1
        elif program == 1:
            if val in alpha:
                val = prog1_registers[val]
            prog1_registers[reg] += int(val)
            prog1_position += 1

    elif operation == 'mul':
        if program == 0:
            if val in alpha:
                val = prog0_registers[val]
            prog0_registers[reg] *= int(val)
            prog0_position += 1
        elif program == 1:
            if val in alpha:
                val = prog1_registers[val]
            prog1_registers[reg] *= int(val)
            prog1_position += 1

    elif operation == 'mod':
        if program == 0:
            if val in alpha:
                val = prog0_registers[val]
            prog0_registers[reg] %= int(val)
            prog0_position += 1
        elif program == 1:
            if val in alpha:
                val = prog1_registers[val]
            prog1_registers[reg] %= int(val)
            prog1_position += 1

    elif operation == 'rcv':
        if program == 0:
            if len(prog0_queue) == 0:
                pass
            else:
                prog0_registers[reg_or_val] = int(prog0_queue.pop(0))
                prog0_position += 1
        elif program == 1:
            if len(prog1_queue) == 0:
                pass
            else:
                prog1_registers[reg_or_val] = int(prog1_queue.pop(0))
                prog1_position += 1

    elif operation == 'jgz':
        if program == 0:
            if reg in alpha:
                reg = prog0_registers[reg]
            if val in alpha:
                val = prog0_registers[val]
            if int(reg) > 0:
                prog0_position += int(val)
            else:
                prog0_position += 1
        if program == 1:
            if reg in alpha:
                reg = prog1_registers[reg]
            if val in alpha:
                val = prog1_registers[val]
            if int(reg) > 0:
                prog1_position += int(val)
            else:
                prog1_position += 1

    if program == 0:
        return prog0_position
    elif program == 1:
        return prog1_position

while prog0_running or prog1_running:
    if prog0_running:
        if prog0_position >= 0 and prog0_position < len(instructions):
            prog0_position = execute(0, prog0_position)
        else:
            print 'Program 0 ran out of bounds and is terminating'
            prog0_running = False
        if prog1_running == False and instructions[prog0_position].split(' ')[0] == 'rcv' and len(prog0_queue) == 0:
            print 'Program 0 tried to receive, queue was empty, and program 1 is not running.  Terminating.'
            prog0_running = False
    if prog1_running:
        if prog1_position >= 0 and prog1_position < len(instructions):
            prog1_position = execute(1, prog1_position)
        else:
            print 'Program 1 ran out of bounds and is terminating'
            prog1_running = False
        if prog0_running == False and instructions[prog1_position].split(' ')[0] == 'rcv' and len(prog1_queue) == 0:
            print 'Program 1 tried to receive, queue was empty, and program 0 is not running.  Terminating.'
            prog1_running = False
    if prog0_running and prog1_running:
        if instructions[prog0_position].split(' ')[0] == 'rcv' and len(prog0_queue) == 0:
            if instructions[prog1_position].split(' ')[0] == 'rcv' and len(prog1_queue) == 0:
                print 'Deadlock encountered!  Both programs tried to receive and both queues were empty.'
                prog0_running = False
                prog1_running = False

print 'Program 0 sent ', prog0_sent_count, 'instructions'
print 'Program 1 sent ', prog1_sent_count, 'instructions'
