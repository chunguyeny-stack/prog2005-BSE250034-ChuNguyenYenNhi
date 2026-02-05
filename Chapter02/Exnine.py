n = input("Nhập số nguyên dương 5 chữ số: ")
chu_so_lon_nhat = int(n[0])
for c in n:
    if int(c) > chu_so_lon_nhat:
       chu_so_lon_nhat = int(c)
print("Chữ số lớn nhất là:", chu_so_lon_nhat)
