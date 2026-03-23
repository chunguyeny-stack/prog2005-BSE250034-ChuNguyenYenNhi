def nhap_ma_tran(ten, hang, cot):
    mt = []
    for i in range(hang):
        dong = []
        for j in range(cot):
            while True:
                gia_tri = input(f"Nhập {ten}[{i}][{j}]: ")
                if not gia_tri.strip():
                    print("Lỗi: Giá trị không được để trống! Vui lòng nhập lại.")
                else:
                    dong.append(int(gia_tri))
                    break
        mt.append(dong)
    return mt
r = int(input("Nhập số hàng: "))
c = int(input("Nhập số cột: "))
print("\n--- Nhập Ma trận A ---")
mt_a = nhap_ma_tran("A", r, c)
print("\n--- Nhập Ma trận B ---")
mt_b = nhap_ma_tran("B", r, c)
mt_tong = []
for i in range(r):
    dong_moi = []
    for j in range(c):
        dong_moi.append(mt_a[i][j] + mt_b[i][j])
    mt_tong.append(dong_moi)
print("\nKết quả Ma trận A + B:")
for dong in mt_tong:
    print(dong)
