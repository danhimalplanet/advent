#!/usr/bin/env python3

input="0  2  7  0"
#input="11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"
banks = [ int(input) for input in input.split() ]

def most(banks):
    index = 0
    i = 0
    for i in range(0, len(banks)):
        if banks[i] > banks[index]:
            index = i
    return index

def reallocate(banks):
    most_index = most(banks)
    wealth = banks[most_index]
    banks[most_index] = 0

    index = most_index + 1
    while wealth > 0:
        if index == len(banks):
            index = 0
        banks[index] = banks[index] + 1
        index = index + 1
        wealth = wealth - 1
    return banks

record = {}

# 'occurence': = int
# 'cycle': = int
#  'cycle' = int

cycles = 0

i = 0
while i < 10000000:
    b = reallocate(banks)
    #print("we reallocated and ended up with", b)

    if tuple(b) in record:
        cycles = cycles + 1
        print("we found the reallocated banks in the dict already")
        break
    else:
        cycles = cycles + 1
        print("added to the record", b)
        record[tuple(b)] = 1
        print("number of cycles we've done is", cycles)
    banks = b
    i  = i + 1 

print(record)
print(cycles)
