class Product:
    def __init__(self, price):
        self._price = price
    def get_price(self):
        return self._price
    def set_price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Giá phải > 0")
p = Product(5)
print(p.get_price())
