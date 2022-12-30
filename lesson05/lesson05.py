### list

# l = list()
# print(type(l), l)
# l = list("asdqwe")
# print(type(l), l)
# l = []
# print(type(l), l)
# l = [1, "jfdh", [[1, 1], 1], 1]
# print(type(l), l)
# print([method for method in dir(list) if not method.startswith("_")])
# l = []
# l.append(1)
# l.append([1, 2, 3])
# print(type(l), l)
# l.extend([1, 2, 3])
# print(type(l), l)
# ll = l
# print(id(l), l)
# print(id(ll), ll)
# l[0] = 10
# ll[4] = 10
# print(id(l), l)
# print(id(ll), ll)
#
# ll = l.copy()
# print(id(l), l)
# print(id(ll), ll)
# l[0] = 10
# ll[4] = 10
# l[1][1] *= 2
# print(id(l), l)
# print(id(ll), ll)
# import copy
#
# ll = copy.deepcopy(l)
# print(id(l), l)
# print(id(ll), ll)
# l[0] = 10
# ll[4] = 10
# l[1][1] *= 2
# print(id(l), l)
# print(id(ll), ll)

# ll = l[:]

# l = [1, 2, 3]
# l.clear()
# l = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
# print(l.count(1))
# print(l.index(5))
# # print(l.index(9))
# l.insert(3, 99)
# print(l)
# print(l.pop())
# print(l)
# print(l.pop(3))
# print(l)
# l.remove(1)
# # l.remove(10)
# print(l)
# l.reverse()
# print(l)
# l.sort()
# print(l)
# l = l+l
# print(l)

# l = [1, 2, "3", (55, 1)]
# print(all(l))
# l.append([])
# print(all(l))
# l = [1,2,3,4]
# for i in l:
#     i = i**2
# print(l)
# for i in range(len(l)):
#     l[i] = l[i]**2
# print(l)
# for i, value in enumerate(l):
#     l[i] = value**2
# print(l)
# ll = list(reversed(l))
# print(l)
# print(ll)

# l = [(i, j, k) for i in range(3) for j in range(3) for k in range(3) if i+j+k % 2]
# print(l)
#
# l = []
#
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i+j+k % 2:
#                 l.append((i, j, k))
# print(l)

### tuple
# print([method for method in dir(tuple) if not method.startswith("_")])
#
# t = tuple()
# t = tuple([1,2,3])
# t = ()
# t = (1, )
# print(type(t))


### set
# s = set()
# s = set("jhsfbjsvbkjsjdlaesbvfiks000")
# print(s)
# s = {1, 2, 3}
# print(type(s))
# s = {}
# print(type(s))
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# print(s1, s2)
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.intersection(s2))
# print(s2.intersection(s1))

### dict
# d = dict()
# d = dict(((1, 2), (2, 2), (3, 2)))
# print(d)
# d = {}
# d = {1: "1",
#      "2": 2}
# print(d[1])
# print(d["2"])
# print(d.get("23"))
#
# print(d.items())
# print(d.keys())
# print(d.values())
#
# for key in d:
#      print(key, d[key])
#
# for key, value in d.items():
#      print(key, value)
#
#
# l = [i for i in range(5)]
# t = (i for i in range(5))
# s = {i for i in range(5)}
# d = {i: i ** 2 for i in range(5)}
#
# print(l)
# print(t)
# print(s)
# print(d)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#
# ]
#
# for row in matrix:
#     print(row)
# print()
#
# for row in matrix:
#     for element in row:
#         print(element, end="\t")
#     print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end="\t")
#     print()

def generate_matrix(n=3, m=3, min_value=0, max_value=100):
    import random
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(min_value, max_value))
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

m = generate_matrix()
print_matrix(m)
m = generate_matrix(10, 10, 1, 20)
print_matrix(m)