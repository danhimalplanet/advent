from collections import Counter

tape = []
tape_length = 15000000
state = 'A'
cursor = 0

def move_position(direction):
    global cursor
    global tape
    if direction == 'left':
        if cursor == 0:
            cursor = len(tape) - 1
        else:
            cursor -= 1
    elif direction == 'right':
        if cursor == len(tape) - 1:
            cursor = 0
        else:
            cursor += 1

counter = 0
while counter < tape_length:
    tape.append(0)
    counter += 1

counter = 0
while counter < 12994925:
    if state == 'A':
        if tape[cursor] == 0:
            tape[cursor] = 1
            move_position('right')
            state = 'B'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            move_position('left')
            state = 'F'
    elif state == 'B':
        if tape[cursor] == 0:
            tape[cursor] = 0
            move_position('right')
            state = 'C'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            move_position('right')
            state = 'D'
    elif state == 'C':
        if tape[cursor] == 0:
            tape[cursor] = 1
            move_position('left')
            state = 'D'
        elif tape[cursor] == 1:
            tape[cursor] = 1
            move_position('right')
            state = 'E'
    elif state == 'D':
        if tape[cursor] == 0:
            tape[cursor] = 0
            move_position('left')
            state = 'E'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            move_position('left')
            state = 'D'
    elif state == 'E':
        if tape[cursor] == 0:
            tape[cursor] = 0
            move_position('right')
            state = 'A'
        elif tape[cursor] == 1:
            tape[cursor] = 1
            move_position('right')
            state = 'C'
    elif state == 'F':
        if tape[cursor] == 0:
            tape[cursor] = 1
            move_position('left')
            state = 'A'
        elif tape[cursor] == 1:
            tape[cursor] = 1
            move_position('right')
            state = 'A'
    counter += 1

print Counter(tape)
