
"""3. Для довільних дійсних чисел `a`, `b`, і `c` визначити, чи має рівняння
`ax2+bx+c=0` хоча б один дійсний корінь і якщо так, то видрукувати його."""
a = int(float(input(f"Enter a:")))
b = int(float(input(f"Enter b:")))
c = int(float(input(f"Enter c:")))
d = b * b - 4 * a * c
x_1 = (-b + (d ** (0.5))) / (2 * a)
x_2 = (-b - (d ** (0.5))) / (2 * a)

if d < 0:
    print(f"нема дійсних коренів ")
elif d == 0:
    print(f"два однакових кореня")
    print(f"x1: {x_1:.2f}, x2: {x_2:.2f}")
elif d > 0:
    print("має два різних кореня")
    print(f"x1: {x_1:.2f}, x2: {x_2:.2f}")
