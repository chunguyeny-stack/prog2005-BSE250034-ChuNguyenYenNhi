class Product:
    def __init__(self, price):
        self.price = price
@property
def price(self):
       return self.__price
@price.setter
def price(self, value):
    if value < 0:
        print("Lỗi")
    else:
        self.__price = value
p = Product(100)
print(p.price)
