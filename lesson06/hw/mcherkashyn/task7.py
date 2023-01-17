def date(day, month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_day_value = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day_value = 30
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        max_day_value = 29
    else:
        max_day_value = 28

    if month < 1 or month > 12:
        print("Дата не вірна")
    elif day < 1 or day > max_day_value:
        print("Дата не вірна")
    else:
        print(f"Дата вірна: {day}.{month}.{year}")

date(32, 1, 2000)
