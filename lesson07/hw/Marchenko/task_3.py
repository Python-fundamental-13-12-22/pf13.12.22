class Name():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def fullname(self):
        result = self.fname + " " + self.lname
        return result
    def initials(self):
        result = self.fname[0] + "." + self.lname[0]
        return result

p1 = Name("Ihor", "Marchenko")
p2 = Name("Egor", "Kravchuk")
p3 = Name("Vlad", "Pastuh")

print(p2.fullname())
print(p2.initials())