import math
def square(x):
    perimetr=x*4
    area=x**2
    diagonal=x*math.sqrt(2)
    return perimetr,area,diagonal
perimetr,area,diagonal=square(17)
print(f"The perimetr: {perimetr}")
print(f"The area: {area}")
print(f"Diagonal: {diagonal}")