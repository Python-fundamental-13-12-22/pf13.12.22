class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        if self.age < other_person.age:
            print(f'{self.name}: is younger than me')
        elif self.age > other_person.age:
            print(f'{self.name} is older than me')
        else:
            print(f'{self.name} is the same age as me')

p1 = Person('Дэн', 26)
p2 = Person('Дання', 19)
p3 = Person('Дианна', 30)
p1.compare_age(p2)
p2.compare_age(p3)
p3.compare_age(p1)
p3.compare_age(p3)
