m, n = map(int, input("Nhập số hàng và số cột (cách nhau bởi dấu cách): ").split())
print("Nhập ma trận A:")
A = []
for i in range(m):
    row = [int(x) for x in input().split()]
    A.append(row)
print("Nhập ma trận B:")
B = []
for i in range(m):
    row = [int(x) for x in input().split()]
    B.append(row)
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("Kết quả cộng hai ma trận:")
for row in C:
    print(row)
