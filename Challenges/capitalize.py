#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the solve function below.
# def solve(s):
#     # name = s.split(" ")
#     # for word in name:
#     #     cap = word.ca
#     # print(type(name))
#     # return s.capitalize()
#     name = ["hello," "world"]
#     return 

# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     result = solve(s)
#     # fptr.write(result + '\n')
#     # fptr.close()


def capitalize(string):
    return ' '.join(w.capitalize() for w in string.split(' '))

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
    
# s = ["hello" "world"]
# for w in s:
#     name = w.capitalize()
# print(name)