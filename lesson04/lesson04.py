# a = [] and ""
# print(a)
#
# a = [] and "" or 15
# print(a)
# # False, 0, None, iter if len==0
# a = [] and "" or 15 and [""] # [] or  [""]
# print(a)
#
# a = 10
# if a > 5:
#     print("a > 5")
#     print("test")
#
# if a > 10:
#     print("a > 10")
# print("end")
#
# if a > 10:
#     print("a > 10")
# else:
#     print("a <= 10")
# a = 10
# if a > 10:
#     print("a > 10")
# elif a == 10:
#     print("a ==10")
# elif a < 10:
#     print("a <= 10")
#
# if a > 10:
#     print("a > 10")
# else:
#     if a == 10:
#         print("a ==10")
#     else:
#         if a < 10:
#             print("a <= 10")
# a = 15
# if a > 10:
#     print("a > 10")
# elif a >5 :
#     print("a > 5")
# elif a < 10:
#     print("a <= 10")
#
# if a > 10:
#     print("a > 10")
#
# if a >5 :
#     print("a > 5")
# elif a < 10:
#     print("a <= 10")
#
# a = 10
# value = "is True" if a == 10 else "is False"
# print(value)
# a = 20
# value = "is True" if a == 10 else "is False"
# print(value)
#
# status_code = 400
#
# match status_code:
#     case 200:
#         print("ok")
#     case 300:
#         print("redirect")
#     case 400:
#         print("bead request")
#     case 500:
#         print("server error")
#
# if status_code == 200:
#     print("ok")
# elif status_code == 300:
#     print("redirect")
# elif status_code == 400:
#     print("bead request")
# elif status_code == 500:
#     print("server error")
# status_code = 401
# match status_code:
#     case 200:
#         print("ok")
#     case 300:
#         print("redirect")
#     case 400:
#         print("bead request")
#     case 401 | 403 as error:
#         print(f"{error} is authentication error")
#     case 500:
#         print("server error")
# status_code = 403
# match status_code:
#     case 200:
#         print("ok")
#     case 300:
#         print("redirect")
#     case 400:
#         print("bead request")
#     case 401 | 403 as error:
#         print(f"{error} is authentication error")
#     case 500:
#         print("server error")

# a = 8
# if a > 5 and a < 10:
#     print("a є [5, 10]")
# if 5 < a < 10:
#     print("a є [5, 10]")
# b = 8
# if 5 < a <= b < 10:
#     print("a є [5, 10]")

#
# a = 0
# while a < 10:
#     print(a)
#     a += 1
# else:
#     print(a)
#
# print([i for i in range(10)])
# print([i for i in range(5, 10)])
# print([i for i in range(0, 10, 3)])
#
# for i in range(10):
#     print(i)
#     cc = i
# else:
#     print(i)
#
#
# print(cc)

# for i in range(10):
#     if i == 7:
#         break
#     print(i)
# else:
#     print("else")

for i in range(10):
    print(i, end=" ")
    if i % 2:
        print()
        continue
    print(i**2)
else:
    print("else")

for i in range(10):
    pass
