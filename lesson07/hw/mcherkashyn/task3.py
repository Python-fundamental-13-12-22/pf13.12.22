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

p1 = Name("Dmytro", "Honchar")
p2 = Name("Anton", "Dzyuba")
p3 = Name("Petro", "Shevchenko")

print(p2.fullname())
print(p2.initials())
