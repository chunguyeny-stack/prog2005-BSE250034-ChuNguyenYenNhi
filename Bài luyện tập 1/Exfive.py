import random
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)
print("Ma trận:")
for row in matrix:
    print(row)
r = int(input("Nhập hàng muốn xem: "))
print("Hàng:", matrix[r-1])
c = int(input("Nhập cột muốn xem: "))
for i in matrix:
    print(i[c-1])
max_value = max(max(row) for row in matrix)
print("Giá trị lớn nhất:", max_value)
