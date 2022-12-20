# a = 1
#
# print(id(a))
# a = 2
# print(id(a))
# l = [1, 5.5]
# print(id(l))
# l.append(2)
# print(id(l))
#
#
# s = "test"
# print(s)
# # s[2] = "s" # TypeError: 'str' object does not support item assignment

# a = 1
# print(type(a))
# a = "2"
# print(type(a))
# print(isinstance(a, str))
# class A:
#     pass
# class B(A):
#     pass
# b = B()
# print(type(b))
# print(isinstance(b, B))
# print(isinstance(b, A))
# print(type(b) is A)
# print(type(b) is B)
# l =[12, 55]
# a = str(l)
# print(a)
# print(int("55"))
# # print(int("55a")) # ValueError: invalid literal for int() with base 10: '55a'
# print(int("55a", 16))
# print(int("01010", 2))
# print(int("55a", 36))
# # print(int("55a", 38)) # ValueError: int() base must be >= 2 and <= 36, or 0

# a = 9**9999
# print(len(str(a)))
# print(a)
# import sys
# sys.setrecursionlimit(1300)
# def f(a):
#     print(a)
#     return f(a+1)
# f(1)
#
# a = (-1)**0.5
# print(a, type(a))

# a=10;
# s = "print(a)"
# # b = 25;
# # c = a+b
# eval(s)
# print(a)

# def привіт():
#     print("hi")
# for i in range(255):
#     print(i, chr(i), ord(chr(i)))
# привіт()
# a = 128
# print(bin(a))
# print(oct(a))
# print(a)
# print(hex(a))

# a = ".vfdbgjkfdgjk"
# print(a)
# a = 'level 00' \
#     'level 01'
# print(a)
# a = 'level 00\n' \
#     'level 01'
# print(a)
# a = """level 00
# level 01
# level 02
# level 03"""
#
# print(a)
#
# pattern = "name %s , age %d"
# s = pattern % ("L", 36)
# print(s)
#
# pattern = "name {name} , age {age}, {name}"
# s = pattern.format(name="L", age=36)
# print(s)
#
# name = "L"
# age = 36
# s = f"name {name} , age {age}, {name}"
# print(s)

# s = "0123456789abc"
# print(len(s))
# print(s[12])
# print(s[1:5]) #[1, 5)
# print(s[1:-5])
# print(s[:])
# print(s[4:])
# print(s[:6])
# print(s[::-1])
# print(s[0:11:3])
# print(s[0::3])
# # print(s[15]) #IndexError: string index out of range
# # print(s[-15]) #IndexError: string index out of range


# for method in dir(str):
#     if not method.startswith("__"):
#         print(method)
#
# print([method for method in dir(str) if not method.startswith("__")])
# s = "iM PrOgRaMeR. iM lIuBoMyR"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.center(100))
# print(s.split())
# print("*".join(s.split()))
# print(s.split("i"))
# print("*".join(s.split("i")))
# print(s.count("i"))
# print(s.find("i"))
# print(s.find("i", 2))
# print(s.find("iss", 15))
# print(s.index("i"))
#
# s = "     iM PrOgRaMeR. iM lIuBoMyR  "
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
#
# print(len(s))
# print(s.zfill(35))
# print(s.index("iss")) #ValueError: substring not found

# print(1 +2.56)
# print(7/3)
# print(7//3)
# print(7%3)


import math
print(math.pow(2, 10))
print(math.sqrt(2))

print(2**10)
print(2**(1/3))

a = 2**(1/3)

print(math.trunc(a))
print(math.floor(a))






















# # import this
# zen = """The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""

a =2
b = 4
