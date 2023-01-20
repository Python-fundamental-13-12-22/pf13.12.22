# l = [i ** 2 for i in range(10)]
# print(l)
# l = {i ** 2 for i in range(10)}
# print(l)
# l = {i: i ** 2 for i in range(10)}
# print(l)
#
# l = (i ** 2 for i in range(10))
# print(l)
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# for i in l:
#     print(i)
# def f(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
# g = f(4)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# def my_decorator(f):
#     print(f)
#     return f
#
# # my_decorator("my")
#
# @my_decorator
# def m():
#     print("m")
#
#
# m()
#
# @my_decorator
# def m2():
#     print("m2")
#
# @my_decorator
# def m3():
#     print("m3")
# m2()
#
# m3()
#
#
# def time_run(func):
#     print("func", func)
#     def wraper():
#         start_time = datetime.now()
#         result = func()
#         end_time = datetime.now()
#         print(f"{func.__name__} run {end_time - start_time}s")
#         return result
#     print("w", wraper)
#     return func
#
#
# @time_run
# def f1():
#     time.sleep(random.randint(0,2))
#     return random.random()
# print("f1", f1)
# for i in range(3):
#     a = f1()
#     print(a)

# from datetime import datetime
#
#
# def time_run(func, text=""):
#     print(f"{text=}")
#     print("func", func)
#     def wraper(*args, **kwargs):
#         print(f"{args=} {kwargs=}")
#         start_time = datetime.now()
#         result = func(*args, **kwargs)
#         end_time = datetime.now()
#         print(f"{func.__name__} run {end_time - start_time}s")
#         return result
#     print("w", wraper)
#     return wraper
#
#
# @time_run
# def f1(sleep=0, return_value=0):
#     time.sleep(random.randint(0,2))
#     return random.random()
# print("f1", f1)
# for i in range(2):
#     a = f1()
#     print(a)
#
# f1(2, return_value=99)
#
# @time_run
# def f2(sleep=0, return_value=0):
#     time.sleep(random.randint(0,2))
#     return random.random()

# def decorator_fectory(argument):
#     print("run decorator_fectory")
#     print(f"{argument=}")
#     def decorator(func):
#         print("run decorator")
#         print(f"{func=}")
#         def wraper(*args, **kwargs):
#             print("run wraper")
#             print(f"{wraper=}")
#             print("end wraper")
#             return func(*args, **kwargs)
#
#         print("end decorator")
#         return wraper
#     print("end decorator_fectory")
#     return decorator
#
# @decorator_fectory("test")
# def my_f():
#     pass
# my_f()

# def retrieve(attempts=3):
#     print("run decorator_fectory")
#     print(f"{attempts=}")
#     def decorator(func):
#         print("run decorator")
#         print(f"{func=}")
#         _attempts = 0
#         def wraper(*args, **kwargs):
#             nonlocal _attempts
#             print("run wraper")
#             print(f"{wraper=}")
#             if _attempts >= attempts:
#                 raise IndexError
#             try:
#                 print("end wraper")
#                 return func(*args, **kwargs)
#             except:
#                 _attempts += 1
#                 return func(*args, **kwargs)
#         print("end decorator")
#         return wraper
#     print("end decorator_fectory")
#     return decorator
#
# @retrieve()
# def my_f():
#     result = random.randint(0, 10)
#     print(result)
#     if result > 5:
#         return result
#     raise Exception
# a = my_f()
# print(a)


# def retrieve(func):
#     atempts = 0
#
#     def decorator(*args, **kwargs):
#         nonlocal atempts
#         print(atempts)
#         atempts += 1
#         result = func(*args, **kwargs)
#         return result
#
#     return decorator
#
#
#
# @retrieve
# def f1():
#     pass

# @retrieve
# def f2():
#     pass
#
#
# @retrieve
# def f3():
#     pass
# f1()
# f2()
# f3()
# f1()
# f2()
# f3()

def retrieve(a=None):
    def decorator(func):
        def wraper(*args, **kwargs):
            print(a)
            result = func(*args, **kwargs)
            return result
        return wraper
    return decorator





@retrieve(1)
@retrieve(2)
@retrieve(3)
@retrieve()
@retrieve(5)
def f1():
    print("f1")
f1()


@retrieve(5)
@retrieve(4)
@retrieve(5)
@retrieve(2)
@retrieve(1)
def f1():
    print("f1")
f1()