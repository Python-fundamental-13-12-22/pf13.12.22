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
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("Anna", "Hrystunyk", 22, "women")
user_2 = User("Andriy", "Ivanov", 35, "men")
user_3 = User("Vitaliy", "Shevchenko", 15, "men")
user_1.describe_user()
user_1.greeting_user()
for i in range(3):
    user_2.increment_login_attempts()
print(f"{user_2.login_attempts=}")
user_2.reset_login_attempts()
print(f"{user_2.login_attempts=}")


class Admin(User):
    def __init__(self, first_name, last_name, age, sex, login_attempts=0, privileges=["Alowed to add message", "Allowed to delete users", "Allowed to ban users"]):
        super().__init__(first_name, last_name, age, sex, login_attempts=0)
        self.privileges = privileges

    def show_privileges(self):
        for privileges in self.privileges:
            print(f"{privileges}")


admin_1 = Admin("Yuriy", "Chern", 48, "men")
admin_1.show_privileges()
print("///////")

class Privileges():
    def __init__(self, privileges=["Alowed to add message", "Allowed to delete users", "Allowed to ban users"]):
        self.privileges = privileges

    def show_privileges(self):
        for privileges in self.privileges:
            print(f"{privileges}")


priv = Privileges()
priv.privileges = ["Alowed to add message", "Allowed to delete users", "Allowed to ban users", "Alowed to mute message"]
admin_2 = Admin("Anton", "Chern", 24, "men")
#для виконання таску 4 код буде суперечити попереднім такскам. Див. код в файлі task4