class MyError(Exception):
    pass


def check_positive(number):
    try:
        if int(number) >= 0:
            print(f"You input positive number: {int(number)}")
        else:
            raise MyError
    except ValueError:
        print("Error type: ValueError!")
    except MyError:
        print(f"You input negative number: {int(number)}. Try again.")


check_positive(24)  #output: "You input positive number: 24"
check_positive(-19)  #output: "You input negative number: -19. Try again."
check_positive("38")  #output: "You input positive number: 38"
check_positive("abc") #output: "Error type: ValueError!"
