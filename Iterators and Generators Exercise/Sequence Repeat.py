class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.counter_iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter_iterations < self.number:
            if len(self.sequence) <= self.counter:
                self.counter = 0
            temp_symbol = self.sequence[self.counter]
            self.counter += 1
            self.counter_iterations += 1
            return temp_symbol
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
