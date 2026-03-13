s = "5; 7; 8; -2; 8; 11; 13; 9; 10"
numbers = [int(x) for x in s.split(";")]
for i in numbers:
    print(i, end=" ")
even = sum(1 for i in numbers if i % 2 == 0)
negative = sum(1 for i in numbers if i < 0)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
prime = sum(1 for i in numbers if is_prime(i))
avg = sum(numbers)/len(numbers)
print("Số chẵn:", even)
print("Số âm:", negative)
print("Số nguyên tố:", prime)
print("Trung bình:", avg)
