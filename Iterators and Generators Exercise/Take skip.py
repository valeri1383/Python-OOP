class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            temp = self.current_num
            self.current_num += self.step
            self.counter += 1
            return temp
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
    print()

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
