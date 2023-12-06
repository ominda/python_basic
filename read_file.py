marks_dict = {}
student_list = []

with open('m.txt', 'r') as file:
    for line in file:
        # print(line.strip().split(','))
        l = tuple(line.strip().split(','))
        # print(type(l), l)
        name, subject, marks = l


        # stu = [(subject, marks) for name, subject, marks in l]
        # print(stu)
       
        # Ominda = [subject for name, subject in line.strip().split(',') if name == 'Ominda']
        # for i in line.strip().split(','):
        #     print(type(i), i)

# print(Ominda)
print(marks_dict.values())

