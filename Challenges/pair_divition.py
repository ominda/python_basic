#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    counter = 0
    for i in range(n):
        print("outer loop i : ", ar[i])
        for j in ar[i+1:]:
            print("inner loop (i, j): ", (ar[i], j))
            if (ar[i] + j) % k == 0:
                counter += 1
                print("inside condition (i, j) :", (ar[i],j), counter)
    return counter

# "1 3 2 6 1 2"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()
    n_and_k = "6 5"
    first_multiple_input = n_and_k.rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    num_list = "1 2 3 4 5 6" #"1 3 2 6 1 2"
    ar = list(map(int, num_list.rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
