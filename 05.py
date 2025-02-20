def ocurmek():
    time = int(input("Nace minutdan: "))
    os.system(f"shutdown/s/t {time}")
    print(f"Kompyuter {time} minutdan son ocer!")

def restart():
    time = int(input("Nace minutdan: "))
    os.system(f"shutdown/r/t {time}")
    print(f"Kompyuter {time} minutdan son restart bolar!")
    
def buyrugy_yzyna_almak():
    os.system("shutdown/a")
    print("Buyruk yzyna alyndy!")
