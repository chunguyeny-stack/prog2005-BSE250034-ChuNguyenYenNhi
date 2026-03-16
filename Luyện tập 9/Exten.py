class SinhVien:
    def __init__(self, diem):
        self.diem = diem
    def __eq__(self, other):
        return self.diem == other.diem
sinh_vien1 = SinhVien(7.8)
sinh_vien2 = SinhVien(9)
if sinh_vien1 == sinh_vien2:
    print("Hai sinh viên có điểm bằng nhau")
else:
    print("Hai sinh viên có điểm không bằng nhau")
