class MyError(Exception):
    pass


def check_positive(number):
    try:
        if int(number) > 0:
            print(f"You input positive number: {number}")
        else:
            raise MyError
    except MyError:
        print(f"You input negative number: {number}. Try again")
    except ValueError:
        print(f"Error type: ValueError!")


check_positive(24)
check_positive(-19)
check_positive("38")
check_positive("abs")
