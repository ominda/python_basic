my_range = range(20)
my_range_list = list(my_range)

# y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# y = ['a', 'b', 'c', 'd', 'e']
# print(y[-1])
# x = []
# for i in range(5):
#     x.append(my_range_list[i])

# #### Slicing ####
# # Count to 5
# count_to_5 = my_range_list[0:5]
# print(count_to_5)

# last_5 = my_range_list[-5:]
# print(last_5)

# mid_5 = my_range_list[8:13]
# print(mid_5)

# def multi(i):
#     return i*2

# #### Condition slising ####
odd_numbers = [i*2 for i in my_range_list if i % 2 != 0]
print(odd_numbers)

