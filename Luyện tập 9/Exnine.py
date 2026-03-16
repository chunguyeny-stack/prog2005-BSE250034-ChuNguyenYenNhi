class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("gâu gâu")
d = Dog("Kiki")
print(d.name)
d.sound()
