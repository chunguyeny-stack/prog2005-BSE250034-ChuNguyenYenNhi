input_str=input("Nhập danh sách số (cách nhau bằng khoảng trắng):")
danh_sach_so = [int(x) for x in input_str.split()]
so_chan = [n for n in danh_sach_so if n % 2 == 0]
tong_chan = sum(so_chan)
print("Các số chẵn", so_chan)
print("Tổng các số chẵn", tong_chan)
