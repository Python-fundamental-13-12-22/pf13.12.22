a = int(input('input a\n'))
b = int(input('input b\n'))
c = int(input('input c\n'))
y = (b**2 - 4*a*c)
if y > 0:
    x1 = b*(-1) - (b^2 - 4*a*c)**(1/2)
    x2 = b*(-1) + (b^2 - 4*a*c)**(1/2)
    print(f"x1 = {x1}, x2 = {x2}")
else:
    print("Коренів немає")
