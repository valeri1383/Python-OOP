#from Python_OOP.Inheritance_Exercise.person.project.person import Person
from project.person import Person

class Child(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)