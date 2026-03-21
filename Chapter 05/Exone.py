from matplotlib import pyplot as plt
xep_loai = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
so_hoc_sinh = [6, 10, 12, 4, 1]
plt.bar(xep_loai, so_hoc_sinh)
plt.title("Kết quả học tập của lớp 12a6")
plt.xlabel("Xếp loại")
plt.ylabel("Số học sinh")
plt.show()
