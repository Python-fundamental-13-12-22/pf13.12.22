"""2. Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити
чи введені дані відповідають коректному запису дати."""
y = int(input("Enter year: "))
m = int(input("Enter month: "))
d = int(input("Enter day: "))

if y > 0 and 0 < d < 31 and 0 < m <= 12:
    if(y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
        if m == 2 and d <= 29:
            print(f" This date is correct: {d}.{m}.{y}")
        else:
            print(f"date is not correct")
    elif m == 2 and d <= 28:
        print(f" This date is correct: {d}.{m}.{y}")
    elif (m == 4 or m == 6 or m == 9 or m == 11) and d <= 30:
        print(f" This date is correct: {d}.{m}.{y}")
    elif (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d <= 31:
        print(f" This date is correct: {d}.{m}.{y}")
    else:
        print(f" This date is not correct: {d}.{m}.{y}")
else:
    print(f" This date is not correct: {d}.{m}.{y}")
