class Name:

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.fullname = self.fname + ' ' + self.lname
        self.initials = self.fname[0] + '.' + self.lname[0]





first_name = 'Андрей'
last_name = 'Бондаренко'

person = Name(first_name, last_name)
print(person.fullname)
print(person.initials)