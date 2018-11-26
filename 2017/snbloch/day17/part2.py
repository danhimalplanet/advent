input = 337
cur_position = 0
buffer = []
buffer.append(0)

for i in range(1, 50000001):
    cur_position = (cur_position + input) % i + 1
    if cur_position == 1:
        buffer.append(i)
print buffer[-1]
