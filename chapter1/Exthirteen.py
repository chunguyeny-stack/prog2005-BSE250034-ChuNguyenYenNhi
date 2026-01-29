try:
    a = int(input("nhập số a: "))
    b = int(input("nhập số b: "))

    if b == 0:
        print("không thể chia cho 0")
    else:
        print("kết quả:", a / b)

except ValueError:
    print("dữ liệu nhập không hợp lệ")
