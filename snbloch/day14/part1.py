num_rows = 128
row_counter = 0
input_string = 'jxqlasbh'
ascii_input = {}
hashes = []

while row_counter < num_rows:
    ascii_row_string = []
    row_string = input_string + '-' + str(row_counter)
    for i in row_string:
        ascii_row_string.append(ord(i))
    suffix = '17,31,73,47,23'
    for i in suffix.split(','):
        ascii_row_string.append(int(i))
    ascii_input[row_counter] = ascii_row_string
    row_counter += 1

row_counter = 0
while row_counter < num_rows:

    list_length = 256
    output = range(list_length)
    current_position = 0
    skip_size = 0
    select = []
    reverse = []
    num_rounds = 64
    execution_round = 0

    while execution_round < num_rounds:
        for i in ascii_input[row_counter]:
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
        dense_hash_rounds_complete += 1

    dense_hash_hex = []
    for i in dense_hash:
        dense_hash_hex.append(hex(i))
    hex_counter = 0
    while hex_counter < len(dense_hash_hex):
        dense_hash_hex[hex_counter] = dense_hash_hex[hex_counter].replace('0x', '')
        hex_counter += 1
    hash_output = ''
    for i in dense_hash_hex:
        if len(i) == 1:
            hash_output = hash_output + '0' + i
        else:
            hash_output = hash_output + i
    hashes.append(hash_output)
    row_counter += 1

binary_hashes = []
for i in hashes:
    binary_hashes.append(bin(int(i, 16))[2:])

used_counter = 0
for i in binary_hashes:
    used_counter += i.count('1')

print used_counter
