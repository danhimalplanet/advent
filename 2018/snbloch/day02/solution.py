import io
from collections import Counter

inventory = set()

def contains_two(input_value):
    c = Counter(input_value)
    for i in c:
        if c[i] == 2:
            return True
    return False

def contains_three(input_value):
    c = Counter(input_value)
    for i in c:
        if c[i] == 3:
            return True
    return False

def is_off_by_one(first, second):
    iterator = 0
    different = []
    while iterator < len(first):
        if first[iterator] != second[iterator]:
            different.append(iterator)
        if len(different) > 1:
            return False
        iterator += 1
    if len(different) == 0:
        return False
    return different[0]

def part1():
    global inventory
    twos_count = 0
    threes_count = 0
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            if contains_two(line) == True:
                twos_count += 1
                inventory.add(line.strip())
            if contains_three(line) == True:
                threes_count += 1
                inventory.add(line.strip())
    checksum = twos_count * threes_count
    print 'Part 1, checksum is ' + str(checksum)

def part2():
    for i in inventory:
        for j in inventory:
            result = is_off_by_one(i, j)
            if result != False:
                print 'Part 2, string is ' + i[0:result] + i[result + 1:]
                return

if __name__ == '__main__':
    part1()
    part2()
