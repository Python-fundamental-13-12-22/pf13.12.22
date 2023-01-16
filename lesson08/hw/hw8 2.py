class User:
    login_attempts=0
    def __init__(self,first_name,last_name,login):
        self.first_name=first_name
        self.last_name=last_name
        self.login=login
        User.increment_login_attempts()


    def describe_user(self):
        return self.first_name, self.last_name

    def greeting_user(self):
        return f"Hello, {self.first_name},{self.last_name}"

    @classmethod
    def login_attempts_(cls):
        return cls.login_attempts

    @classmethod
    def increment_login_attempts(cls):
         cls.login_attempts += 1

    @classmethod
    def reset_login_attempts(cls):
         return cls.login_attempts*0

user=User("MaksON", "MOntyk", "maksIScool")
print(user.describe_user())
print(user.greeting_user())
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")
user=User("MaksON", "MOntyk", "maksIScool")


print(f"Login attempts: {User.login_attempts_()}")
print(f"Reset login: {User.reset_login_attempts()}")



class Admin(User):
    def __init__(self,first_name,last_name,login):
        super().__init__(first_name,last_name,login)
    priviliges=["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]
    @classmethod
    def show_privileges(cls):
        return Admin.priviliges
admin=Admin("Yulia","Lokot","ymlokot")
print(f"Administrator has such priviliges as: {admin.show_privileges()}")


class Priviliges(Admin):
    pass
new_admin=Priviliges("Yulia","Lokot","ymlokot")
print(new_admin.show_privileges())