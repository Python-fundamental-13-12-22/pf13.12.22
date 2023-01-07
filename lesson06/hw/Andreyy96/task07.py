def date(day, month, year):
    key = False
    if year <= 0:
        key = False
    elif month <= 0 or month > 12:
        key = False
    elif day <= 0 or day > 31:
        key = False
    elif month == 2 and day > 28:
        key = False
    elif (month == 4, 6, 9, 11) and day > 30:
        key = False
    else:
        key = True

    return key

year = int(input('Введите год: '))
month = int(input('Введите месяц: '))
day = int(input('Введите день: '))
print(date(day, month, year))
