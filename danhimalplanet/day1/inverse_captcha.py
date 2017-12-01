#!/usr/bin/env python

import sys

def inverse_captcha(number):
    sum = 0
    if number[0] == number[-1]:
        sum = sum + int(number[0])
    for i in range(1, len(number)):
        if number[i] == number[i - 1]:
            sum = sum + int(number[i])
    return sum

if len(sys.argv) - 1 == 1:
    number=sys.argv[1]
    print("sum: {}".format(inverse_captcha(number)))
else:
    number="1234"
    print("Using example data '1234'")
    print("sum: {}".format(inverse_captcha(number)))
