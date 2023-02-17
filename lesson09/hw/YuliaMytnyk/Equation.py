import math
def solve_quadric_equation():
    try:
        a=int(input("Enter the first digit : "))
        b=int(input("Enter the second digit : "))
        c=int(input("Enter the third digit : "))
        D=b**2-4*a*c
        if D>0:
            return f"   The solution are x1={(-b+math.sqrt(D))/(2*a)} and x2={(-b-math.sqrt(D))/(2*a)}"
        elif D==0:
            return f"   The solution is x={(-b/2*a)}"
        elif a==0 or b==0 or c==0:
            raise ZeroDivisionError
        else:
            raise ValueError
    except ZeroDivisionError:
        return  "   Zero Division Error"
    except ValueError:
        return  "   Could not convert string to float"
print(solve_quadric_equation())

