#from Python_OOP.Inheritance_Exercise.Need_for_speed.project.Vehicle import Vehicle
from project.vehicle import Vehicle

class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    # def __init__(self, fuel, horse_power):
    #     Vehicle.__init__(self, fuel, horse_power)
    #     self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
