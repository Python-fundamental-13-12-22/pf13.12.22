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

