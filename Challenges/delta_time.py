#!/bin/python3
import datetime

# t1 = "Sat 02 May 2015 19:54:36 +0530"
# t2 = "Fri 01 May 2015 13:54:36 -0000"

# # get the time difference between the two timestamps
# td = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z") - datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

# # print the time difference in seconds
# print(int(abs(td.total_seconds())))

###############################
#!/bin/python3

# Complete the time_delta function below.
def time_delta(t1, t2):
    td = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z") - datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return int(abs(td.total_seconds()))

#########################################
# from datetime import datetime as dt

# def time_delta(t1, t2):
#     dt1, dt2 = [dt.strptime(x, '%a %d %b %Y %H:%M:%S %z') for x in [t1, t2]]
#     return str(abs(int((dt1 - dt2).total_seconds())))
##########################################

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
