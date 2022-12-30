a = int(input('input a\n'))
b = int(input('input b\n'))
c = int(input('input c\n'))
p = (a + b + c)/2
if (a + b > c or a + c > b or c + b > a) and (p != a, p != b, p != c):
    s = (p * (p - a) * (p - b) * (p - c))**(1/2)
    print(f"Площа = {s}, периметр = {p*2}")
else:
    pritn("Трикутник неможливо побудувати")
