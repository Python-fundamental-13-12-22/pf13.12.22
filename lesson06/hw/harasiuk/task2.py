def leap_year(a):
    a = True
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("It's a leap year!")
        a = True
    else:
        print('This is not a leap year!')
        a = False
    print(f"{a}")
    return a


y = int(input('Please, input year\n'))
leap_year(y)
