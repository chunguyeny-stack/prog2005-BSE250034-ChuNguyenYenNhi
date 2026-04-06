SinhVien = {
    "Linh":9.0,
    "Hà":8.0,
    "Mai":8.5
}
def diem_trung_binh(SinhVien):
    tong = sum(SinhVien.values())
    return tong/len(SinhVien)
print("Điểm trung bình:",diem_trung_binh(SinhVien))
