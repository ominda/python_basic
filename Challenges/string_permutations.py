from itertools import permutations, combinations

# S = input().split()
S = "HACK 2".split()
O = permutations(S[0], int(S[1]))

# for i in O:
#     print("".join(i))

#####################################

# print("\n".join(sorted(["".join(i) for i in O])))

#####################################

##### Combinations #####
K = "HACK 2".split()
result = []
for i in range(1, int(K[1])+1):
    result.extend(combinations(sorted(K[0]), i))
print("\n".join(["".join(j) for j in result]))
# for j in result:
#     print("".join(j))
# print("\n".join(["".join(j) for j in result]))

