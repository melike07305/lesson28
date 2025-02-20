def main():
    while True:
        choice = input("Saylan: ")
        if choice == '1':
            ocurmek()
        elif choice == '2':
            restart()
        elif choice == '3':
            buyrugy_yzyna_almak()
        elif choice == '4':
            print("Programmany ulalanynyz ucin sagbolun!")
            break
        else:
            print("Yalnys buyruk!")

main()
