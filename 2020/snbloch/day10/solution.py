from itertools import combinations
from collections import defaultdict

values = []
values.append(0)
with open('input.txt', 'r') as inputfile:
    for line in inputfile:
        values.append(int(line.strip()))
values.append(max(values) + 3)

def part1():
    diff_count = defaultdict(int)
    sorted_values = sorted(values)
    for i in range(1, len(sorted_values)):
        if sorted_values[i] - sorted_values[i - 1] == 1:
            diff_count['ones'] += 1
        elif sorted_values[i] - sorted_values[i - 1] == 2:
            diff_count['twos'] += 1
        elif sorted_values[i] - sorted_values[i - 1] == 3:
            diff_count['threes'] += 1
    print(diff_count['ones'] * diff_count['threes'])

def tribonacci(length):
    tribonacci_list = [0,0,1]
    for i in range(length):
        tribonacci_list.append(tribonacci_list[i + 2] + tribonacci_list[i + 1] + tribonacci_list[i])
    return tribonacci_list[-1]
    
def part2():
    sorted_values = sorted(values)
    total = 1
    series_length = 0
    for i in range(1, len(sorted_values)):
        if sorted_values[i] - sorted_values[i - 1] == 1:
            series_length += 1
        elif sorted_values[i] - sorted_values[i - 1] == 3:
            total *= tribonacci(series_length)
            series_length = 0
    print(total)

if __name__ == '__main__':
    part1()
    part2()