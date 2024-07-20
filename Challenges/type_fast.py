import time
import matplotlib.pyplot as plt

print("Type 'Dictionary' word 5 times as faster as you can.")
number_of_tries = 5
time_list = []
x = ["1", "2", "3", "4", "5"]
# seconds = 3
# while seconds > 0:
#     print(seconds)
#     time.sleep(1)
#     seconds -= 1
word_type = "Dictionary"
mistakes = []
input("Press Enter to continue")
while number_of_tries > 0:
    start_time = time.time() 
    word = input()
    end_time = time.time()
    if word_type != word:
        mistakes.append(word)
    time_list.append(end_time - start_time)
    number_of_tries -= 1
print(time_list)
print(mistakes)

plt.plot(x, time_list)
plt.xlabel("Number of tries")
plt.ylabel("Time taken")
plt.title("Type Improvement graph")
plt.show()
