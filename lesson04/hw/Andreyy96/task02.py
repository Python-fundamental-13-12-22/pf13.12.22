year = int(input('Введите год: '))
month = int(input('Введите месяц: '))
day = int(input('Введите день: '))

if year <= 0:
    print("Некорректный ввод данных: год")
elif month <= 0 or month > 12:
    print("Некорректный ввод данных: месяц")
elif day <= 0 or day > 31:
    print("Некорректный ввод данных: день")
else:
    print(f'Введено корректные данные: {year}.{month}.{day}')
