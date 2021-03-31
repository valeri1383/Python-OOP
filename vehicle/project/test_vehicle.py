from Python_OOP.Testing_Exercise.vehicle.project.vehicle import Vehicle
#from project.vehicle import Vehicle
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 100)

    def test_constructor(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.horse_power, 100)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_when_fuel_enough(self):
        self.vehicle.drive(24)
        self.assertEqual(self.vehicle.fuel, 20)

    def test_drive_when_fuel_not_enough(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(50)

        self.assertIsNotNone(context.exception)

    def test_refuel_when_fuel_enough(self):
        self.vehicle.drive(24)
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 30)

    def test_refuel_when_fuel_too_much(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(30)

        self.assertIsNotNone(context.exception)

    def test_custom_str_method(self):
        info = self.vehicle.__str__()
        self.assertEqual(info, "The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()