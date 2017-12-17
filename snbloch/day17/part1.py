input = 337
cur_position = 0
insert_value = 1
buffer = []
buffer.append(0)

def spin(steps):
    global cur_position
    global buffer
    global insert_value
    counter = 0
    while counter < steps:
        if cur_position == len(buffer) - 1:
            cur_position = 0
        else:
            cur_position += 1
        counter += 1
    if cur_position == len(buffer):
        buffer.insert(0, insert_value)
        cur_position = 0
    else:
        buffer.insert(cur_position + 1, insert_value)
        cur_position += 1
    insert_value += 1
    return

i = 0
while i < 2017:
    spin(input)
    i += 1

print buffer[cur_position + 1]
