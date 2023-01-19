def greatest_common_denominator(number1,number2,number3):
    from math import gcd
    from functools import reduce
    return reduce(gcd, [number1,number2,number3])
print(greatest_common_denominator(11,22,121))