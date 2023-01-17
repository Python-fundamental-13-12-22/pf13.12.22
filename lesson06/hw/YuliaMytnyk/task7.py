import datetime
def is_valid_date():
    day=int(input("enter a day: "))
    month = int(input("enter a month: "))
    year = int(input("enter a year: "))
    try:
        datetime.datetime(year,month,day)
        return True
    except ValueError:
        return False
print(is_valid_date())
