a= int(input("số nguyên thứ nhất: "))
b= int(input("số nguyên thứ hai: "))
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
if b != 0:
    thuong = a / b
else:
    thuong = "không chia cho 0"

print("tổng", tong)
print("hiệu", hieu)
print("tích",tich)
print("thương", thuong)
