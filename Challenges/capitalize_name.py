#!/bin/python3

# capitalize every word in a string

s = "ominda rathnasiri 23is 3 on 4the floor"

def solve(s):
    return " ".join(list(i.capitalize() for i in s.split(' ')))


print(solve(s))


#######################3

# def solve(s):s
#     return s.title()
# print(solve(s))