class User:
    def __init__(self, first_name=None, last_name=None, user_email=None, user_age=None):
        self._first_name = first_name
        self._last_name = last_name
        self._user_email = user_email
        self._user_age = user_age
        self.login_attempts = 0


    def __repr__(self):
        return f"({self._first_name}, {self._last_name},{self._user_email},{self._user_age})"
    @property
    def first_name(self):
        #print("get_shop_name")
        return self._first_name
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    @property
    def last_name(self):
        #print("get_store_type")
        return self._last_name
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def user_email(self):
        # print("get_store_type")
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        self._user_email = user_email

    @property
    def user_age(self):
        # print("get_store_type")
        return self._user_age
    @user_age.setter
    def user_age(self, user_age):
        self._user_age = user_age

    @property
    def login_attempts(self):
        # print("get_store_type")
        return self._login_attempts

    @login_attempts.setter
    def login_attempts(self, login_attempts):
        self._login_attempts = login_attempts
    def describe_user(self):
        print(f"""{self.first_name.capitalize()} {self.last_name.capitalize()} """)
    def greeting_user(self):
        print(f"""Вітаємо на нашому сайті {self.first_name.capitalize()} {self.last_name.capitalize()} """)
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self, first_name=None, last_name=None, user_email=None, user_age=None, privileges=['Allowed to add message', 'Allowed to delete users', 'Allowed to ban users']):
        super().__init__(first_name, last_name, user_email, user_age)
        self._privileges = privileges

    @property
    def privileges(self):
        # print("get_store_type")
        return self._privileges

    @privileges.setter
    def login_attempts(self, privileges):
        self._privileges = privileges
    def show_privileges(self):
        print(f"""{self.privileges[0]}, {self.privileges[1]}, {self.privileges[2]} """)
class Privileges(Admin):
    def __init__(self, privileges=['Allowed to add message', 'Allowed to delete users', 'Allowed to ban users']):
        super().__init__(self, privileges)
    def show_privileges(self):
        super().show_privileges()

print('------- task 1')
user = User('Vasyl', 'Svidryk','svvasya@gmail.com',36)
user.describe_user()
user.greeting_user()
print('------- task 2')
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
print('------- task 3')
user_admin = Admin()
user_admin.show_privileges()
print('------- task 4')
priv = Privileges()
priv.show_privileges()
priv2 = Admin()
priv2.show_privileges()