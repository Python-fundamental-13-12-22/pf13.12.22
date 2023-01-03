# ###1
year = int(input('Введіть рік   '))
if year%4 == 0 and year%100 != 0:
    print('''It's a leap year''' )
elif year % 400 == 0:
    print('''It's a leap year''')
else:
    print('''It's not a leap year''')
