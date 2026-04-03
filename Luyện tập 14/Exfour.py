class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
B1 = Book("Book1",50000)
print("Giá sách", B1.get_price())
