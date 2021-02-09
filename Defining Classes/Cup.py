class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        self.milliliters = milliliters
        if self.size < self.quantity + self.milliliters:
            return

        self.quantity += self.milliliters

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(20)
cup.fill(10)
print(cup.status())
