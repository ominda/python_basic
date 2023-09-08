# This program expect an integer list.
# Process each item and identify whether it is Odd or Even.
# We expect to generate a dictionary.

number_list = [911, 703, 892, 572, 164, 798, 989, 408]


def is_odd_even(number: int) -> str:
    """This function expect a integer and return with string 
    depend on the number, whether it is "Odd" or "Even"
    """
    return "Odd" if number % 2 != 0 else "Even"


odd_even_dictionary = { number: is_odd_even(number) for number in number_list}

print(odd_even_dictionary)