#from Python_OOP.Testing_Exercise.hero.project.hero import Hero
from project.hero import Hero
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Val', 5, 100, 20)
        self.enemy_hero = Hero('Ivo', 4, 100, 25)

    def test_constructor(self):
        self.assertEqual(self.hero.username, 'Val')
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 20)

    def test_enemy_name_same_as_hero_name(self):
        enemy_hero = Hero('Val', 60, 100, 10)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertIsNotNone(context.exception)

    def test_hero_health_eq_to_0(self):
        self.hero.health = 0
        self.assertEqual(0, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertIsNotNone(ex.exception)

    def test_hero_health_lower_than_0(self):
        self.hero.health = -5
        self.assertEqual(-5, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertIsNotNone(ex.exception)

    def test_enemy_health_lower_than_0(self):
        self.enemy_hero.health = -5
        self.assertEqual(-5, self.enemy_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertIsNotNone(ex.exception)

    def test_enemy_hero_health_eq_to_0(self):
        self.enemy_hero.health = 0
        self.assertEqual(0, self.enemy_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertIsNotNone(ex.exception)

    def test_fight_draw_case(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual('Draw', result)

    def test_hero_win(self):
        self.hero.damage = 30
        self.hero.health = 110
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(35, self.hero.damage)

    def test_hero_loose(self):
        self.enemy_hero.damage = 30
        self.enemy_hero.health = 110
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(5, self.enemy_hero.level)
        self.assertEqual(15, self.enemy_hero.health)
        self.assertEqual(35, self.enemy_hero.damage)

    def test_custom_str(self):
        self.assertEqual("Hero Val: 5 lvl\nHealth: 100\nDamage: 20\n", str(self.hero) )


if __name__ == '__main__':
    unittest.main()

