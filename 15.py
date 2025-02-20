import datetime
sagat = int(input("Enter the number of hours? "))
T = datetime.datetime.today()
H = datetime.timedelta(hours = sagat)
R = T - H
print("Date before", sagat, "hours", R.strftime("%d.%m.%Y %X"))



with open("Resul.txt", "w") as fayl:
    fayl.write("Resul Nuryyev 17 yash")



with open("Resul.txt", "r") as fayl:
    print(fayl.read())




A = ["Inlis dili", "Kompyuter", "Matematika"]
with open("Kurslar.txt", "w") as fayl:
    for i in A:
        fayl.write(f"{i}\n")


with open("Kurslar.txt", "r") as fayl:
    print(fayl.read())
