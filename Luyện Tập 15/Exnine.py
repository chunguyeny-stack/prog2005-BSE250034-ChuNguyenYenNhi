a = input("Nhập chuỗi:")
with open("noidung.txt","w", encoding="utf-8") as f:
    f.write(a)
print("Đã lưu vài file output.txt")
