def tinh_toan(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat
t = (2, 4, 6, 8)
ket_qua = tinh_toan(t)
print("Tổng:", ket_qua[0])
print("Lớn nhất:", ket_qua[1])
print("Nhỏ nhất:", ket_qua[2])
