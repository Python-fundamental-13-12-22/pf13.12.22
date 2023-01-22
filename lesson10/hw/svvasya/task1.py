class Phone:

    def __init__(self, name="", brand="", price=0, type_phone=""):
        self._name = name
        self._brand = brand
        self._price = price
        self._type_phone = type_phone
    def find_radio(self):
        if self.type_phone == "радіотелефон":
            return True
    def __repr__(self):
        return f"({self._name}, {self._brand},{self._price},{self._type_phone})"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price
    @property
    def type_phone(self):
        return self._type_phone
    @type_phone.setter
    def type_phone(self, type_phone):
        self._type_phone = type_phone
class MobilePhone(Phone):
    def __init__(self, name="", brand="", price=0, type_phone="", color="", memory=0):
        super().__init__(name, brand, price, type_phone)
        self._color = color
        self._memory = memory

    @property
    def color(self):
        return self._color
    @color.setter
    def name(self, color):
        self._color = color
    @property
    def memory(self):
        return self._memory
    @memory.setter
    def memory(self, memory):
        self._memory = memory
class RadioPhone(Phone):
    def __init__(self, name="", brand="", price=0, type_phone ="", radius=0, answering=False):
        super().__init__(name, brand, price, type_phone)
        self._radius = radius
        self._answering = answering
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def name(self, radius):
        self._radius = radius
    @property
    def answering(self):
        return self._answering
    @answering.setter
    def answering(self, answering):
        self._answering = answering

inputFile = open("motorola.txt", "r")
s = []
for line in inputFile:
    s_i = line.encode('cp1251').decode('utf8').split(',')
    s.append(s_i)
inputFile.close()
inputFile = open("samsung.txt", "r")

for line in inputFile:
    s_i = line.encode('cp1251').decode('utf8').split(',')
    s.append(s_i)
inputFile.close()

phone = Phone()
phone_radio = RadioPhone()
output_temp = {}
output_temp_2 = {}
summ = 0
for i in range(0,len(s)):
    phone.name = s[i][1]
    phone.brand = s[i][2]
    phone.price = s[i][3]
    phone.type_phone = s[i][0]
    output_temp[phone.name + " " + phone.brand] = int(phone.price)
    summ += int(phone.price)
    if phone.find_radio() == True:
        phone_radio.answering = s[i][5]
        output_temp_2[phone.name] = phone_radio.answering
output_temp['SUMM'] = summ

with open('out1.txt', 'w') as file:
    for key, value in output_temp.items():
        file.write('%s,%s\n' % (key, value))
    print (f' file out1.txt saved')

with open('out2.txt', 'w') as file:
    for key, value in output_temp_2.items():
        file.write('%s,%s\n' % (key, value))
    print(f' file out2.txt saved')


