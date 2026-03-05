numbers = [int(x) for x in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
print("Danh sách ban đầu:", numbers)
swap_count = 0
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swap_count += 1
print("Danh sách sau khi sắp xếp tăng dần:", numbers)
print("Số lần hoán đổi:", swap_count)
