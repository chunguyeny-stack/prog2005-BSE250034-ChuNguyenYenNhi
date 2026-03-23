arr = ['8, 7, 90, 33 ,4','7, 8, 99','6, 8, 33, 55, 22','4, 67, 88, 90']
print("Danh sách đã sắp xếp:", arr)
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif len(arr[mid]) > len(target):
            left = mid + 1
        else:
            right = mid - 1
    return-1
target = input("Nhập chuỗi cần tìm:")
pos = binary_search(arr, target)
if pos != -1:
    print(f"chuỗi '{target}' nằm ở vị trí {pos} trong danh sách")
else:
    print(f" chuõi '{target} 'không tồn tại trong danh sách.")
