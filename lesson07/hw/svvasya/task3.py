class Name():
    def __init__(self,first_name, last_name):
        self.fname = first_name
        self.lname = last_name
    def fullname(self):
        self.fullname = self.fname + " " +  self.lname
        return self.fullname
    def initials(self):
        self.init = self.fname[0].upper() + "." + self.lname[0].upper() + "."
        return self.init

f_name = Name("Василь", "Свідрик")
print(f_name.fullname())
print(f_name.initials())