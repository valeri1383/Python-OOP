def even_numbers(function):
    def wrapper(numbers):
        numbers = function(numbers)
        result = [x for x in numbers if x % 2 == 0]
        return result
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))
