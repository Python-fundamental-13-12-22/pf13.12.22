def date(day, month, year):
    if year in range(1, 2200) and month in range(1, 13) and day in range(1,32):
        return True
    else:
        return False
year = int(input('Введіть рік   '))
month = int(input('Введіть місяць   '))
day = int(input('Введіть день   '))
print(date(day, month, year))
