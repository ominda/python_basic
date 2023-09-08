# This program created to understand the generators
# How we can create a generetor object and how to use it

def get_odd_numbers(upper_limit):
    """Create a generator object"""
    for number in range(upper_limit):
        if number % 2 == 1:
            print(f"Odd {number}")
            yield number

        
print("Starting")
generator = get_odd_numbers(10)
print(generator)
print("Finish")

for num in generator:
    print(f"In loop {num}")