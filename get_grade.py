# Get the grade of each student.
# Create a function with '*args' and '**kwargs' as applicable
# Return the grade.

# 0 < 35 -> W
# 35 < 55 -> S
# 55 < 65 -> C
# 65 < 75 -> B
# 75 <= 100 -> A


def get_grade(marks):
    """Function take marks as an integer and
    work with grade and return the grade correspond to the given marks.    
    """
    if marks < 0 or marks > 100:
        return
    elif marks < 35:
        grade = "W"
    elif marks < 55:
        grade = "S"
    elif marks < 65:
        grade = "C"
    elif marks < 75:
        grade = "B"
    else:
        grade = "A"
    return grade


result = get_grade(100)
if not result:
    print("Invalid marks")
else:
    print(f'You got "{result}"')