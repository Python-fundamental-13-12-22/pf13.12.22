# 1. Ввести значення(рік), вивести повідомлення `It's a leap year!` якщо рік високосний і
# `This is not a leap year!` якщо ні.
rik = int(input("Веедіть рік від -2100 до 2100:\n"))
if rik in range(-2100, 2100, 4):
    print("It's a leap year!")
else:
    print("This is not a leap year!")
