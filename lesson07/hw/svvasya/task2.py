class Employee():
    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.age = lastname
        self.fullname = firstname + " " + lastname
        self.email = firstname.lower() + "." + lastname.lower() + "@" + "gmail.com"

f_name = Employee("Vasyl","Svidryk")
print(f_name.fullname)
print(f_name.email)