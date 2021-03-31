import unittest


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList(1, 2, 3, 4, 5)

    def test_custom_add_method_when_not_int(self):
        with self.assertRaises(Exception) as context:
            IntegerList.add('6')

        self.assertIsNotNone(context.exception)

    def test_custom_add_method_when_int(self):
        self.list.add(6)
        self.assertEqual(self.list.get_data(), [1, 2, 3, 4, 5, 6])

    def test_remove_index_when_valid(self):
        self.list.remove_index(0)
        self.assertEqual(self.list.get_data(), [2, 3, 4, 5])

    def test_remove_index_when_invalid(self):
        with self.assertRaises(Exception) as context:
            self.list.remove_index(10)

        self.assertIsNotNone(context.exception)

    def test_init_take_only_int(self):
        self.assertTrue(self.list.get_data(), [1, 2, 3, 4, 5])

    def _test_init_raise_error_when_not_int(self):
        with self.assertRaises(Exception) as context:
            IntegerList(1, 2, 3, 4, 5)

        self.assertIsNotNone(context.exception)

    def test_custom_get_when_index_valid(self):
        self.assertTrue(self.list.get(2), 3)

    def test_custom_get_when_index_not_valid(self):
        with self.assertRaises(Exception) as context:
            self.list.get(10)

        self.assertIsNotNone(context.exception)

    def test_custom_insert_when_index_valid(self):
        self.list.insert(0, 10)
        self.assertEqual(self.list.get_data(), [10, 1, 2, 3, 4, 5])

    def test_custom_insert_when_index_not_valid(self):
        with self.assertRaises(Exception) as context:
            self.list.insert(6, 10)

        self.assertIsNotNone(context.exception)

    def test_custom_get_biggest(self):
        self.assertTrue(self.list.get_biggest(), 5)

    def test_custom_get_index(self):
        self.assertTrue(self.list.get_index(2), 1)


if __name__ == '__main__':
    unittest.main()
