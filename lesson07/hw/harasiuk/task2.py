class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = first_name + " " + last_name
        self.email = first_name.lower() + "." + last_name.lower() + "@company.com"


me = Employee("Kolya", "Harasiuk")
print(me.email)
print(me.fullname)
