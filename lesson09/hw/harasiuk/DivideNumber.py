def divide(numerator, denominator):
    try:
        c = numerator / denominator
        print(f"Result is{c}")
    except TypeError:
        print("Value Error! You did not enter a number!")
    except ZeroDivisionError:
        print(f"Oops, {numerator} / {denominator}, division by zero is error!!!")


divide(8, 16) #output: "Result is 0.5"
divide(5, 0) #output: "Oops, 5 / 0 denominator, division by zero is error!!!"
divide("25", 5) #output: "Value Error! You did not enter a number!"
divide("abc", 9) #output: "Value Error! You did not enter a number!"
