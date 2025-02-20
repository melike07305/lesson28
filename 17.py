with open("Polozitel.txt", "w") as fayl:
    for i in C:
        fayl.write(str(i)+"\t")

with open("Otrisatel.txt", "w") as fayl:
    for i in D:
        fayl.write(str(i)+"\t")



import datetime

def yazgy_gos():
    yazgy = input("To Do List? \n")
    senesi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ToDoList.txt", 'a') as fayl:
        fayl.write(f"{senesi} - {yazgy}\n")
    print("Yazgy gosuldy")

def yazgylary_gorkez():
    with open("ToDoList.txt", 'r') as fayl:
        setirler = fayl.readlines()

    if not setirler:
        print("Gunlik yazgy yok!")
    else:
        print("Gulik yazgylary: ")
        for setir in setirler:
            print(setir)

print("Gunlik Ulgamy")
while True:
    bolum = input("\nTaze yazgy goshmak (1)  yada Gunlik yazgylary gormek (2), Cykmak (3): ")
    if bolum == "1":
        yazgy_gos()
    elif bolum == "2":
        yazgylary_gorkez()
    elif bolum == "3":
        print("Programmany ulananynyz ucin sag bolun!")
        break
