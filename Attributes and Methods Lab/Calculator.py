class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result = result * x
        return result

    @staticmethod
    def divide(*args):
        return args[0] / args[1]

    @staticmethod
    def subtract(*args):
        result = args[0] - sum(args[1:])
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

