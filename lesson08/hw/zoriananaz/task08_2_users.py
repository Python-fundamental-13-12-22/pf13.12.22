class User:
    def __init__(self, first_name, last_name, age, sex, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greeting_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"reset login attempts")


user = User("Vasia", "Vasin", 18, "male")
user.describe_user()
user.greeting_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)


class Admin(User):
    privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def __init__(self, first_name, last_name, age, sex):
        super().__init__(self, first_name, last_name, age, sex)

    def show_privileges(self):
        for i in self.privileges:
            print(i)


adm = Admin("Petro", "Petrenko", 24, "male")
adm.show_privileges()


class Privileges:
    privileges = Admin.privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


print()
priv = Privileges()
priv.show_privileges()
