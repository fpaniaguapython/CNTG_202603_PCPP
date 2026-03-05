# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
    
p1 = Person('nombre', 18)
p2 = Person.fromBirthYear('nombre', 16)
print(Person.isAdult(p1.age))
print(Person.isAdult(p2.age))