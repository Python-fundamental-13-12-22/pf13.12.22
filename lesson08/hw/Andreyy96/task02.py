class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'Полное имъя пользователя: {self.first_name} {self.last_name}')

    def greeting_user(self):
        print(f'Добро пожаловать: {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges

    def show_privileges(self):
        a = 1
        for i in self.privileges:
            print(f'Администратор может: {a} {i}')
            a += 1

    def show_privileges_2(self):
        self.privileges.show_privileges()

class Privileges():

    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        for i in self.privileges:
            print(f'Администратор может: {i}')



user1 = User('Андрей', 'Бондаренко', 18)
user2 = User('Анастасия', 'Бондаренко', 29)

# 01
user1.describe_user()
user1.greeting_user()

# 02
for i in range(3):
    user1.increment_login_attempts()
print(f'Количество попыток ввода: {user1.login_attempts}')
user1.reset_login_attempts()
print(f'Количество попыток ввода: {user1.login_attempts}')

# 03
admin = Admin('Дмитрий', 'Куценко', 55, ['Allowed to add message', 'Allowed to delete users', 'Allowed to ban user'])
admin.show_privileges()

# 04
priv = Privileges()
priv.privileges = ['Allowed to add message', 'Allowed to delete users', 'Allowed to ban user']
admin2 = Admin('Анастасия', 'Бондаренко', 29, priv)
admin2.show_privileges_2()



