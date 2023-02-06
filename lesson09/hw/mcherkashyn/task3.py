def check_odd_even(number):
    try:
        number = int(number)
        number = (number % 2)
        if number == 0:
            print("Entered number is even")
        elif number != 0:
            print("Entered number is odd")
    except ValueError:
        print("You entered not a number.")

check_odd_even("fgg")
