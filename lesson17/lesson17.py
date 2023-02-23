def my_func(a, b):
    if a < b:
        return a + b
    elif a == b:
        return a ** b
    else:
        return a - b


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Hi, my name is {self.name}. I am {self.age} years old and I am {self.gender}."

    def have_birthday(self):
        self.age += 1
        return f"Happy birthday, {self.name}! You are now {self.age} years old."
