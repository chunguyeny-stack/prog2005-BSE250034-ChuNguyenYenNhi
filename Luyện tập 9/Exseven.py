class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, s):
        name, age = s.split("-")
        return cls(name, int(age))
p = Person.from_string("Nhi-19")
print(p.name)
print(p.age)
