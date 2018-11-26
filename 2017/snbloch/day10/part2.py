lengths = '94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243'
ascii_input = []
for i in lengths:
    ascii_input.append(ord(i))
suffix = '17,31,73,47,23'
for i in suffix.split(','):
    ascii_input.append(int(i))
print ascii_input

list_length = 256
output = range(list_length)
current_position = 0
skip_size = 0
select = []
reverse = []
num_rounds = 64
execution_round = 0

while execution_round < num_rounds:
    for i in ascii_input:
        del select[:]
        current_length = i

        counter = 0
        select_position = current_position
        while counter < current_length:
            select.append(output[select_position])
            if select_position + 1 >= len(output):
                select_position = 0
            else:
                select_position += 1
            counter += 1

        del reverse[:]
        counter = 0
        reverse_position = len(select) - 1
        while counter < len(select):
            reverse.append(select[reverse_position])
            counter += 1
            reverse_position -= 1

        counter = 0
        while counter < len(reverse):
            output[current_position] = reverse[counter]
            if current_position + 1 >= len(output):
                current_position = 0
            else:
                current_position += 1
            counter += 1
        print 'Execution Round: ', execution_round
        print 'Output: ', output

        skip_size = skip_size % list_length
        if current_position + skip_size >= len(output):
            current_position = skip_size - (len(output) - current_position)
        else:
            current_position += skip_size

        skip_size += 1
    execution_round += 1

sparse_hash = output
dense_hash_rounds = list_length / 16
dense_hash_rounds_complete = 0
dense_hash = []
while dense_hash_rounds_complete < dense_hash_rounds:
    dense_hash.append(dense_hash_rounds_complete)
    dense_hash[dense_hash_rounds_complete] = 0
    hash_start = dense_hash_rounds_complete * 16
    hash_end = hash_start + 16
    hash_position = hash_start
    while hash_position < hash_end:
        dense_hash[dense_hash_rounds_complete] ^= sparse_hash[hash_position]
        hash_position += 1
        print 'Hash position: ', hash_position
        print dense_hash[dense_hash_rounds_complete]
    dense_hash_rounds_complete += 1

dense_hash_hex = []
for i in dense_hash:
    dense_hash_hex.append(hex(i))

print dense_hash_hex
