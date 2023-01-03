# def my_func():
#     print("test")
#     print("my func")
#     print("test")
#
#
# #
# my_func()
# my_func()
# my_func()
# my_func()
# r = my_func()
# print(r)


# def my_add(a, b):
#     c = a + b
#     return c
#
#
# print(my_add(5, 8))
#
# d = my_add(9, 9)
# print(d)
#
# f = my_add
# print(my_add)
# print(f)
# print(f(5, 9))
# m = max([1, 2, 3, 4])
# print(m)
#
# save_max = max
#
# def max(a, b, c):
#     result = None
#     if a > b and a > c:
#         result = a
#     elif b > a and b > c:
#         result = b
#     else:
#         result = c
#     return result
# print(max(1,4,2))
# print(max(9,4,2))
# max = save_max
# m = max([1, 2, 3, 4])
# print(m)

# def my_func():
#     """
#     my func
#     :return:
#     """
#
#
# my_func()
# help(my_func)
# print(my_func.__doc__)
#
#
# def max(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# def my_add(a, b):
#     return a + b
# my_add(1)

# def print_info(name, age):
#     print(f"my name is {name}, age: {age}")
#
# print_info("Liubomyr", 36)
# print_info(36, "Liubomyr")
# print_info(age=36, name="Liubomyr")


# def print_info(name, age=15):
#     print(f"my name is {name}, age: {age}")
#
# print_info("Liubomyr", 36)
# print_info("Liubomyr")
#
# def my_sum(a, b, c=3, d="dd"):
#     pass

# def my_sum(a, b, c=3, d): # error
#     pass
# def my_test(l=[]):
#
#     l.append(1)
#     print(l)
# my_test([1,2,3])
# my_test([3,2,3])
# my_test([7,9])
# my_test()
# my_test()
# my_test()
# my_test([7,9])
# my_test()

# def my_f(a, b):
#     a.append(b)
#     b = b**2
#     print(a, b)
#
# l = [1,2,3]
# c = 20
# my_f(l, c)
# print(l, c)

# def f(a, b, *args, c=3, d=4, **kwargs):
#     print(f"{a=} {b=} {args=} {c=} {d=} {kwargs=}")
#
#
# f(1, 2)
# f(1, 2, 33)
# f(1, 2, 33, 44)
# f(1, 2, 33, 44, 55, c=333, ff=44, xy=999)
#
#
# def f(a, b, c=3, d=4, *args, **kwargs):
#     print(f"{a=} {b=} {args=} {c=} {d=} {kwargs=}")
# f(1, 2, 33, 44, 55, c=333, ff=44, xy=999)
#
# def f(a, b, *args, c=3, d=4, **kwargs):
#     print(f"{a=} {b=} {args=} {c=} {d=} {kwargs=}")
#
#
# l = [1, 2, 3, 4, 5, 6, 7]
# f(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
# f(*l)
# d = {
#     "a": 55,
#     "b": 99,
#     "c": 33,
#     "d": 444,
#     "ff":88
# }
# f(**d)
# f(*d)
# f(l[3:])

# g = 55
#
# def f():
#     global g
#     print(dir())
#     print(g)
#     g = 99
#     print(g)
#     print(dir())
#
# f()
# print(g)

# def f():
#     a = 0
#     def g(k):
#         nonlocal a
#         print(k**2)
#         a +=1
#         print(a)
#     return g
# my_f = f()
#
# my_f(55)
# my_f(55)
# my_f(55)


# fibo
# 1 1 2 3 5 8 13 21 ...
# def fibo1(n):
#     f = [1, 1]
#     if n < 2:
#         return f[n]
#     for i in range(2, n):
#         f.append(f[i - 1] + f[i - 2])
#     return f[n - 1]
#
#
# print(fibo1(5))
# print(fibo1(6))
#
#
# def fibo2(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo2(n - 1) + fibo2(n - 2)
#
# print(fibo1(5))
# print(fibo1(6))

#
# my_lambda = lambda a, b: a + b
# print(my_lambda(1, 2))
# print(my_lambda(11, 2))

l = [1, 2, "77", 99, "35", 45, 66]

print(sorted(l, key=lambda x: x if type(x) is int else int(x)))
