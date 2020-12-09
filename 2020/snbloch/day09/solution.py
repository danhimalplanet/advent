from itertools import combinations

values = []
with open('input.txt', 'r') as inputfile:
    for line in inputfile:
        values.append(int(line.strip()))
preamble_length = 25
position = 25

def part1():
    global position, preamble_length
    finished = False
    while finished == False:
        combos = list(combinations(values[position - preamble_length:position], 2))
        twosum = [sum(list(i)) for i in combos]
        if values[position] not in twosum:
            print(values[position])
            finished = True
        else:
            position += 1

def part2():
    global position
    checksum = values[position]
    finished = False
    range_size = 2
    while range_size <= position and finished == False:
        start_pos = 0
        end_pos = range_size
        while end_pos <= position:
            if sum(values[start_pos:end_pos]) == checksum:
                print(min(values[start_pos:end_pos]) + max(values[start_pos:end_pos]))
                finished = True
                break
            else:
                start_pos += 1
                end_pos += 1
        range_size += 1

if __name__ == '__main__':
    part1()
    part2()
