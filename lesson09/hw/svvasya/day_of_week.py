def day_of_week(day_number):
    try:
        if day_number > 1 and day_number < 7:
            if day_number == 1:
                result = 'Monday'
            elif day_number == 2:
                result = 'Tuesday'
            elif day_number == 3:
                result = 'Wednesday'
            elif day_number == 4:
                result = 'Thursday'
            elif day_number == 5:
                result = 'Friday'
            elif day_number == 6:
                result = 'Saturday'
            elif day_number == 7:
                result = 'Sunday'
        else:
            result = 'There is no such day of the week! Please try again.'
    except:
        result = 'You did not enter a number! Please try again.'
    return result

print(day_of_week (5))
print(day_of_week (9))
print(day_of_week ('rere'))
print(day_of_week (2))





