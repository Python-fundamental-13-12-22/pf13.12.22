def day_of_week(number_of_day):
    list1 = ["Понеділок", "Вівторок", "Середа", "П'ятниця", "Субота", "Неділя"]
    try:
        number_of_day = int(number_of_day)
        print(list1[number_of_day-1])
    except IndexError:
        print("There is no such day of the week! Please try again.")
    except ValueError:
        print("You did not enter a number! Please try again.")


day_of_week(2) # output: "Tuesday"
day_of_week(11) # output: "There is no such day of the week! Please try again."
day_of_week("Monday") # output: "You did not enter a number! Please try again.
