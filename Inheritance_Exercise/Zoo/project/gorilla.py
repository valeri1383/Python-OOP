# from Python_OOP.Inheritance_Exercise.Zoo.project.mammal import Mammal
from project.mammal import Mammal



class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)
