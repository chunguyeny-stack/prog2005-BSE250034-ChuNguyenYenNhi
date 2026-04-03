class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
book1 = Book("Book 1", 30000)
book2 = Book("Book 2", 50000)
book3 = Book("Book 3", 100000)
books = [book1, book2, book3]
tong = sum([b.get_price() for b in books])
with open("books.txt", "w", encoding="utf-8") as f:
    for b in books:
        f.write(f"{b.get_name()};{b.get_price()}\n")
    f.write(f"Tong;{tong}\n")
print("Đã ghi dữ liệu vào file books.txt thành công!")



