class reverse_iter:
    def __init__(self, item):
        self.item = item
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= len(self.item):
            temp = self.counter
            self.counter += 1
            return self.item[-temp]
        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
