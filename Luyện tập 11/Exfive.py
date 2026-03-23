my_dict = {
    "name": "Nhi",
    "age": "19",
    "id": "SV001"
}
key = input("Nhập key cần kiểm tra:")
if key in my_dict:
    print(f"key'{key}' tồn tại trong dictionary với gái trị:",{my_dict[key]})
else:
    print(f"key'{key}' không tồn tại trong dictionary.")
