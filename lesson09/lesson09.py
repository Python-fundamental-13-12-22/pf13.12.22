from loging_config import logging
# a = int(input("a:"))
# b = int(input("b:"))
# c = a / b
#
# a = input("a:")
# if a.isdigit():
#     a = int(a)
# else:
#     print("a is not number")
# try:
#     a = int(input("a:"))
# except:
#     print("a is not number")
#
# def read_int(msg):
#     while True:
#         a = input(msg)
#         if a.isdigit():
#             a = int(a)
#             return a
#         else:
#             print("a is not number")

def read_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError as err:
            logging.warning(f"read_int {type(err)}")
            print(type(err), err)


a = read_int("a:")
# b = read_int("b:")
# try:
#     c = a / b
# except:
#     print("error")

# print("end")
# a = 1
# b = "sad"
# try:
#     5.0**99999
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError as err:
#     print("ArithmeticError", type(err))
# except OverflowError as err:
#     print("OverflowError", type(err))


# a = input("a:")
# b = input("b:")
# try:
#     a = int(a)
#     b = int(b)
#     c = a / b
# except (ZeroDivisionError, ValueError) as err:
#     print(type(err), "error")
# except Exception as err:
#     print(type(err), err)
# else:
#     print(f"{c=}")
# finally:
#     print("end")
#
# def f(a,b):
#     try:
#         a = int(a)
#         b = int(b)
#         c = a / b
#         return c
#     except (ZeroDivisionError, ValueError) as err:
#         print(type(err), "error")
#     except Exception as err:
#         print(type(err), err)
#     else:
#         print(f"{c=}")
#     finally:
#         print("end")
#         return 5
# g = f(5, 3)
# print(g)


# def f(a,b):
#     if type(a) is not int or type(b) is not int:
#         raise ArithmeticError
#     if b == 0:
#         raise ZeroDivisionError("b is 0")
#
#     return a / b
#
# try:
#     print(f(5, 0))
# except ZeroDivisionError as err:
#     print(err)
# except ArithmeticError:
#     print("a or b is not number")
#
# try:
#     print(f("5", 0))
# except ZeroDivisionError as err:
#     print(err)
# except ArithmeticError:
#     print("a or b is not number")

# f("5", 0)

class MyError(ArithmeticError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.info("create MyError")
    pass


def f(a,b):
    if type(a) is not int or type(b) is not int:
        raise MyError("message")
    if b == 0:
        raise ZeroDivisionError("b is 0")

    return a / b
try:
    print(f("5", 0))
except ZeroDivisionError as err:
    print(err)
except MyError as err:
    print(err)
except ArithmeticError:
    print("a or b is not number")



