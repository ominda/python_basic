# Get user input to perform arithmatic opperations
# Numbers: 10, 20
# Perator: +, -, /, *

"""
Ex: 
Incert two number: 10 20
Incert the Operator: +, -, /, *
"""


num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))
operator = input("Enter the operator: ")

result = 0
 
if operator == '+':
    result = num_1 + num_2
elif operator == '-':
    result = num_1 - num_2
elif operator == '/':
    result = num_1/num_2
elif operator == '*':
    result = num_1 * num_2
else:
    print ("Invalid input!")

print(result)