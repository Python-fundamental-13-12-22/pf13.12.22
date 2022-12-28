y = int(input('Please, input year\n'))
if (y % 4 == 0  and y % 100 != 0) or y % 400 == 0:
    print("It's a leap year!")
else:
    print('This is not a leap year!')
