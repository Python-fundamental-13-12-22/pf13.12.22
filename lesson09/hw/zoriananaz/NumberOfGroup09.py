class ToSmallNumberGroupError(Exception):
    pass


def check_number_group(number):
    try:
        if int(number) > 10:
            print(f"Number of your group input parameter  {number} is valid")
        elif int(number) <= 10:
            raise ToSmallNumberGroupError
    except ToSmallNumberGroupError:
        print(f"We obtain error: Number of your group can't be less than 10")
    except ValueError:
        print(f"You entered incorrect data. Please try again.")


check_number_group(4)
check_number_group(59)
check_number_group("25")
check_number_group("abc")
check_number_group("4")
