def reverse_part(index, length, arr):
    part = list(reversed([arr[(index + i) % len(arr)] for i in range(length)]))
    for i in range(length):
        arr[(index + i) % len(arr)] = part[i]

def calculate_hash(lengths, line_hash = range(256), index = 0, skip = 0, depth = 1):
    line_hash = list(line_hash)
    for length in lengths:
        reverse_part(index, length, line_hash)
        index += length + skip
        skip += 1
    if depth > 1:
        return calculate_hash(lengths, line_hash, index, skip, depth - 1)
    return line_hash

def solve_task_1(line):
    line_hash = calculate_hash([int(x) for x in line.split(',')])
    print(line_hash[0] * line_hash[1])

def solve_task_2(line):
    line_hash = calculate_hash([ord(ch) for ch in line] + [17, 31, 73, 47, 23], depth = 64)
    dense_hash = [reduce(lambda x, y: x ^ y, line_hash[i:i + 16]) for i in range(0, len(line_hash), 16)]
    print(''.join(["{0:02x}".format(i) for i in dense_hash]))

if __name__ == '__main__':
    with open('in.txt') as f:
        line = f.readline()
    solve_task_1(line)
    solve_task_2(line)   
