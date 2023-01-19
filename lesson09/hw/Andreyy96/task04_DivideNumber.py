def divide(numerator, denominator):
    try:
        divide_number = int(numerator) / int(denominator)
        print(f'Result is {divide_number}')
    except ZeroDivisionError as err:
        print(f'Oops, {numerator}/{denominator}, division by zero is error!!!. {err}')
    except ValueError as err:
        print(f'Value Error! You did not enter a number! {err}')


divide(8, 16)     # output: 'Result is 0.5'
divide(5, 0)      # output: 'Oops, 5 / 0 denominator, division by zero is error!!!'
divide("25", 5)   # output: 'Value Error! You did not enter a number!'
divide("abc", 9)  # output: 'Value Error! You did not enter a number!'
