def even_parameters(func):
    def wrapper(*args):
        if all(isinstance(x, int) for x in args):
            even = True
            for x in args:
                if x % 2 != 0:
                    even = False
                    break
            if even:
                result = func(*args)
                return result
            return 'Please use only even numbers!'
        return 'Please use only even numbers!'
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
print()

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

