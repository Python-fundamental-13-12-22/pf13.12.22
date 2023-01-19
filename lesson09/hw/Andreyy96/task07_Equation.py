def solve_quadric_equation(a, b, c):
    try:
        discr = (int(b) ** 2) - (4 * int(a) * int(c))
        if discr > 0:
            x1 = (-b + discr ** 0.5) / (2 * a)
            x2 = (-b - discr ** 0.5) / (2 * a)
            print(f'The solution are {x1=} and {x2=}')
        else:
            print('No roots')
    except ZeroDivisionError as err:
        print(f'Zero Division Error. {err}')
    except ValueError as err:
        print(f'Could not convert string to float. {err}')


solve_quadric_equation(1, 5, 6)        # output:  'The solution are x1= and x2='
solve_quadric_equation(0, 8, 1)        # output:  'Zero Division Error'
solve_quadric_equation(1, 'abc', 5)    # output:  'Could not convert string to float'
