#task1
year=int(input("Enter a year: "))
if year%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
#task2
import datetime
year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
day=int(input("Enter a day: "))
date=datetime.date(year,month,day)
if date ==datetime.datetime.now().date():
    print("Correct;)")
else:
    print("Incorrect:(")
#task 3
import math
def solve_equation(a,b,c):
    D=b**2-4*a*c
    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print(f'two roots:x1={x1},x2={x2}')
    elif D==0:
        x=b/2*a
        print(f"one root:x={x}")
    else:
        print("zero roots")
solve_equation(5,-8,3)
#task4
import math
def triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        perimetr=a+b+c
        s=perimetr/2
        area=math.sqrt((s*(s-a)*(s-b)*(s-c)))
        print(f"Perimetr: {perimetr}")
        print(f"Area: {area}")
    else:
        print("Mistake,try another digit")
triangle(3,4,5)
#task5
days_of_week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
k=int(input("Whrite a number of week(1-365): "))
n=days_of_week[(k-1)%7]
print(f"Number of week: {k}")
print(f"Day of week: {n}")
#task6
import random
random_digit=random.randint(0,100)
attempts=0
while True:
    guess=int(input("Enter a digit: "))
    attempts +=1
    if guess == random_digit:
        print(f"Congratulations,you got it: {random_digit}")
        break
    elif guess<random_digit:
        print("More")
    else:
        print("Less")
    if attempts>10:
        print(f"Sorry,try again ;) guessed number: {random_digit}")
        break
#task7
count=0
for i in range(10):
    digit=int(input("Enter a natural digit,greater than 2 :"))
    if digit <=0:
        print("Invalid input,try greater one!")
    if digit%5==0:
        count+=1
print(f"There are {count} digits,multiple of 5")
#task8
for a in range(1,10):
    for n in range(1,10):
        print(f"{a} x {n} = {a*n}",end="\t")
    print()
#task9
N=int(input("Enter a width : "))
M=int(input("Enter a height : "))
for n in range(N):
    for m in range(M):
        if n==0 or n==N-1 or m==0 or m==M-1:
            print("*",end="\t")
        else:
            print("+",end="\t")
    print()
#task11
positive_digit=0
negative_digit=0
while True:
    digit = int(input("Enter a digit: "))
    if digit>0:
        positive_digit+=1
    elif digit<0:
        negative_digit+=1
    elif digit==0:
        break
total_sum=positive_digit+negative_digit
print(f"Positive digit: {(positive_digit/total_sum)*100}%")
print(f"Negative digitL: {(negative_digit/total_sum)*100}%")








