class Shop:
    def __init__(self, shop_name="homebox", store_type="ecomerce", number_of_units=0):
        self._shop_name = shop_name
        self._store_type = store_type
        #task 3
        self.number_of_units = number_of_units
    def __repr__(self):
        return f"({self._shop_name}, {self._store_type},{self._number_of_units})"
    @property
    def shop_name(self):
        #print("get_shop_name")
        return self._shop_name
    @shop_name.setter
    def store_type(self, shop_name):
        self._shop_name = shop_name
    @property
    def store_type(self):
        #print("get_store_type")
        return self._store_type
    @store_type.setter
    def store_type(self, store_type):
        self._store_type = store_type
    @property
    def number_of_units(self):
        return self._number_of_units
    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units
    def describe_shop(self):
        print(self.shop_name)
        print(self.store_type)
    def open_shop(self):
        print(f"""{self.store_type.capitalize()} магазин  {self.shop_name.upper()}  відкрито!""")
    def set_number_of_units(self, st_number_of_units):
        self.number_of_units = st_number_of_units
        return self.number_of_units
    def increment_number_of_units(self, incr_st_number_of_units):
        self.number_of_units += incr_st_number_of_units
        return self.number_of_units

class Discount(Shop):
    def __init__(self, shop_name="homebox", store_type="ecomerce", number_of_units=0,
        discount_products=['iphone 12','iphone 13','iphone 13 pro','iphone 13 max']):
            super().__init__(shop_name, store_type, number_of_units)
            self._discount_products = discount_products
    def __repr__(self):
        return f"({self._shop_name}, {self._store_type},{self._number_of_units}, {self._discount_products} )"
    @property
    def discount_products(self):
        return self._discount_products
    @discount_products.setter
    def discount_products(self, discount_products):
        self._discount_products = discount_products
    def get_discounts_products(self):
        print(self.discount_products)

        

print('------- task 1')
store = Shop()
print('------- атрибут 1')
print(store.shop_name)
print('------- атрибут 2')
print(store.store_type)
print('------- Методи')
store.describe_shop()
store.open_shop()
print('------- task 2')
store_new = Shop("Магазин інструментів PPF", "online-market")
store_new.describe_shop()
print('------- task 3')
print(store.number_of_units)
store.number_of_units = 1000
print(store.number_of_units)
print('------- task 4')
print(store.set_number_of_units(1500))
print(store.increment_number_of_units(20))
print('------- task 5')
store_discount = Discount(Shop)
store_discount.get_discounts_products()

#store_discount.get_discounts_products()




















