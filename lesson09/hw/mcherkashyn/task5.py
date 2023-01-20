class ToSmallNumberGroupError(Exception):
    pass

def check_number_group(number):
    try:
        if int(number) > 10:
            print(f"Number of your group {number} is valid")
        else:
            raise ToSmallNumberGroupError
    except ToSmallNumberGroupError:
        print("We obtain error: Number of your group can't be less than 10")
    except ValueError:
        print("You entered incorrect data. Please try again.")

check_number_group("dgd")
