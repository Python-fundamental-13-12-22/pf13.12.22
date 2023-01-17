# TASK 11

def greatest_common_denominator(a, b, c):
    def gcd(x,y):
        while y:
            x, y = y, x % y
        return x
    return gcd(gcd(a, b), c)