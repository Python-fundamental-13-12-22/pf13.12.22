def is_year_leap(year):
    remainder = year % 4
    if remainder == 0:
        result = "True"
    elif remainder != 0:
        result = "False"
    return result

print(is_year_leap(2000))
