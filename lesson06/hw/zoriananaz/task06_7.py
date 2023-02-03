""" Написати функцію `date`, яка приймає 3 аргументи - день, місяць і рік. Повернути True,
якщо така дата є в нашому календарі, і `False` - в іншому випадку."""


def date(d, m, y):
    result = ' '
    if y > 0 and 0 < d < 31 and 0 < m <= 12:
        if m == 2 and d <= 29:
            if d <= 29:
                if(y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
                    result = True
                elif d <= 28:
                    result = True
                else:
                    result = False
        elif (m == 4 or m == 6 or m == 9 or m == 11) and d <= 30:
            result = True
        elif (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d <= 31:
            result = True
        else:
            result = False
    else:
        result = False
    return result


print(date(2, 2, 2000))
print(date(29, 2, 2000))
print(date(31, 4, 2000))
print(date(30, 2, 2000))
print(date(29, 2, 1900))
print(date(29, 2, 1990))
print(date(30, 4, 2000))
print(date(31, 2, 2000))
