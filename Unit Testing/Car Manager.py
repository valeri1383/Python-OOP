import unittest


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car('skoda', 'rapid', 6, 50)

    def test_constructor(self):
        self.assertEqual(self.car.make, 'skoda')
        self.assertEqual(self.car.model, 'rapid')
        self.assertEqual(self.car.fuel_consumption, 6)
        self.assertEqual(self.car.fuel_capacity, 50)

    def test_make_method_when_valid(self):
        self.car.make = 'BMW'
        self.assertEqual(self.car.make, 'BMW')

    def test_make_method_when_invalid(self):
        with self.assertRaises(Exception) as context:
            self.car.make('')

        self.assertIsNotNone(context.exception)

    def test_set_new_model_when_valid(self):
        self.car.model = 'M5'
        self.assertEqual(self.car.model, 'M5')

    def test_set_new_model_when_invalid(self):
        with self.assertRaises(Exception) as context:
            self.car.model('')

        self.assertIsNotNone(context.exception)

    def test_set_fuel_consumption_when_valid(self):
        self.car.fuel_consumption = 10
        self.assertEqual(self.car.fuel_consumption, 10)

    def test_set_fuel_consumption_when_invalid(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption('')

        self.assertIsNotNone(context.exception)

    def test_set_fuel_capacity_when_valid(self):
        self.car.fuel_capacity = 60
        self.assertEqual(self.car.fuel_capacity, 60)

    def test_set_fuel_capacity_when_invalid(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity('')

        self.assertIsNotNone(context.exception)

    def test_set_fuel_amount_when_valid(self):
        self.car.fuel_amount = 100
        self.assertEqual(self.car.fuel_amount, 100)

    def test_set_fuel_amount_when_invalid(self):
        with self.assertRaises(Exception) as context:
            self.car.make('')

        self.assertIsNotNone(context.exception)

    def test_refuel_method_when_fuel_is_valid(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_refuel_method_when_fuel_is_invalid(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)

        self.assertIsNotNone(context.exception)

    def test_drive_method_when_distance_is_possible(self):
        self.car.fuel_amount = 10
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 4)

    def test_drive_method_when_distance_is_impossible(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(100)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()