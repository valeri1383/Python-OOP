import random


class RandomList(list):

    def get_random_element(self):
        el = random.randint(self[0], self[-1])
        self.remove(el)
        return self


my_list = RandomList([3, 4, 5])
print(my_list)
print(my_list.get_random_element())