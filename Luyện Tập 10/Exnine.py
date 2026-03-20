class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Tuổi không được âm")
        self._name = name
        self._age = age
    def get_name(self):
        return self._name
    def set_name(self, name):
        if not name:
            raise ValueError("Tên không được rỗng")
        self._name = name
    def __str__(self):
        return f"Person(name={self._name}, age={self._age})"
    def introduce(self):
        return f"Xin chào, tôi là {self._name}"
    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name, int(age))
    @staticmethod
    def is_adult(age):
        return age >= 18
    def __eq__(self, other):
        return self._name == other._name and self._age == other._age
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def __str__(self):
        return f"Student(name={self._name}, age={self._age}, id={self.student_id})"
p1 = Person("Châu", 20)
p2 = Person.from_string("Hông,22")
s1 = Student("Linh", 19, "SV01")
print(p1)
print(p2)
print(s1)
print(p1.introduce())
print("Linh là người lớn?", Student.is_adult(s1._age))
print("p1 == p2 ?", p1 == p2)


