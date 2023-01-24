# TASK 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        if self.age > other_person.age:
            return f'{other_person.name} is younger than me'
        elif self.age < other_person.age:
            return f'{other_person.name} is older than me'
        else:
            return f'{other_person.name} is the same age as me'

p1 = Person('Андрїй', 10)
p2 = Person('Аліна', 30)
p3 = Person('Олексій', 25)

print(p3.compare_age(p1))
print(p1.compare_age(p2))
print(p3.compare_age(p3))

# TASK 2

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = first + ' ' + last
        self.email = first + '.' + last + "@company.com"

employee1 = Employee('Артем', 'Стрельніков')
print(employee1.fullname)
print(employee1.email)

# TASK 3

class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return self.fname + ' ' + self.lname

    def initials(self):
        return self.fname[0] + '.' + self.lname[0]
