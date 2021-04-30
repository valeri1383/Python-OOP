def get_primes(my_list):
    for number in my_list:
        new_list = []
        is_prime = True

        for x in range(2, number):
            if number % x == 0:
                is_prime = False
                break
        if is_prime and number > 1:
            yield number
            new_list.append(number)


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
