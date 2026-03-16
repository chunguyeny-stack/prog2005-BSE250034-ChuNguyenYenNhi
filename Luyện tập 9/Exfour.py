n = input("Nhập một chuỗi:")
in_hoa = in_thuong = chu_so = dac_biet = khoang_trang = nguyen_am = phu_am = 0
for c in n:
    if c.isupper():
        in_hoa += 1
    if c.islower():
        in_thuong += 1
        if c in "ueoai":
            nguyen_am += 1
        else:
            phu_am += 1
    if c.isdigit():
        chu_so += 1
    if c == " ":
        khoang_trang += 1
    if not c.isalnum() and c != " ":
        dac_biet += 1
print("Số lượng chữ cái in hoa:", in_hoa)
print("Số lượng chữ cái in thường:", in_thuong)
print("Số lượng chữ số:", chu_so)
print("Số lượng ký tự đặc biệt:", dac_biet)
print("Số lượng ký tự khoảng trắng:", khoang_trang)
print("Số lượng nguyên âm:", nguyen_am)
print("Số lượng phụ âm:", phu_am)
