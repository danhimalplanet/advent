#!/usr/bin/env python

# rotate a list structure

import sys
from collections import deque

def inverse_captcha(number):
    nums=deque(number)
    rotated=deque(number)
    rotated.rotate(int(len(number)/2))
    sum = 0
    length=len(number)
    for index in range(0, len(number)):
        if nums[index] == rotated[index]:
            sum += int(nums[index])
    return sum

if len(sys.argv) - 1 == 1:
    number=sys.argv[1]
    print("sum: {}".format(inverse_captcha(number)))
else:
    number="1212"
    print("Using example data {}".format(number))
    print("sum: {}".format(inverse_captcha(number)))
