a = []
n = int(input("Nhập n:"))
for i in range(n):
     a.append(int(input()))
tong = 0
for x in a:
    if x % 2 != 0:
        print(x)
        tong += 1
print("Tổng số lượng các số lẻ:", tong)
for x in a:
    if x > 1:
        check = True
        for i in range(2, x):
          if x % i == 0:
            check = False
        if check:
             print(x)
