def square(a):
    p = a*4
    s = a**2
    c = (a**2 + a**2)**(1/2)
    l = (p, s, c)
    return l


a = int(input("input a\n"))
l = square(a)
print(l)
