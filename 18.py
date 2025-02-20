import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Bir san chakla (1-100 aralygynda) "))
            attempts += 1
            if guess < secret_number:
                print("Kabir uly san chakla!")
            elif guess > secret_number:
                print("Kabir kichi san chakla!")
            else:
                print(f"Dogry! {attempts} synanyshykda chakladynyz")
                break
        except ValueError:
            print("Yalnysh san girizdiniz!")
guess_the_number()



import calendar

def display_calendar():
    try:
        year = int(input("Yyly girizin: "))
        month = int(input("Ayy girizin: "))
        if 1 <= month <= 12:
            print(calendar.month(year, month))
        else:
            print("Yalnysh ay giriziniz!")
    except ValueError:
        print("Yalnysh san girizdiniz")
display_calendar()



import datetime

def birthday_day():
    try:
        birthday = input("Doglan gununizi girizin (YYYY-MM-DD): ")
        birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        print(f"Doglan gununiz: {birthday_date.strftime('%A')}")
    except ValueError:
        print("Yalnysh format! YYYY-MM-DD formatynda girizin")
birthday_day()

