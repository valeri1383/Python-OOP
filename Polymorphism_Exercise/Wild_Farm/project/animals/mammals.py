#from Python_OOP.Polymorphism_Exercise.Wild_Farm.project.animals.animal import Mammal
from project.animals.animal import Mammal
#from Python_OOP.Polymorphism_Exercise.Wild_Farm.project.food import Vegetable, Meat
from project.food import Vegetable, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += food.quantity * 0.10
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.40
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += food.quantity * 0.30
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 1
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'

