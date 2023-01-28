class Phone:
    def __init__(self, name="", brand="", price=0):
        self._name = name
        self._brand = brand
        self._price = price
    def find_radio(self):
        if self.type_phone == "радіотелефон":
            return True
    def __repr__(self):
        return f"({self._name}, {self._brand},{self._price})"
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
class MobilePhone(Phone):
    def __init__(self, name="", brand="", price=0, color="", memory='0'):
        super().__init__(name, brand, price)
        self._color = color
        self._memory = memory
    def __repr__(self):
        return f"({self._name}, {self._brand},{self._price},{self._color},{self._memory})"
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    @property
    def memory(self):
        return self._memory
    @memory.setter
    def memory(self, memory):
        self._memory = memory
class RadioPhone(Phone):
    def __init__(self, name="", brand="", price=0, radius=0, answering=""):
        super().__init__(name, brand, price)
        self._radius = radius
        self._answering = answering
    def __repr__(self):
        return f"({self._name}, {self._brand},{self._price},{self._radius},{self._answering})"
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, radius):
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

phones_arr = []
for i in range(0,len(s)):
    name = s[i][1]
    brand = s[i][2]
    price = s[i][3]
    type_phone = s[i][0]

    if type_phone == 'радіотелефон':
        radius = s[i][4]
        answering = ''.join(filter(str.isalnum,s[i][5] ))
        phone = RadioPhone(name=name,
                           brand=brand,
                           price=price,
                           radius=radius,
                           answering=answering)

    elif type_phone == 'мобільний телефон':
        color = s[i][4]
        memory = s[i][5].isalnum()
        phone = MobilePhone(name=name,
                            brand=brand,
                            price=price,
                            color=color,
                            memory=memory)
    phones_arr.append(phone)
phones_arr.sort(key=lambda phone: int(phone.price))
#print(phones_arr)
with open('out1.txt', 'w') as file:
   for phone in phones_arr:
       file.write(f"{phone} \n")
   print (f' file out1.txt saved')
#print(phones_arr)
answ_radiophone = [phone for phone in phones_arr if type(phone) is RadioPhone]
#print(answ_radiophone)
with open('out2.txt', 'w') as file:
   for k in answ_radiophone:
       #print(type(k.answering))
       if k.answering == 'Yes':
           file.write(f'{k} \n')
   print(f' file out2.txt saved')