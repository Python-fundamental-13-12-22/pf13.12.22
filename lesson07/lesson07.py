# class A:
#     pass
#
#
# a = A()
# print(type(a))
# print(dir(a))
#
#
# class A(object):
#     """hdvsjdsvb"""
#     pass
#
#
# print(A.__doc__)
# a = A()
# print(type(a))
# print(dir(a))
#
# print(a.__doc__)
#
#
# class MyClass(object):
#     """hdvsjdsvb"""
#     def print_1(self):
#         print("1", self)
#
# m = MyClass()
# m.print_1()
# MyClass.print_1(m)
# def print_2(s=None):
#     print("2", s)
# print_2()
# MyClass.print_3 = print_2
# m.print_3()
# print(m)
# print(MyClass.__dict__)
# print(m.__dict__)

# class MyClass(object):
#     cm = []
#     ci = 0
#     def __init__(self):
#         self.im = []
#         self.ii = 10
#
# m1 = MyClass()
# m2 = MyClass()
# print(m1.cm, m1.ci, m1.im, m1.ii)
# print(m2.cm, m2.ci, m2.im, m2.ii)
# m1.im.append(99)
# m2.ii = 88
# m1.cm.append(777)
# m2.ci = 6666
# print(m1.cm, m1.ci, m1.im, m1.ii)
# print(m2.cm, m2.ci, m2.im, m2.ii)
# print(m2.cm, m2.__class__.ci, m2.im, m2.ii)
# print(m1.__dict__)
# print(m2.__dict__)

# class MyClass(object):
#     def __init__(self):
#         self.a = 1
#         self._a = 10
#         self.__a = 19
#     def __print(self):
#         print(self.a, self._a, self.__a)
#
#
# a = MyClass()
# print(a.a)
# print(a._a)
# print(a._MyClass__a)
# a._MyClass__print()

class MyClass:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print("start __new__")
        print(cls)
        # obj = object.__new__(cls)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        cls.__instance.x = "hi"
        print(cls.__instance, id(cls.__instance))
        print("end __new__")

        return cls.__instance
    def __init__(self, a=None):
        print(self, self.__dict__)
        self.a = a
        print(self, self.__dict__)
    def __del__(self):
        print("del")
a1 = MyClass()
a2 = MyClass(2)
del a1
print(a)
