class MyError(Exception):
    pass


def check_odd_even(number):
    try:
        if int(number) % 2 == 0:
            print("Entered number is even")
        else:
            raise MyError
    except ValueError:
        print("You entered not a number.")
    except MyError:
        print("Entered number is odd")


number = input("input number\n")
check_odd_even(number)
