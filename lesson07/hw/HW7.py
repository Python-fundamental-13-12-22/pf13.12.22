#1

class Person():
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def compare_age(self,other_person):
        if self.age>other_person.age:
            return f"{other_person.name} is younger than me"
        elif self.age<other_person.age:
            return f"{other_person.name} is older than me"
        elif self.age==other_person.age:
            return f"{other_person.name} is the same as me"
p1=Person("Yulia-Maria",17)
p2=Person("Ruslan",43)
p3=Person("Maksym",17)
print(p1.compare_age(p2))
print(p1.compare_age(p3))

#2

class Employee():
    def __init__(self,fname, lname):
        self.fname=fname
        self.lname=lname
        self.fullname=f"{fname} {lname}"
        self.gmail=f"{fname}.{lname}@compony.com"
emp1=Employee("Yulia","Lokot")
emp2=Employee("Maksym", "Mytnyk")
print(emp1.fullname, emp1.gmail)
print(emp2.fullname,emp2.gmail)

#3

class Name():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.fullname=f"{fname} {lname}"
        self.initials=f"{fname[0::-1]}.{lname[0::-1]}."
name1=Name("Yulia","Lokot")
print(name1.fullname,name1.initials)