def solve_quadric_equation(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = b**2 - 4*a*c
        x1 = ((0 - b) - d ** (1 / 2)) / (2 * a)
        x2 = ((0 - b) + d ** (1 / 2)) / (2 * a)
        print(f"The solution are {x1=} and {x2=}")
    except ZeroDivisionError:
        print("Zero Division Error")
    except ValueError:
        print("Could not convert string to float")


solve_quadric_equation(1, 5, 6)    #output: " The solution are x1=(-2-0j) and x2=(-3+0j)"
solve_quadric_equation(0, 8, 1)  #output: "Zero Division Error"
solve_quadric_equation(1, "abc", 5) #output: "Could not convert string to float"
