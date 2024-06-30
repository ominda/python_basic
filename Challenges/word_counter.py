N = 5
S = """bcdef
abcdefg
bcde
bcdef
bcdef"""

# ['bcdef', 'abcdefg', 'bcde', 'bcdef', 'bcdef' ]

# L = set(S.split('\n'))
# print(len(L), L)
L = S.split('\n')
word_count = []
count = 1
j = 0

print(L)

# for j in range(N):  # j -> 0, 1, 2, 3, 4
#     count = 1
#     for i in range(1+j, N-1): # i -> 1, 2, 3, 4
#         if L[j] == L[i]:
#             count += 1
#             L.pop(i)
#     word_count.append(count)

# print(word_count)

###################################################
# N = 5 , N-1 -> 4

for i in range(N-1):
    for j in range(i+1, N-(i+1)):
        if L[i] == L[j]:
            count += 1
print(L[i], count)
