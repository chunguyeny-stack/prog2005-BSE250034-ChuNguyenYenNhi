thong_tin = {}
n = int(input("Bạn muốn nhập bao nhiêu người? "))
for i in range(n):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    tuoi = int(input(f"Nhập tuổi của {ten}: "))
    thong_tin[ten] = tuoi
if n > 0:
    tong_tuoi = sum(thong_tin.values())
    tuoi_tb = tong_tuoi / n
    print(f"Tuổi trung bình của {n} người là: {tuoi_tb}")
