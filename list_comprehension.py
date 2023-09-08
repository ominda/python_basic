# With this program, we can generate list from a given numbered list.
# The generated list can be any type.
# Much powerfull feature and we able to optimize our code with list comprehension.

number_list = [911, 703, 892, 572, 164, 798, 989, 408]
odd_even_list = []

def is_odd(number: int) -> str:
    """Expect a integer number and check whether it is odd or even
    if odd, function will return "Odd" and else "Even"
    """
    return "Odd" if number % 2 != 0 else "Even"


odd_even_list = [{number: is_odd(number)} for number in number_list]

print(odd_even_list)

