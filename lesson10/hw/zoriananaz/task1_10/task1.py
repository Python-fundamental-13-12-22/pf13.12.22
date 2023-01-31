class Phone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


class Cellphone(Phone):
    def __init__(self, name, brand, price, color, memory):
        super().__init__(name, brand, price)
        self.color = color
        self.memory = memory


class Radiophone(Phone):
    def __init__(self, name, brand, price, phone_reach, answering_machine):
        super().__init__(name, brand, price)
        self.phone_reach = phone_reach
        self.answering_machine = answering_machine





