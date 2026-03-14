sinh_vien = {
    "Hoa": 8,
    "Minh": 7,
    "Huyền": 9
}
ten = input("Nhập tên sinh viên: ")
if ten in sinh_vien:
    print("Tồn tại trong dictionary")
else:
    print("Không tồn tại")
