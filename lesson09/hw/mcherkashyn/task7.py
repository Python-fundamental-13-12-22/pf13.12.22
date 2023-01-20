import math

def solve_quadric_equation(a, b, c):

    try:
        d = (int(b) ** 2) - (4 * int(a) * int(c))
        x1 = ((-b - (math.sqrt(d))) / (2 * a))
        x2 = ((-b + (math.sqrt(d))) / (2 * a))
        print(f"The solution are x1={x1} and x2={x2}")
    except ZeroDivisionError:
        print("Zero Division Error")
    except ValueError:
        print("Could not convert string to float")

solve_quadric_equation(1, "abc", 5)
