def day_of_week(number):
    try:
        week = [1, 2, 3, 4, 5, 6, 7]
        number = int(number)
        if range(len(week)):
            if number == 1:
                print(f"Sunday")
            elif number == 2:
                print(f"Monday")
            elif number == 3:
                print(f"Tuesday")
            elif number == 4:
                print(f"Wednesday")
            elif number == 5:
                print(f"Thursday")
            elif number == 6:
                print(f"Friday")
            elif number == 7:
                print(f"Saturday")
            elif number > 7:
                raise IndexError
    except IndexError:
        print(f"There is no such day of the week! Please,try again")
    except ValueError:
        print(f"You did not enter a number! Please try again.")


day_of_week(2)
day_of_week(8)
day_of_week("df")
