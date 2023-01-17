# TASK 7

def date(day, month, year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 2 and 1<= day <= 29:
            return True
        else:
            return False
    elif 1<= year <= 2500:
        if month == 2 and 1<= day <= 28:
            return True
        elif 1<= day <= 30 and (month == 4 or month == 6 or month == 9 or month == 11):
            return True
        elif 1<=day<=31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            return True
        else:
            return False

print(date(2,1,-1))