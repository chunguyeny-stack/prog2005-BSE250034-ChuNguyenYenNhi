def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)
so = int(input("Nhập một số:"))
print(f"Giai thừa của {so} là {giai_thua(so)}")
