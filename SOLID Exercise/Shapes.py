'''
You are provided with code containing class Rectangle and class AreaCalculator.
Refactor the code using the Open/Closed Principle,
so that the code is open for extension (adding more shapes) but closed for modification.
'''
from abc import ABC, abstractmethod


class AreaCalculator(ABC):

    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    @abstractmethod
    def total_area(self):
        total = sum([x.total_area for x in self.shapes])
        return total


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def total_area(self):
        total = self.width * self.height
        return total


class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def total_area(self):
        total = (self.width * self.height) / 2
        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
