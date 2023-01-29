def solve_quadric_equation(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = b**2 - (4 * a * c)
        x1 = -(b - (d ** 0.5)) / (2 * a)
        x2 = -(b + (d ** 0.5)) / (2 * a)
        print(f"The solution are {x1} and {x2}")
    except ZeroDivisionError:
        print(f"Zero Division Error")
    except ValueError:
        print(f"Could not convert string to float")


solve_quadric_equation(1, 5, 6)
solve_quadric_equation(0, 8, 1)
solve_quadric_equation(1, "abc", 5)
