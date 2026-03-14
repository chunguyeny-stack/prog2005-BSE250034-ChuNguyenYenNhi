def diem_trung_binh(ds):
    tong = sum(ds.values())
    so_sv = len(ds)
    return tong / so_sv
sinh_vien = {
    "My": 8,
    "Linh": 8,
    "Châu": 9
}
tb = diem_trung_binh(sinh_vien)
print("Điểm trung bình:", tb)
