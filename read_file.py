with open('m.txt', 'r') as file:
    for line in file:
        # print(line.strip().split(','))
        l = tuple(line.strip().split(','))
        print(type(l))
        p = [ (name) for name in l ]
        print(p)
        # Ominda = [subject for name, subject in line.strip().split(',') if name == 'Ominda']
        # for i in line.strip().split(','):
        #     print(type(i), i)

# print(Ominda)

