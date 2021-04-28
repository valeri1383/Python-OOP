#from Python_OOP.Inheritance_Exercise.Zoo.project.animal import Animal
from project.animal import Animal


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)
