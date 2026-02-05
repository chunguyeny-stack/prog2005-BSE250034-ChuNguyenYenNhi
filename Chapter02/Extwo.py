n = int(input("Nhập một số dương: "))
if n < 2:
    print("Không phải là số nguyên tố")
else:
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
    if dem == 2:
        print("Là số nguyên tố")
    else:
        print("Không phải là số nguyên tố")
