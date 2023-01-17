#task1
class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units


    def describe_shop(self):
        return self.shop_name, self.store_type


    def open_shop(self):
        return "The shop is open from 6am to 21pm ;)"


    def set_number_of_units(self):
        return self.number_of_units


    def increment_number_of_units(self, number):
        self.number_of_units += number


store=Shop("Lum", "Clothes", 17)
print(f"Store: {store.describe_shop()}")
print(store.open_shop())
print(f"Number of units in the store: {store.number_of_units}")
store.increment_number_of_units(7)
print(f"Increment number of units in the store: {store.number_of_units}")
class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products


    def get_discounts_ptoducts(self):
        print(f"The discount products: {self.discount_products}")
store_discout=Discount("Lum", "Discount", ["SHOES", "CAP","TROUSERS","JEANS"])
store_discout.get_discounts_ptoducts()
#task2
class User:
    login_attempts = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        User.increment_login_attempts()

    def describe_user(self):
        return f"{self.first_name} {self.last_name}"

    def greeting_user(self):
        return f"Hello, {self.first_name} {self.last_name}!"

    @classmethod
    def login_attempts_(cls):
        return cls.login_attempts

    @classmethod
    def increment_login_attempts(cls):
        cls.login_attempts += 1

    @classmethod
    def reset_login_attempts(cls):
        cls.login_attempts = 0


class Admin(User):
    priviliges = ["Add message", "Delete users", "Ban users"]

    @classmethod
    def show_privileges(cls):
        return cls.priviliges


user = User("Dzhulbars", "Venatus")
print(user.describe_user())
print(user.greeting_user())
User.increment_login_attempts()
print(f"Login attempts: {User.login_attempts_()}")
User.reset_login_attempts()
print(f"Reset login: {User.login_attempts_()}")
admin = Admin("Dzhulars","c++")
print(f"Administrator has such priviliges as: {admin.show_privileges()}")

