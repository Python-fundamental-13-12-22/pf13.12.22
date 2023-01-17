# TASK 1

def arithmetic (arg_1, arg_2, arg_3):
    if arg_3 == '+':
        return arg_1 + arg_2
    elif arg_3 == '-':
        return arg_1 - arg_2
    elif arg_3 == '*':
        return arg_1 * arg_2
    elif arg_3 == '/':
        return arg_1 / arg_2
    else:
        return 'Невідома операція'

# TASK 2

def is_year_leap (year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

# TASK 3

def square(a):
    return (a*4,a*a,2**0.5*a)

# TASK 4

def season(month):
    if 1<= month <= 2 or month == 12:
        return 'winter'
    elif 3<= month <= 5:
        return 'spring'
    elif 6<= month <= 8:
        return 'summer'
    elif 9<= month <= 11:
        return 'autumn'
    else:
        return 'no results'

# TASK 5

RATE = 0.1
def bank(n, years):
    total = n * (1 + RATE) ** years
    print(f'{total:.2f}')
    return f'{total:.2f}'

# TASK 6

def is_prime(number):
    if number == 1 or number == 2 or number == 3:
        return True
    elif number % 2 != 0 and number % 3 != 0 and number % 1 == 0 and number % number == 0:
        print (number, 'просте число ')
        return True
    else:
        print(number, 'складне число')
        return False

# TASK 7

def date(day, month, year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 2 and 1<= day <= 29:
            return True
        else:
            return False
    elif 1<= year <= 2500:
        if month == 2 and 1<= day <= 28:
            return True
        elif 1<= day <= 30 and (month == 4 or month == 6 or month == 9 or month == 11):
            return True
        elif 1<=day<=31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            return True
        else:
            return False

# TASK 8

def number_of_uc_lc(string):
    uc = 0
    lc = 0
    for c in string:
        if c.isupper():
            uc += 1
        elif c.islower():
            lc += 1
    print(uc, lc)
    return {"uc": uc, "lc": lc}

# TASK 9

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# TASK 10

def max_values(matrix):
    max_val = float("-inf")
    max_index = (0,0)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_index = (i, j)
    return (max_index[0], max_index[1], max_val)

# TASK 11

def greatest_common_denominator(a, b, c):
    def gcd(x,y):
        while y:
            x, y = y, x % y
        return x
    return gcd(gcd(a, b), c)


