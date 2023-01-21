def day_of_week():
    try:
        day = int(input("Enter a day: "))
        if day < 1 or day > 7:
            return "  There is no such day of the week! Please try again."
        days_of_week=["  Monday ", "  Tuesday ", "  Wednesday ", "  Thursday ", "  Friday ", "  Saturday ", "  Sunday "]
        return days_of_week[day-1]
    except ValueError:
        return "  You did not enter a number! Please try again."
print(day_of_week())
