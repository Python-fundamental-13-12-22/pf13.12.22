# TASK 5

RATE = 0.1
def bank(n, years):
    total = n * (1 + RATE) ** years
    print(f'{total:.2f}')
    return f'{total:.2f}'

