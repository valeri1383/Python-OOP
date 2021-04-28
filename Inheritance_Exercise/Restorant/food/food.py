#from Python_OOP.Inheritance_Exercise.Restorant.project.product import Product
from project.product import Product


class Food(Product):
    def __init__(self, name, price, grams):
        Product.__init__(self, name, price)
        self.grams = grams

    def grams(self):
        return self._grams

