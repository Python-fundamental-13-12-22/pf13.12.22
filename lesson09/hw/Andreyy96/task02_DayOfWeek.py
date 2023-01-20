def day_of_week(number):
    try:
        day_week = [1, 2, 3, 4, 5, 6, 7]
        number = int(number)
        if day_week[number - 1]:
            if number == 1:
                print('Понедельник')
            elif number == 2:
                print('Вторник')
            elif number == 3:
                print('Среда')
            elif number == 4:
                print('Четверг')
            elif number == 5:
                print('Пятница')
            elif number == 6:
                print('Субота')
            elif number == 7:
                print('Воскресение')
    except IndexError as err:
        print("There is no such number of the week! Please try again.", err)
    except ValueError as err:
        print('You did not enter a number! Please try again.', err)


day_of_week(2)          # output:  "Tuesday"
day_of_week(11)         # output:  "There is no such number of the week! Please try again."
day_of_week("Monday")   # output:  "You did not enter a number! Please try again."
