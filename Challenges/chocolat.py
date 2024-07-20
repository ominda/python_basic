#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    # count = 0
    # for i in range(len(s)-m+1):
    #     sum = 0
    #     for j in range(i,i+m):
    #         sum += s[j]
    #     if sum == d:
    #         count += 1

    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    n = 5

    # s = list(map(int, input().rstrip().split()))
    mylist = "1 2 1 3 2"
    s = list(map(int, mylist.rstrip().split()))

    # first_multiple_input = input().rstrip().split()
    birthday_month = "3 2"
    first_multiple_input = birthday_month.rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
