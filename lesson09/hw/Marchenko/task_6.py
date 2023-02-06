class ToSmallNumberGroupError(Exception):
    pass


def check_number_group(number):
    try:
        if int(number) > 10:
            print(f"Number of your group {number} is valid")
        else:
            raise ToSmallNumberGroupError
    except ValueError:
        print("You entered incorrect data. Please try again.")
    except ToSmallNumberGroupError:
        print("We obtain error: Number of your group can't be less than 10")


check_number_group(4) #output: "We obtain error: Number of your group can't be less than 10 "
check_number_group(59) #output: "Number of your group 59 is valid"
check_number_group("25") #output: "Number of your group 25 is valid"
check_number_group("abc") #output: "You entered incorrect data. Please try again."
