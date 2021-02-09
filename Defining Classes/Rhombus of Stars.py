
def first_half(n):
    for i in range(n + 1):
        print(f"{' ' * (n - i)}{'* ' * i}")

def second_half(n):
    for j in range(1, n):
        print(f"{' ' * j}{'* ' * (n - j)}")

def rhombus_of_stars(n):
    first_half(n)
    second_half(n)


rhombus_of_stars(int(input()))