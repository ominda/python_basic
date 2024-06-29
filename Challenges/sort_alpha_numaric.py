# S = "Sorting1234"
# lower_list = [l for l in S if l.islower()]
# lower_list.sort()
# upper_list = [l for l in S if l.isupper()]
# upper_list.sort()
# odd_list = [l for l in S if l.isdigit() and int(l)%2 != 0]
# odd_list.sort()
# even_list = [l for l in S if l.isdigit() and int(l)%2 == 0]
# even_list.sort()
# print(lower_list)
# print(upper_list)
# print(odd_list) 
# print(even_list)

# print("".join(lower_list + upper_list + odd_list + even_list))

######################################

# S = input()
# lower_list = []
# upper_list = []
# odd_list = []
# even_list = []

# for i in range(len(S)):
#     if S[i].islower():
#         lower_list.append(S[i])
#     if S[i].isupper():
#         upper_list.append(S[i])
#     if S[i].isdigit() and int(S[i])%2 != 0:
#         odd_list.append(S[i])
#     if S[i].isdigit() and int(S[i])%2 == 0:
#         even_list.append(S[i])
# lower_list.sort()
# upper_list.sort()
# odd_list.sort()
# even_list.sort()    
# print("".join(lower_list + upper_list + odd_list + even_list))

#############################################

# S = "Sorting1234"
S = "SorTingA1234"
print("".join(sorted(list(S),key= lambda x : (-x.islower() ,-x.isupper(), int(x) % 2 == 0 if x.isdigit() else None,x))))
# print(sorted(list(S)))

# lambda x : (-x.islower() ,-x.isupper(), int(x) % 2 == 0 if x.isdigit() else None,x)

# print(list(map(lambda x : x.islower(), list(S))))

# print(sorted(list(S),key= lambda x : (-x.islower(), -x.isupper(), int(x) % 2 == 0 if x.isdigit() else None, x)))