#1
year=int(input("Enter a year: "))
if year%4==0:
    print("It's a leap year!")
else:
    print("It's not a leap year!")

#2
import datetime
year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
day=int(input("Enter a day: "))
date=datetime.date(year,month,day)
if date==datetime.datetime.now().date():
    print("Correct!")
else:
     print("Incorrect!")

#3
import math
def solve_equation(a,b,c):
    D=b**2-4*a*c
    if D>0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"x1={x1}, x2={x2}")
    elif D==0:
        x=-b/(2*a)
        print(f"x={x}")
    else:
        print("0")
solve_equation(5,-8,3)

#4
import math
def triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        perimetr=a+b+c
        s=perimetr/2
        area=(math.sqrt(s*(s-a)*(s-b)*(s-c)))
        print(f"Perimetr={perimetr};")
        print(f"Area={area};")
    else:
        print("It's not possible to construct a triangle.")
triangle(3,4,5)

#5
days_of_week=("Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
k=int(input("Enter a day(1-365): "))
n=days_of_week[(k-1)%7]
print(f"{k} day of week is {n}")

#6
import random
random_number=random.randint(0,100)
attempts = 0
while True:
    number=int(input("Enter a number(0-100): "))
    attempts+=1
    if number==random_number:
        print(f"Guessed: {random_number}")
        break
    if number<random_number:
        print("higher")
    else:
        print("lower")
    if attempts>10:
        print(f"Not guessed: {random_number}")
        break

#7
count=0
for i in range(10):
    number=int(input("Enter a number: "))
    if number<=2:
        print("The number is invalid!")
    elif number%5==0:
        count+=1
print(f"There are {count} numbers divisible by 5 ")

#8
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}", end="\t")
    print()

#9
N=int(input("Enter height: "))
M=int(input("Enter width: "))
for n in range(N):
    for m in range(M):
        if n==0 or n==N-1 or m==0 or m==M-1:
            print("*", end="\t")
        else:
            print("+", end="\t")
    print()

#11
positive_count=0
negative_count=0
while True:
    number=int(input("Enter a number: "))
    if number>0:
        positive_count+=1
    elif number<0:
        negative_count+=1
    elif number==0:
        break
total_count=positive_count+negative_count
print(f"Positive count: {(positive_count/total_count)*100}%")
print(f"Negative count: {(negative_count/total_count)*100}%")