#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    ###################################################
    # initial_number = starting_number = 3
    # timer = 1
    # map_timer_stage = {}
    # while initial_number > 0:
    #     map_timer_stage[timer] = initial_number
    #     timer += 1
    #     initial_number -= 1
    #     if initial_number > 25:
    #         break
    #     if initial_number == 0:
    #         initial_number = starting_number * 2
    #         starting_number = initial_number
    #         continue
    #     # print(map_timer_stage)
    # return map_timer_stage[t]
    ####################################################
    
    time, value = 1, 3
    while time + value <= t:
        time, value = time + value, value * 2
    return value - (t - time)
    ####################################################

    # temp = math.ceil(math.log2((t/3)+1))
    # return int(3*(2**temp) - 2 - t)
    ####################################################

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())
    time = "21"
    t = int(time.strip())

    result = strangeCounter(t)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
