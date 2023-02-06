class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        fullname_person = self.first_name + " " + self.last_name

        return fullname_person

    def email(self):
        email_person = self.first_name.lower() + "." + self.last_name.lower() + "@company.com"

        return email_person


person = Employee('Andrii', 'Bondarenko')
print(person.fullname())
print(person.email())
