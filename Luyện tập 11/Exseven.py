import csv
ten = input("Nhập tên nhân viên: ")
tuoi = input("Nhập tuổi: ")
nv_id = input("Nhập ID nhân viên: ")
with open("nhan_vien.txt", "w", encoding="utf-8") as f:
    f.write(f"{nv_id}, {ten}, {tuoi}")
print("Đã lưu vào nhan_vien.txt")
with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Tuổi"])
    writer.writerow([nv_id, ten, tuoi])
print("Đã lưu vào nhan_vien.csv")
