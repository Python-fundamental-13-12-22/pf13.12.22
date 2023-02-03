def divide(numerator, denominator):
    try:
        result = numerator / denominator
        if denominator != 0:
            print(f"Result is {result}")
    except ZeroDivisionError:
        print(f"Oops, {numerator} / {denominator} denominator, division by zero is error!!!")
    except TypeError:
        print(f"Value Error! You did not enter a number!")
    except ValueError:
        print(f"Value Error! You did not enter a number!")


divide(8, 16)
divide(5, 0)
divide("25", 5)
divide("abc", 9)
