"""1. В класі Person визначте метод `compare_age()`, який повертатиме результат порівняння віку людини
з Вашим віком. При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age,
буде повертатися повідомлення наступного формату:
{other_person} is {older than / younger than / the same age as} me."""


class Person:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def сompare_age(self, other_person):

        if self.age < other_person.age:
            print(f"{other_person.age} is older than me")
        if self.age > other_person.age:
            print(f"{other_person.age} is younger than me")
        if self.age == other_person.age:
            print(f"{other_person.age} is the same age as me")


p1 = Person('Me', 32)
p2 = Person('Valeriy', 33)
p3 = Person('Lubchuk', 38)
print(p1.сompare_age(p2.age))
