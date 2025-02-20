import datetime
wagt = datetime.datetime.today()

print(wagt.strftime("%A"))
print(wagt.strftime("%a"))
print(wagt.strftime("%B"))
print(wagt.strftime("%b"))



import datetime
wagt = datetime.datetime.today()

print(wagt.strftime("Hepdanin %u - nji guni"))
print(wagt.strftime("Yylyn %j - nji guni"))
print(wagt.strftime("Yylyn %V - nji hepdesi"))




import datetime
print("Enter a future date: ")
y = int(input("Year: "))
m = int(input("Month: "))
d = int(input("Day: "))

T = datetime.datetime.today()
F = datetime.datetime(y, m, d)
R = F - T
print(R.days, "days left")
