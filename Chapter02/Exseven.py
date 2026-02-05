a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
uscln = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        uscln = i
print("Ước số chung lớn nhất là:", uscln)
