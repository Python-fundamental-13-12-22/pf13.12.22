"""1. В класі Person визначте метод `compare_age()`, який повертатиме результат порівняння віку людини
з Вашим віком. При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age,
буде повертатися повідомлення наступного формату:
{other_person} is {older than / younger than / the same age as} me."""


class Person:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def compare_age(self, other_person):
        if self.age < other_person.age:
            print(f"{other_person.name} is older than me")
        elif self.age > other_person.age:
            print(f"{other_person.name} is younger than me")
        elif self.age == other_person.age:
            print(f"{other_person.name} is the same age as me")


p1 = Person('Zoriana', 32)
p2 = Person('Valeriy', 33)
p3 = Person('Ivan', 38)
p1.compare_age(p2)
p1.compare_age(p3)
