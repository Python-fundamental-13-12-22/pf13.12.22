class Name:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def fullname(self):
        return self.fname, self.lname

    def initials(self):
        return self.fname[0] + "." + self.lname[0]


me = Name("Kolya", "Harasiuk")
fullname = me.fullname()
print(fullname)
initials = me.initials()
print(initials)

