#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = []
    for i in grades:
        if i < 38:
            result.append(i)
        elif i % 5 > 2:
            result.append(i + 5 - (i % 5))
        else:
            result.append(i)
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # grades_count = int(input().strip())
    grades_count = 4

    grades = [73, 67, 38, 33]

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    output = gradingStudents(grades)
    print('\n'.join(map(str, output)))

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
