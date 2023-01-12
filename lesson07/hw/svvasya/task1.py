class Person():
    my_age = 36
    def __init__(self, name=None, age=None):
        #print(self, self.__dict__)
        self.name = name
        self.age = age
        #print(self, self.__dict__)
    def compare_age(self):
        if self.age > self.my_age:
            return f"""{self.name} is older than Me"""
        elif self.age < self.my_age:
            return f"""{self.name} is younger than Me"""
        elif self.age == self.my_age:
            return f"""{self.name} is the same age as Me"""

p1 = Person('Тарас', 40)
p2 = Person('Володимир', 35)
p3 = Person('Іван', 36)
print(p1.compare_age())
print(p2.compare_age())
print(p3.compare_age())