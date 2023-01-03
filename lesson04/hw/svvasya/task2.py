# ###2
year = int(input('Введіть рік   '))
month = int(input('Введіть місяць   '))
day = int(input('Введіть день   '))
if year in range(1,2200) and month in range(1,13) and  day in range(1,32): # В умові чітко не вказано діапазон років взяв 1,2199
    print('date is ok')
else:
    print('date is wrong')
