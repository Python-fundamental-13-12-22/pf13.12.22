class User():

    def __init__(self, first_name, last_name, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name, self.last_name)

    def greeting_user(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Reset login attempts!")

u1 = User("Dmytro", "Petrenko")

u1.describe_user()
u1.greeting_user()

u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(u1.login_attempts)

u1.reset_login_attempts()
print(u1.login_attempts)

class Admin(User):

    def __init__(self, first_name, last_name, privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]):
        self.first_name = first_name
        self.last_name = last_name
        self.privilages = privileges

    def show_privileges(self):
        print(self.privilages)

Admin = Admin("Mykola", "Usyk")

Admin.show_privileges()

class Privileges():

    def __init__(self, first_name, last_name, privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]):
        self.first_name = first_name
        self.last_name = last_name
        self.privilages = privileges

    def show_privileges(self):
        print(self.privilages)

priv = Admin.privilages
print(priv)

Admin2 = Privileges("Petro", "Dmytrov")
Admin2.show_privileges()
