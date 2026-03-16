class SinhVien:
    count = 0
    def __init__(self, name):
        self.name = name
        SinhVien.count += 1
    @classmethod
    def dem_so_doi_tuong(cls):
        print("Số đối tượng đã tạo:", cls.count)
sinh_vien1 = SinhVien("Linh")
sinh_vien2 = SinhVien("Hoa")
sinh_vien3 = SinhVien("Mai")
SinhVien.dem_so_doi_tuong()
