from random import randint as ri


# class Person:
#
#     def init(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
#
# person_3 = Person()
# person_3.init("Ana", 18, "women")
#
# print(person_3.name)


# class Person:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         return f"self.name={self.name} {self.age=} {self.sex=}"
#
#     def __repr__(self):
#         return f"<{self.name} {self.age} {self.sex}>"
#
#     @staticmethod
#     def st():
#         print("st")
#
#     @classmethod
#     def cm(cls):
#         print(cls)
#
#
# person_1 = Person("Ana", 18, "women")
# person_2 = Person("Lesii", 68, "women")
# person_3 = Person("Vika", 12, "women")
# person = [person_1, person_2, person_3]
# print(person_3.name)
# print(person_1)
# print(person_2)
# print(person_3)
#
# print(person)
# person_3.st()
# Person.st()
# person_3.cm()
# Person.cm()

class Point:
    def __init__(self, x=0, y=0):
        self._x = x  # pylint: disable=C0103
        self._y = y

    def __repr__(self):
        return f"({self._x}, {self._y})"

    def __add__(self, other):
        print(f"{self}+{other}")
        point = Point()
        if isinstance(other, Point):
            point.x = self._x + other.x
            print(point.y)
            point.y = self._y + other.y
        if type(other) is int:
            point.x = self._x + other
            point.y = self._y + other
        return point

    def __radd__(self, other):
        print(f"{self}+{other}")
        point = Point()
        if type(other) is Point:
            point.x = self._x + other.x
            point.y = self._y + other.y
        if type(other) is int:
            point.x = self._x + other
            point.y = self._y + other
        return point

    def __eq__(self, other):
        print(f"{self}=={other}")
        return self.x == other.x and self.y == other.y

    def get_x(self):
        print("get_x")
        return self._x

    def set_x(self, x):
        self._x = x

    x = property(get_x, set_x)

    @property
    def y(self):
        print("get_y")
        return self._y

    @y.setter
    def y(self, y):
        self._y = y


# points = [Point(ri(-10, 10), ri(-10, 10)) for i in range(10)]
# print(points)
# point = points[0] + points[1]
# print(point)
# point = points[0] + 1
# print(point)
# point = 3 + points[0]
# print(point)
#
# point2 = point
# print(point, id(point))
# print(point2, id(point2))
# print(point == point2)
#
# point3 = Point(point.x, point.y)
# print(point, id(point))
# print(point3, id(point3))
# print(point == point3)

class Point3D(Point):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self._z = z
    def __repr__(self):
        return f"({self._x}, {self._y}, {self._z})"
    def old_repr(self):
        print(super().__repr__())

    @property
    def z(self):
        print("get_z")
        return self._z

    @z.setter
    def z(self, z):
        self._z = z


points = [Point3D(ri(-10, 10), ri(-10, 10), ri(-10, 10)) for i in range(10)]
print(points)
points[0].old_repr()
print(points[0]+points[1])
# points[0].x
# points[0].y
# points[0].z

#
# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B): pass
# class E(B): pass
# class F(C): pass
# class G(E, F): pass
# class K(D, G): pass
#
# print(K.__mro__)