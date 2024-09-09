class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

from person import Person
jane = Person("Jane", 25)
print(getattr(jane, "name"))
print(getattr(jane, "age"))
setattr(jane, "age", 26)
print(jane.age)
delattr(jane, "age")
jane.age