def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        year_leap = True
    elif year % 400 == 0:
        year_leap = True
    else:
        year_leap = False
    return year_leap
year = int(input('Введіть рік '))
print(is_year_leap(year))
