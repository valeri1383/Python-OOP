import unittest


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Kitty')

    def test_cat_size_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_fed_true_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cannot_eat_if_fed(self):
        self.cat.eat()

        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertIsNotNone(context.exception)

    def test_can_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertIsNotNone(context.exception)

    def test_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()

