class Person:
    my_age = 25


    def __init__(self, name, age):
        self.name = name
        self.age = age


    def compare_age(self):
        if self.age > self.my_age:
            print(f"{self.name} is older than as me.")
        elif self.age < self.my_age:
            print(f"{self.name} is younger than me.")
        else:
            print(f"{self.name} is the same age as me.")


p1 = Person("Andriy", 18)
p2 = Person("Andriy1", 20)
p3 = Person("Andriy2", 19)
p2.compare_age()
