scores = []
for i in range(3):
 scores.append(float(input(f"Nhập điểm môn thứ {i+ 1}:")))
TB = sum(scores) / 3
if TB >= 8:
    print("Giỏi")
elif 6.5 <= TB < 7.9:
    print("Khá")
elif 5 <= TB < 6.4:
    print("Trung bình")
else:
    print("Yếu")
