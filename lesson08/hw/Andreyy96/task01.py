class Shop:


    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units


    def describe_shop(self):
        print(f'{self.shop_name=}, {self.store_type=}')

    def open_shop(self):
        print(f'Онлайн-магазин {self.shop_name} открытый')

    def set_number_of_units(self):
        number_of_units = int(input('Введите число количество товару: '))
        self.number_of_units = number_of_units

    def increment_number_of_units(self, number):
        self.number_of_units += number


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products, number_of_units=0):
        super().__init__(shop_name, store_type, number_of_units)
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        for products in self.discount_products:
            print(products)



shop_name = 'SportMaster'
store_type = 'Спортивные товары'
store = Shop(shop_name, store_type)

# 01
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()

# 02
store2 = Shop('Games_shop', 'video_games')
store2.describe_shop()

# 03
print(f'Количество товару на сайте: {store.number_of_units}')
store.number_of_units = 7
print(f'Измененное количество товару на сайте: {store.number_of_units}')

# 04
store.set_number_of_units()
print(f'Количество товару на сайте: {store.number_of_units}')
number = int(input('Введите число увелечение количество товару: '))
store.increment_number_of_units(number)
print(f'Количество товару на сайте: {store.number_of_units}')

# 05
store_discount = Discount(shop_name, store_type, ['HOODY', 'BOOTS'], 2)
store_discount.get_discounts_ptoducts()
