year = int(input('Введите год: '))
month = int(input('Введите месяц: '))
day = int(input('Введите день: '))

if year <= 0:
    print("Некорректный ввод данных: год")
elif month <= 0 or month > 12:
    print("Некорректный ввод данных: месяц")
elif day <= 0 or day > 31:
    print("Некорректный ввод данных: день")
elif month == 2 and day > 28:
    print("Некорректный ввод данных: день")
elif (month == 4, 6, 9, 11) and day > 30:
    print("Некорректный ввод данных: день")
else:
    print(f'Введено корректные данные: {year}.{month}.{day}')
