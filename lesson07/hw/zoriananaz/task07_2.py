"""2. Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
   - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
   - В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи
     ‘@company.com’ наприкінці."""


class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = self.fname + " " + self.lname
        self.email = self.fname.lower() + "." + self.lname.lower() + "@" + "bunge.com"


p = Employee("Zoriana", "Nazaruk")
print(p.fullname)
print(p.email)
