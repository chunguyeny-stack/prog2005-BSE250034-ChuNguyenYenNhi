ma=input("Nhập mã sản phẩm: ")
ten=input("Nhập tên sản phẩm: ")
gia=float(input("Nhập giá sản phẩm: "))
tep=open("sanpham.txt","a",encoding="utf-8")
tep.write(ma+";"+ten+";"+str(gia)+"\n")
tep.close()
tep=open("sanpham.txt","r",encoding="utf-8")
dulieu=tep.readlines()
tep.close()
danhsach=[]
for dong in dulieu:
 tach=dong.strip().split(";")
 danhsach.append(tach)
print("Danh sách sản phẩm:")
for sp in danhsach:
 print(sp[0],sp[1],sp[2])
danhsach.sort(key=lambda x:float(x[2]),reverse=True)
print("Sản phẩm sau khi sắp xếp giá giảm dần:")
for sp in danhsach:
 print(sp[0],sp[1],sp[2])





