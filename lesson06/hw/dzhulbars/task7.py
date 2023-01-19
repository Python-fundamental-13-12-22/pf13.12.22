import datetime
def date():
    today=datetime.datetime.now().date()
    year=int(input("Enter a year: "))
    month=int(input("Enter a month: "))
    day=int(input("Enter a day: "))
    date=datetime.date(year,month,day)
    if date==datetime.datetime.now().date():
        return f"Correct: {today}"
    else:
        return f"Incorrect...Correct date is: {today}"
print(date())
