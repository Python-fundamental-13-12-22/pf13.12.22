"""1. Ввести значення(рік), вивести повідомлення `It's a leap year!` якщо рік
високосний і `This is not a leap year!` якщо ні."""

year = int(input("Enter year: "))

if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"This is a leap year: {year}")
else:
    print(f"This is not a leap year: {year}")
