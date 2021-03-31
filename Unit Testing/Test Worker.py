import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):

    def setUp(self):
        self.worker = Worker('Valeri', 100, 50)

    def test_worker_correct_name(self):
        self.assertEqual(self.worker.name, 'Valeri')

    def test_worker_salary(self):
        self.assertEqual(self.worker.salary, 100)

    def test_worker_energy(self):
        self.assertEqual(self.worker.energy, 50)

    def test_worker_energy_after_rest_method(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 51)

    def test_worker_work_with_negative_or_0_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as context:
            self.worker.work()

        self.assertIsNotNone(context.exception)

    def test_worker_money_increased_after_work_method(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_worker_energy_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 49)

    def test_get_info(self):
        result = 'Valeri has saved 100 money.'
        self.worker.work()
        self.assertEqual(self.worker.get_info(), result)


if __name__ == '__main__':
    unittest.main()
