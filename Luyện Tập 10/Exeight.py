def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range (0, n - 1 -1):
            if len(arr[j]) < len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"Bước {i+1}: {arr}")
            if not swapped:
                break
danh_sach = []
for k in range (5):
    chuoi = input (f"Nhập chuỗi thứ{k+1}:")
    danh_sach.append(chuoi)
print("\n--- Bắt đầu sắp xếp---")
print("kết quả sau cùng (giảm dần theo độ dài):")
print(danh_sach)
