# if __name__ == '__main__':
#     N = int(input())
#     C = [input().split() for _ in range(N)]
#     L = []
    
#     for i in range(N):
#         if C[i][0] == 'print':
#             print(L)
#             continue
            
#         list_command = getattr(L, C[i][0])
#         list_command(*map(int, C[i][1:]))

###########################
# def myfunc(n):
#     return n*n

# x = map(myfunc, range(5))
# print(set(x))
###########################

# l = ['sat', 'bat', 'cat', 'mat']
# test = list(map(list, l))
# print(test)
###########################

# l1 = [3, 2, 1]
# l2 = [6, 5, 4]
# result =  list(map(lambda n1, n2: n1*n2, l1, l2))
# print(result)

############################

if __name__ == '__main__':
    N = int(input())
    C = [input().split() for _ in range(N)]
    L = []
    
    for i in range(N):
        if C[i][0] == 'print':
            print(L)
            continue
            
        list_command = getattr(L, C[i][0])
        print(list_command)
        print(C[i][1:])
        list_command(map(int, C[i][1:]))