mau_sac = ["Red", "Orange", "Green", "Pink", "Black"]
try:
    mau_sac.remove("Green")
    print("Đã xóa màu Green khỏi danh sách")
except:
    print("Không tìm thấy màu Green trong danh sách")
print("Danh sách màu còn lại:", mau_sac)
