from itertools import product, count, cycle, repeat
A = list(map(int, "1 2".split()))
B = list(map(int, "3 4".split()))

# for a in A:
#     for b in B:
#        print((int(a), int(b)), end=" ")

##############################################

# for i in product(A, B):
#     print(i, end=" ")

##############################################

print(*product(A, B))

##############################################
