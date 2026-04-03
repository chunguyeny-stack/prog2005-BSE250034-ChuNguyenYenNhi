book = [
    "Book 1;30000",
    "Book 2;50000",
    "Book 3;100000",
    "Tong;900000"
]
with open("books.txt", "w", encoding="utf-8") as f:
    for line in book:
        f.write(line + "\n")
print("Đã tạo file books.txt thành công!")
