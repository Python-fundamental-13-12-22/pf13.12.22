#task1
import re

def valid_email(email):
    try:
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
        match = re.match(pattern, email)
        if match:
            return "Email is valid"
        else:
            raise ValueError
    except:
        return "Email is invalid"


print(valid_email("trafik@ukr.tel.com"))
print(valid_email("trafik@ukr_tel.com"))
print(valid_email("tra@fik@ukr.com"))
print(valid_email("ownsite@our.c0m"))
#task2
def days_of_week():
    try:
        day = int(input("Enter a day 1-7: "))
        if day in range(1,8):
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            return days[day-1]
        else:
            return "There is no such a day in the week.Try again"
    except ValueError:
        return "Enter a digit instead of word"


print(days_of_week())
#task3
def check_odd_even():
    try:
        digit = int(input("Enter a digit: "))
        if digit % 2:
            return "Odd"
        else:
            return "Even"
    except ValueError:
        return "Write a digit instead of word"


print(check_odd_even())
#task4
def divide():
    while True:
        try:
            a = int(input("Enter a first digit: "))
            b = int(input("Enter a second digit: "))
            if a == 0 or b == 0:
                return "Oops, numerator / denominator, division by zero is error!!!"
            else:
                sum = a/b
                return f"The answer is: {sum}."
        except ValueError:
            return "Enter a digit instead of word."


print(divide())
#task5
class ToSmallNumberGroupError(Exception):
    pass


def check_number_group():
    try:
        digit = int(input("Enter a digit: "))
        if digit >= 10:
            return "Number of your group input parameter of function is valid."
        else:
            raise ToSmallNumberGroupError
    except ToSmallNumberGroupError:
        return "We obtain error: Number of your group can't be less than 10."
    except ValueError:
        return "Enter a digit instead of word."


print(check_number_group())
#task6
class MyError(Exception):
    pass


def check_positive():
    try:
        digit = int(input("Enter a digit: "))
        if digit >= 0:
            return f"You input positive number: {digit}."
        elif digit <= 0:
            raise MyError
    except MyError:
        return f"You input negative number: {digit}."
    except ValueError:
        return "Enter a digit instead of word."


print(check_positive())
#task7
import math


def solve_quadric_equation():
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        D = b**2-4*a*c
        if D > 0:
            return f"The solution is x1={(-b+math.sqrt(D))/(2*a)} and x2={(-b-math.sqrt(D))/(2*a)}"
        elif D == 0:
            return f"The solution is x={(-b/2*a)}"
        elif a == 0 or b == 0 or c == 0:
            raise ZeroDivisionError
        else:
            raise ValueError
    except ZeroDivisionError:
        return "Zero Division Error"
    except ValueError:
        return "Could not convert string to float"


print(solve_quadric_equation())