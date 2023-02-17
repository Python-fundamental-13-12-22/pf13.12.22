class ToSmallNumberGroupError(Exception):
    pass
def check_number_group():
    try:
        number=int(input("enter a number: "))
        if number>10:
            return f"Number of your group {number} of function is valid"
        elif number<=10:
            raise ToSmallNumberGroupError
        else:
            raise ValueError
    except ToSmallNumberGroupError:
        return  "We obtain error: Number of your group can't be less than 10"
    except ValueError:
        return "You entered incorrect data. Please try again."
print(check_number_group())

