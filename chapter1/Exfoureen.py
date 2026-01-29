import math

x = float(input("nhập một số: "))

if x < 0:
    print("không thể tính căn bậc hai của số âm")
else:
    print("căn bậc hai là:", math.sqrt(x))
