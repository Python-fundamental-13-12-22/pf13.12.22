"""2. Написати функцію `is_year_leap`, приймає 1 аргумент - рік, і повертає True,
якщо рік високосний, і `False` в іншому випадку."""


def is_year_leap(year):
    if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        result = True
    else:
        result = False
    return result


print(is_year_leap(1900))
print(is_year_leap(2000))
print(is_year_leap(2023))
