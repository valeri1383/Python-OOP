# from Python_OOP.Polymorphism_Exercise.Wild_Farm.project.animals.animal import Bird
from project.animals.animal import Bird
# from Python_OOP.Polymorphism_Exercise.Wild_Farm.project.food import Meat, Vegetable, Fruit
from project.food import Meat, Vegetable, Fruit


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.25
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight,wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'

