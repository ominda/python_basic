# Get the minimum, maximum and average of the given number list.
# Numbers provided with a list.

# Iterate the list with for loop and identify which eliment is the min, max and add all together. 

numbers = [911, 703, 892, 572, 164, 798, 989, 408, 527, 919, 173, 425, 109, 238, 213, 580, 709, 608, 126, 55, 339, 462, 654, 378, 964, 584, 172, 930, 172, 772, 676, 41, 449, 15, 965, 470, 552, 955, 367, 832, 506, 735, 218, 769, 40, 552, 829, 191, 784, 566, 327, 207, 466, 17, 721, 652, 54, 386, 159, 204, 771, 346, 234, 160, 368, 455, 221, 966, 984, 963, 849, 764, 440, 365, 177, 109, 430, 467, 918, 952, 113, 572, 943, 936, 345, 970, 789, 36, 312, 426, 387, 476, 352, 454, 543, 244, 688, 301, 768, 548]

minimum = maximum = numbers[0]
total = 0

for num in numbers:
    if minimum > num:
        minimum = num
    if maximum < num:
        maximum = num
    total += num

average = total/len(numbers)

print(f'{minimum = }, {maximum = } and {average = }')
