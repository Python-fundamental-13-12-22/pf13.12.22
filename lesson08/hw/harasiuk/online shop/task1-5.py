class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f"{self.shop_name=} {self.store_type=}")

    def open_shop(self):
        print(f"{self.shop_name} is open!")

    def set_number_of_units(self, n_o_u):
        self.number_of_units = int(n_o_u)

    def increment_number_of_units(self, delta_units):
        self.number_of_units =  self.number_of_units + delta_units


store = Shop("store", "default store")
print(f"{store.shop_name=}")
print(f"{store.store_type=}")
store.describe_shop()
store.open_shop()

music_shop = Shop("Note", "music shop")
music_shop.describe_shop()
print(f"{store.number_of_units=}")
store.number_of_units = 10
print(f"{store.number_of_units=}")
store.set_number_of_units(8)
print(f"{store.number_of_units=}")
store.increment_number_of_units(3)
print(f"{store.number_of_units=}")


class Discount(Shop):
    def __init__(self, shop_name, store_type, number_of_units=0, discount_products=[]):
        super().__init__(shop_name, store_type, number_of_units, )
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        for products in self.discount_products:
            print(products)


store_discount = Discount("store discount", "discount", 3, ["pen", "apple_pen", "not apple pen"])
store_discount.get_discounts_ptoducts()
