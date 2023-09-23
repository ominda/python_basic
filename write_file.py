# Need to create a program to generate a file with below format

# Name, Subject, Marks
# Ominda, Maths, 75

# Create 3 list with Headding, Name, and Subject.
# Generate a file with these 3 list

heading_list = ['Name', 'Subject', 'Marks']
students_name_list = ['Ominda', 'Mihidinu', 'Vajira', 'Rasanga', 'Chinthana']
subject_list = ['Maths', 'Science', 'Engilish', 'Sinhala']
marks_range = 100
delemeter = ', '

with open('data.txt', 'w') as file:
    for item in heading_list:
        file.write(delemeter.join(item))