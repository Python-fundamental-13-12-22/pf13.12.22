class MyError(ArithmeticError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    pass
def check_positive(number):
    if int(number) >= 0:
        print(f"You input positive number: {number}")
    elif int(number) < 0:
        raise MyError(f"You input negative number: {number}. Try again.")
try:
    #check_positive(24)  # output:    "You input positive number: 24"

    check_positive(-19)  # output:     "You input negative number: -19. Try again."

    #check_positive("38")  # output:    "You input positive number: 38"

    #check_positive("abc")  # output:     "Error type: ValueError!"
except MyError as err:
    print(err)
except ValueError as err:
    print(f"Error type: {err} ")

