#!/usr/bin/env python3

nums = []

for x in range(0, 256):
    nums.append(x)

def reverse_segment(nums, start, length):
    """
    print("nums:", nums)
    print("length nums:", len(nums))
    print("start:", start)
    print("length:", length)
    """

    if length==1:
        return nums

    if start + length <= len(nums):
        sublist_length=length
        sublist = nums[start:start+sublist_length]

        reversed_sublist=sublist[::-1]

        x = start
        y = 0

        while y < len(reversed_sublist):
            nums[x] = reversed_sublist[y]
            x += 1
            y += 1

    else:
        sublist_part1_length=((len(nums) - start))
        sublist_part1 = nums[start:start+sublist_part1_length]
        #print("sublist_part1", sublist_part1)

        sublist_part2_length=( start + length ) - len(nums)
        #print("sublist_part2_length:", sublist_part2_length)

        sublist_part2 = nums[0:sublist_part2_length]
        #print("sublist_part2:", sublist_part2)

        sublist = sublist_part1 + sublist_part2
        #print("sublist:", sublist)

        reversed_sublist=sublist[::-1]
        x = start
        y = 0
        while x < len(nums):
            nums[x] = reversed_sublist.pop(0)
            x += 1
            y += 1
        #print(reversed_sublist)

        x = 0
        y = 0
        while x < len(reversed_sublist):
            nums[x] = reversed_sublist[y]
            x += 1
            y += 1

    return(nums)

def encode_some_bs(inputs):
    lst = []
    lst = str(inputs)
    lst = lst.strip("[")
    lst = lst.strip("]")
    lst = [ char for char in lst if char != " " ]
    lst = [ ord(char) for char in lst ] + [17, 31, 73, 47, 23]
    return lst

nums = encode_some_bs([1,2,3])
print(nums)
x = 1
start = True
while x <= 64:
    print("round:", x)
    x += 1
