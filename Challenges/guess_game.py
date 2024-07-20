# import random
# name_count = 8
# name_list = []
# for _ in range(name_count):
#     name_list.append(input("Enter a name: "))

# print(name_list[random.randint(0, name_count)])

######################################

import random
colour_list = ['Red', 'Yello', 'Green', 'Blue', 'Purple', 'Black', 'Orange']
# length_of_list = len(colour_list)
random_color = colour_list[random.randint(0, len(colour_list)-1)].lower()
print(random_color)
color = input("Guess the color : ")

while True:    
    if random_color == color:
        print("You guess the color correctly !")
        play_again = input("Do you want to play again ? (yes/no)").lower()
        if play_again == "no":
            break
        elif play_again == "yes":
            random_color = colour_list[random.randint(0, len(colour_list)-1)].lower()
            print(random_color)
            continue
        else:
            print("Not a valid input!")
            play_again = input("Do you want to play again ? (yes/no)").lower()
    else:
        color = input("Guess the color : ")