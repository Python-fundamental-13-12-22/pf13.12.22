class Shop():

    def __init__(self, shop_name, store_type, number_of_units = 0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        return self.shop_name, self.store_type

    def open_shop(self):
        return f"{self.shop_name} is open"

    def set_number_of_units(self, number):
        self.number_of_units = number
        return self.number_of_units

    def increment_number_of_units(self, number):
        self.increment_number_of_units = self.number_of_units + number
        return self.increment_number_of_units


store = Shop("Intel", "computer store")
print(f"shop_name: {store.shop_name}")
print(f"store_type: {store.store_type}")
print(store.describe_shop())
print(store.open_shop())

store2 = Shop("Amazon", "marketplace")
print(store2.describe_shop())

print(store.number_of_units)
store.number_of_units = 6
print(store.number_of_units)

print(store.set_number_of_units(20))

print(store.increment_number_of_units(8))

class Discount(Shop):

    def __init__(self, discount_products = []):
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        return self.discount_products

store_discount = Discount(["processor", "motherboard", "fan"])

print(store_discount.get_discounts_ptoducts())
