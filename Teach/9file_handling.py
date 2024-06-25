file = open('m.txt', 'r')
# for line in file:
#     print(line, end="")

# print(file.read())

for line in file.readlines():
    print(type(line), line)
    
    # name, subject, marks = line
# # print(file.readline())
# # print(file.readline())

# print(file.readlines())