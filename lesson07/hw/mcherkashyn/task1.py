class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def compare_age(self):
        #print(self.age)
        if self.age > Me.age:
            result = "older than"
        elif self.age < Me.age:
            result = "younger than"
        elif self.age == Me.age:
            result = "the same age as"
        return (f"{self.name} is {result} me")

p1 = Person("Dmytro", 28)
p2 = Person("Anton", 10)
p3 = Person("Petro", 22)

Me = Person("Mykhailo", 22)

print(p3.compare_age())
