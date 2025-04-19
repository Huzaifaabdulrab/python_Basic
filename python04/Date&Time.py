# import time

# ticks = time.time()
# print(ticks)

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# import calendar

# print(calendar.month(2025 ,1))

# from datetime import date

# date1 = date(2023 , 2, 12)
# print(date1)

import datetime

# x= datetime.datetime.now()
# print(x)

y = datetime.datetime(2021 , 1 , 1)
print(y.strftime("%f"))
print(y.strftime("%a"))
print(y.strftime("%b"))
print(y.strftime("%Y"))