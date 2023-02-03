def check_odd_even(number):
    try:
        number = int(number)
        if number % 2 == 0:
            print(f"Entered number is odd")
        elif number % 2 != 0:
            print(f"Entered number is even")
    except ValueError:
        print(f"You entered not a number.")


check_odd_even(24)
check_odd_even(19)
check_odd_even("aaa")
