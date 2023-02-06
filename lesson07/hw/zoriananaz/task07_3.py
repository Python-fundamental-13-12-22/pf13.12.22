"""3. В класі Name визначте:
   - атрибути для first name та last name (fname та lname відповідно);
   - метод fullname що повертає first і last names;
   - метод initials який повертає ініціали (перші літери first та last name, розділених ‘.’ ."""


class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return self.fname + " " + self.lname

    def initials(self):
        return self.fname[0] + "." + self.lname[0]


p = Name("Zoriana", "Nazaruk")
print(p.fullname())
print(p.initials())
