class Employee():
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def fullname(self):
        result = self.first + " " + self.last
        return result
    def email(self):
        result = self.first + "." + self.last + "@company.com"
        return result

p1 = Employee("Dmytro", "Honchar")
p2 = Employee("Anton", "Dzyuba")
p3 = Employee("Petro", "Shevchenko")

print(p1.fullname())
print((p1.email()))
