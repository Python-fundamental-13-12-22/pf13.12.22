def is_year_leap(year):
    result = False
    if year % 4 == 0:
        print("It's a leap year!")
        result = True
    else:
        result = False
        print('This is not a leap year!')
    return result

year = int(input('Введите год: '))
print(is_year_leap(year))
