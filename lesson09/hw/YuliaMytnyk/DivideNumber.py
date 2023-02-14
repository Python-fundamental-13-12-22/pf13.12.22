def divide():
    while True:
        try:
            number1=int(input("Enter numerator: "))
            number2=int(input("Enter denominator: "))
            if number1==0 or number2==0:
                return  "Oops, numerator / denominator, division by zero is error!!!"
            else:
                sum=number1/number2
                return  f"Result is {sum}"
        except ValueError:
            return "Value Error! You did not enter a number!"
print(divide())
