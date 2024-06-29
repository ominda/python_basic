# if __name__ == "__main__":
#     N = int(input())
#     L = list(map(int,(input().split())))
#     # N = 4
#     # L = list(map(int, '12 9 8 1234'.split()))
#     # palindrome_list = [True for x in L if str(x) == str(x)[::-1]]
#     palindrome_list = [True if str(x) == str(x)[::-1] else False for x in L]
#     print(palindrome_list)
#     C = list(map(lambda x: x > 0, L))
#     print(C)
#     print(all(C + palindrome_list))

#################################

N = int(input())
L = input().split()
print((all(int(L[i]) > 0 for i in range(N))) and any(L[i] == L[i][::-1] for i in range(N)))