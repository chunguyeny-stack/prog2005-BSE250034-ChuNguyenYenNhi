while True:
    print("\nChọn bài tập:")
    print("1. Bài 9 - 2 class bất kỳ")
    print("2. Bài 10 - Bubble Sort")
    print("3. Thoát")
    choice = input("Nhập lựa chọn: ")
    if choice == "1":
        p = Person("Châu", 20)
        s = Student("Linh", 19, "SV01")
        print(p)
        print(s)
        print(p.introduce())
    elif choice == "2":
        strings = [input("Nhập chuỗi: ") for _ in range(5)]
        n = len(strings)
        for i in range(n):
            for j in range(0, n-i-1):
                if len(strings[j]) < len(strings[j+1]):
                    strings[j], strings[j+1] = strings[j+1], strings[j]
                print("Bước:", strings)
        print("Kết quả cuối:", strings)
    elif choice == "3":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, thử lại.")
