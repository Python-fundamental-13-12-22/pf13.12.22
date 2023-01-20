def divide(numerator, denominator):
    try:
        result = numerator/denominator
        print(f"Result is {result}")
    except ZeroDivisionError as err:
           print(f"Oops, {numerator} / {denominator} denominator, {err} is error!!!")
    except:
        print('Value Error! You did not enter a number!')
divide(3, 'hghgh')
divide(8, 16)        #output:   "Result is 0.5"
divide (5, 0)        #output:   "Oops, 5 / 0 denominator, division by zero is error!!!"
divide("25", 5)    #output:   "Value Error! You did not enter a number!"
divide("abc", 9)  #output:    "Value Error! You did not enter a number!"
