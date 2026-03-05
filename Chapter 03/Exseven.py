numbers = [int(x) for x in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
target = int(input("Nhập số cần tìm: "))
found_index = -1
for i in range(len(numbers)):
    if numbers[i] == target:
        found_index = i
        break
    print("So sánh với phần tử tại chỉ số", i, ":", numbers[i])
if found_index != -1:
    print("Số", target, "được tìm thấy tại chỉ số:", found_index)
else:
    print("Không tìm thấy số", target, "trong danh sách.")
