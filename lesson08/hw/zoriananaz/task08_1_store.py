class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(self.shop_name, self.store_type)

    def open_shop(self):
        print(f"{self.shop_name} is open")

    def set_number_of_units(self, numb):
        self.number_of_units = int(numb)

    def increment_number_of_units(self, increase=0):
        self.number_of_units += increase


store = Shop("Olenka", "cloth")
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()
store_2 = Shop("Moyo", "devices")
store_2.describe_shop()

print(f"{store.number_of_units = }")
store.number_of_units = 8
print(f"{store.number_of_units = }")
store.set_number_of_units(6)
print(f"{store.number_of_units = }")
store.increment_number_of_units(3)
print(f"{store.number_of_units = }")


class Discount(Shop):
    discount_products = ["Cherry wine", "Brownie"]

    def get_discounts_products(self):
        for product in self.discount_products:
            print(product)


store_discount = Discount("Tasty food", "food", 2)
store_discount.get_discounts_products()
