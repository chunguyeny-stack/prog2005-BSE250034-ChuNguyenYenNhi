name = input("Nhập tên sinh viên: ")
toan = float(input("Điểm Toán: "))
ly = float(input("Điểm Lý: "))
hoa = float(input("Điểm Hóa: "))

dtb = (toan + ly + hoa) / 3

print("Tên sinh viên:", name)
print("Điểm trung bình:", round(dtb, 2))
