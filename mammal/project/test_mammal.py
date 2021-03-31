#from Python_OOP.Testing_Exercise.mammal.project.mammal import Mammal
from project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('Ivo', 'ram', 'bee')

    def test_constructor(self):
        self.assertEqual(self.mammal.name, 'Ivo')
        self.assertEqual(self.mammal.type, 'ram')
        self.assertEqual(self.mammal.sound, 'bee')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), 'Ivo makes bee')

    def test_getting_kingdom(self):
        self.mammal.__kingdom = "animals"
        self.mammal.get_kingdom()
        self.assertEqual(self.mammal.__kingdom, "animals")

    def test_info(self):
        info = self.mammal.info()
        self.assertEqual(info, 'Ivo is of type ram')


if __name__ == '__main__':
    unittest.main()