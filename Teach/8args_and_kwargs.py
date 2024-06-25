# args example
def add_numbers(*args) -> float:
    """
    This function will take n number of numaric arguments and return the summary of them.
    """
    answer = 0
    for num in args:
        answer += num
    return answer


# print(add_numbers(1, 2, 3, 4, 5))


# kwargs example
def city_postalcodes(**kwargs):
    """
    This function will take n number of key:value paires and returns the postal codes
    """
    city = []
    code = []
    for city_name, postal_codes in kwargs.items():
        city.append(city_name)
        code.append(postal_codes)
    return city, code


# print(city_postalcodes(Colombo = "000100", Galle = "000520", Ratnapura = "000200", Kandy = "000400"))

# kwargs example 2
def subject_marks(**kwargs):
    """
    This function will capture the subject and corresponding marks for each subjects,
    and return the total of marks.
    """
    subjects_list = []
    marks_list = []
    for subject, marks in kwargs.items():
        # subjects_list.append(subject)
        marks_list.append(marks)
    return sum(marks_list)


msg = "You have total: "
print(msg, subject_marks(Science = 79, Maths = 80, English = 59, Sinhala = 60))
