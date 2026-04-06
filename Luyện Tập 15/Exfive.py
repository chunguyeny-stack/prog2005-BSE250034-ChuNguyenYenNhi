def count_vowels(s):
    vowels = ("aeiouAEIUO")
    tong = 0
    for n in s.lower():
        if n in vowels:
            tong += 1
        return tong
a = int(input("Nhập chuỗi:"))
print("Số nguyên âm là:", count_vowels(a))
