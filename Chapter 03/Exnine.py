numbers = [int(x) for x in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print("Các số lẻ trong danh sách là:", odd_numbers)
