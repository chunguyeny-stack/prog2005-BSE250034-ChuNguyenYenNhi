numbers = [int(x) for x in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
even_numbers = []
sum_even = 0
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        sum_even += num
print("Các số chẵn trong danh sách là:", even_numbers)
print("Tổng các số chẵn:", sum_even)
