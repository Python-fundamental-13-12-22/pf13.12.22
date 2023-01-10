# import math
# # def greatest_common_denominator(a, b, c):
# a = 15
# b = 20
# c = 25
# greatest_common_denominator = math.gcd
# print(greatest_common_denominator(a, b, c))
def gcd1(a, b, c):
    def gcd2(a, b):
      while b:
        a, b = b, a % b
      return a
    d = gcd2(gcd2(a, b), c)
    return d


print(gcd1(6, 12, 18))
