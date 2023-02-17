class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=number_of_units
    def describe_shop(self):
        return self.shop_name ,self.store_type
    def open_shop(self,):
        return "The store is open"
    def set_number_of_units(self):
        return self.number_of_units
    def increment_number_of_unit(self,number):
        self.number_of_units+=number
store=Shop("Lum", "clothes",10)
print(f"Store number 1: {store.describe_shop()}")
print(store.open_shop())
print(f"Number of units in store : {store.number_of_units}")
store.increment_number_of_unit(10)
print(f"Increment number of units in store : {store.number_of_units}")
class Discount(Shop):
    def __init__(self,shop_name, store_type, discount_products):
        super().__init__(shop_name,store_type)
        self.discount_products = discount_products

    def get_discount_products(self):
        print(f"Discount products: {self.discount_products}")

store_discount=Discount("Lum","clothes",["Bags","T-shirts"])
store_discount.get_discount_products()
