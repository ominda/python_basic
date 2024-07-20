#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_count = 0
    max_count = 0
    min_score = scores[0]
    max_score = scores[0]

    for score in scores:
        if score < min_score:
            min_count += 1
            min_score = score
        if score > max_score:
            max_count += 1
            max_score = score
    return max_count, min_count  

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    n = int("10".strip())

    # scores = list(map(int, input().rstrip().split()))
    score_list = "3 4 21 36 10 28 35 5 24 42"
    scores = list(map(int, score_list.rstrip().split()))

    result = breakingRecords(scores)

    print(" ".join(map(str, result)))

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
