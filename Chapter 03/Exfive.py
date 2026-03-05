numbers = [float(x) for x in input("Nhập các số thực, cách nhau bởi dấu cách: ").split()]
print("Danh sách ban đầu:", numbers)
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] < key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key
print("Danh sách sau khi sắp xếp giảm dần:", numbers)
