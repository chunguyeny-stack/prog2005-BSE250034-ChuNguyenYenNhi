text = input("Nhập chuỗi: ")
reversed_slicing = text[::-1]
print("Đảo ngược bằng Slicing:", reversed_slicing)
reversed_manual = ""
for ch in text:
    reversed_manual = ch + reversed_manual
print("Đảo ngược không dùng Slicing:", reversed_manual)
