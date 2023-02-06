def day_of_week(day):
    try:
        day = int(day)
        list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(list[day-1])
    except IndexError:
        print("There is no such day of the week! Please try again.")
    except ValueError:
        print("You did not enter a number! Please try again.")

day_of_week(78)
