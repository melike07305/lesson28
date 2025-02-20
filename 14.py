import datetime
print("Enter date in the past: ")
y = int(input("Year: "))
m = int(input("Month: "))
d = int(input("Day: "))

T = datetime.datetime.today()
P = datetime.datetime(y, m, d)
R = T - P
print(R.days, "days have passed")


import datetime
gun = int(input("Enter the number of days? "))
T = datetime.datetime.today()
D = datetime.timedelta(days = gun)
R = T + D
print("Date after", gun, "days", R.strftime("%d.%m.%Y"))



import datetime
gun = int(input("Enter the number of days? "))
T = datetime.datetime.today()
D = datetime.timedelta(days = gun)
R = T - D
print("Date before", gun, "days", R.strftime("%d.%m.%Y"))




import datetime
sagat = int(input("Enter the number of hours? "))
T = datetime.datetime.today()
H = datetime.timedelta(hours = sagat)
R = T + H
print("Date after", sagat, "hours", R.strftime("%d.%m.%Y %X"))
