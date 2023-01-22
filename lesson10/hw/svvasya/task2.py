class Table:
    def __init__(self, size="", material="", price=0):
        self._size = size
        self._material = material
        self._price = price
    def __repr__(self):
        return f"({self._size}, {self._material},{self._price})"
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
    @property
    def material(self):
        return self._material
    @material.setter
    def material(self, material):
        self._material = material
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price


class Chairs:
    def __init__(self, material="", price=0):
        self._material = material
        self._price = price

    def __repr__(self):
        return f"({self._material},{self._price})"

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

inputFile = open("mebli_input.txt", "r")
s = []
for line in inputFile:
    s_i = line.encode('cp1251').decode('utf8').split(',')
    s.append(s_i)
inputFile.close()
print(s)

