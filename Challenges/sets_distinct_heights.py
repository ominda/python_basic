######## Distinct avarage ############
N = 10
L = "161 182 161 154 176 170 167 171 170 174".split()
S = set(map(int, L))
avg = sum(S) / len(S)
# print(avg)


########################

n = 4
N = set(map(int,"2 4 5 9".split()))
m = 4
M = set(map(int, "2 4 11 12".split()))
Nn = N.difference(M)
Mm = M.difference(N)
# print(type(sorted(list(Nn.union(Mm)))), sorted(list(Nn.union(Mm))))
print(i for i in list(Nn.union(Mm)))
# for i in sorted(list(Nn.union(Mm))):
#     print(i)

########################

# _, a, _, b = input(), set(input().split()), input(), set(input().split())
# print(*sorted(map(int, a ^ b)), sep='\n')
