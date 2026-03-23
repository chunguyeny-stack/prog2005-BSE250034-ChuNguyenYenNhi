def sap_xep_chen_giam_dan(danh_sach):
    for i in range(1, len(danh_sach)):
        key = danh_sach[i]
        j = i - 1
        while j >= 0 and len(danh_sach[j]) < len(key):
            danh_sach[j + 1] = danh_sach[j]
            j -= 1
        danh_sach[j + 1] = key
        print(f"Bước {i}: {danh_sach}")
chuoi_list = []
for i in range(5):
    chuoi = input(f"Nhập chuỗi thứ {i+1}: ")
    chuoi_list.append(chuoi)
print("\nQuá trình sắp xếp:")
sap_xep_chen_giam_dan(chuoi_list)
print("Kết quả cuối cùng:", chuoi_list)
