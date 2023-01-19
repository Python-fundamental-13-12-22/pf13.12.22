def greatest_common_denominator(a, b, c):
    divisor = min(a, b, c)
    while divisor > 0:
        if a % divisor == 0 and b % divisor == 0 and c % divisor == 0:
            return divisor
        divisor -= 1

print(greatest_common_denominator(8, 2, 12))
