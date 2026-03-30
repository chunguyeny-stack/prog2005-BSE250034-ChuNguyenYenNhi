 class Flower:
    def __init__(self, color):
        self.__color = color
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
f = Flower("Đỏ")
print("Màu hoa:", f.get_color())
f.set_color("Vàng")
print("Màu mới:", f.get_color())
