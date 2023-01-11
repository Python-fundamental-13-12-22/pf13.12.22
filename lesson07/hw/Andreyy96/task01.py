class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.my_age = 26

    def compare_age(self):
        if self.age < self.my_age:
            print(f'{self.name}: {self.age} is younger than me {self.my_age}')
        elif self.age > self.my_age:
            print(f'{self.name}: {self.age} is older than me {self.my_age}')
        else:
            print(f'{self.name}: {self.age} is the same age as me {self.my_age}')

p1 = Person('Дэн', 26)
p1.compare_age()

p2 = Person('Дання', 19)
p2.compare_age()

p3 = Person('Дианна', 30)
p3.compare_age()
