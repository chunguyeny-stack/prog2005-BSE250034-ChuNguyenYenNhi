danh_sach = [10, 5, 7, 2, 11, 7, 13]
print("Danh sách ban đầu:", danh_sach)
n_them = int(input("Nhập số cần thêm vào danh sách: "))
danh_sach.append(n_them)
k = int(input("Nhập giá trị k để đếm: "))
print(f"Số {k} xuất hiện {danh_sach.count(k)} lần.")
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
tong_snt = 0
for x in danh_sach:
    if la_so_nguyen_to(x):
        tong_snt += x
print("Tổng các số nguyên tố trong danh sách là:", tong_snt)
danh_sach.sort()
print("Danh sách sau khi sắp xếp:", danh_sach)
danh_sach.clear()
print("Danh sách sau khi xóa:", danh_sach)
