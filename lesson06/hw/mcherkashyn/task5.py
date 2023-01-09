def bank(n, years):
    calc = n * (1+10/100)**years
    result = calc - n
    return int(result)

print(bank(30000,3))
