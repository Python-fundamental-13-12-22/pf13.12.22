#task1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        if self.age > other_person.age:
            return f"{other_person.name} is younger than me."
        elif self.age < other_person.age:
            return f"{other_person.name} is older than me."
        else:
            return f"{other_person.name} is the same age as me."


p1 = Person("Maks", 18)
p2 = Person("Yura", 43)
p3 = Person("Yulia", 17)
print(p1.compare_age(p2))
print(p1.compare_age(p3))
#task2
class Employee:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        self.fullname = f"{first_name} {last_name}"
        self.email = f"{first_name}@{last_name}.com"
        print(self.email)


result=Employee("Dzulbars", "development")
#task3
class Name:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        self.fullname = f"{first_name} {last_name}"
        self.initials = f"{first_name[0::-1]}.{last_name[0::-1]}"
        print(self.fullname, self.initials)


it=Name("Maksym", "Mytnyk")