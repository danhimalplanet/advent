#!/usr/bin/env python3

nums = []

for x in range(0, 256):
    nums.append(x)

print(len(nums))
#nums = [ 0, 1, 2, 3, 4]

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

#nums=[4, 3, 0, 1, 2]
#
#length=5
#start=1
#print("nums:", nums)
#print("start:", start)
#print("length:", length)
#print("reversed at start with length:", reverse_segment(nums, start, length))

#inputs = [3, 4, 1, 5]
inputs = [230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167]

x = 0

start = True
while x < len(inputs):
    if start == True:
        print("Beginning:", nums)
        start = False
        current_pos = x
        skip_size = 0
        print("-----------")
    length = inputs[x]
    print("length:", length)
    print("current_pos:", current_pos)
    nums = reverse_segment(nums, current_pos, length)
    print(nums)
    print("skip_size:", skip_size)

    current_pos = current_pos + length + skip_size
    if current_pos > len(nums):
        current_pos = abs(len(nums) - current_pos)

    skip_size = skip_size + 1
    x = x + 1

    num1 = nums[0]
    num2 = nums[1]
    print("result:", num1 * num2)
    print("skip_size next round will be:", skip_size)
    print("current position next round will be:", current_pos)
    print("-----")
