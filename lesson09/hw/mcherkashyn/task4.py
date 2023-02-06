def divide(numerator, denominator):
    try:
        numerator = int(numerator)
        denominator = int(denominator)
        result = numerator / denominator
        print(f"Result is {result}")
    except ValueError:
        print("Value Error! You did not enter a number!")
    except ZeroDivisionError:
        print("Oops, numerator / denominator, division by zero is error!!!")

divide("hello", 89)
