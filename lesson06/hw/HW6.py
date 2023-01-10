#1
def arifmetic(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid!"


a = int(input("a: "))
b = int(input("b: "))
operation = input("Select a opeation(+;-;*;/): ")
print(f"Result: {arifmetic(a, b, operation)}")

#2
year=int(input("Enter a year: "))
if year%4==0:
    print("It is a leap year")
else:
    print("It is not a leap yar ")


# 3
    import math


    def square(x):
        perimetr = x * 4
        area = x ** 2
        diagonal = x * math.sqrt(2)
        return perimetr, area, diagonal


    perimetr, area, diagonal = square(17)
    print(f"The perimetr: {perimetr}")
    print(f"The area: {area}")
    print(f"Diagonal: {diagonal}")


#4
def season():
    month=int(input("Enter a month: "))
    if month==12 or month==1 or month==2:
        print("winter")
    elif month==3 or month==4 or month==5:
        print("spring")
    elif month==6 or month==7 or month==8:
        print("summer")
    elif month==9 or month==10 or month==11:
        print("autumn")
    else:
        print("Invalid month!")
months=season()
print(months)


#5
def bank():
    n=int(input("Enter the sum of deposit(UA): "))
    years=int(input("Enter a period: "))
    for a in range(years):
     sum=n+n*0.1
    return sum
print(f"Received amount of money(UA): {bank()} ")


#6
def is_prime():
    x=int(input("Enter a number: "))
    if x<2:
        return False
    if x==2:
        return True
    for digit in range(2,x-1):
        if x%digit==0:
            return False
    return True
print(is_prime())


#7
import datetime
def is_valid_date():
    day=int(input("enter a day: "))
    month = int(input("enter a month: "))
    year = int(input("enter a year: "))
    try:
        datetime.datetime(year,month,day)
        return True
    except ValueError:
        return False
print(is_valid_date())


#8
def number_of_uc_lc(string):
    uc=0
    lc=0
    for symbol in string:
        if symbol.isupper():
            uc+=1
        elif symbol.islower():
            lc+=1
    return {"uc":uc,"lc":lc}
string=input("Enter a text: ")
print(number_of_uc_lc(string))


#9
import math
n=int(input("Enter a number to find factorial: "))
f=math.factorial(n)
print(f)


#11
import math
a=int(input("a:"))
b=int(input("b: "))
nsd= math.gcd(a, b)
print(nsd)

