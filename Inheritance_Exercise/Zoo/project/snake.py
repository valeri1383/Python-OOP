#from Python_OOP.Inheritance_Exercise.Zoo.project.reptile import Reptile
from project.reptile import Reptile


class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)
