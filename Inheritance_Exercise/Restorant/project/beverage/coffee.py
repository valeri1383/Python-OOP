#from Python_OOP.Inheritance_Exercise.Restorant.project.beverage.hot_beverage import HotBeverage
from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name, caffeine):
        HotBeverage(self, name, Coffee.COFFEE_PRICE, Coffee.COFFEE_MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

