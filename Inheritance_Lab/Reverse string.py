def reverse_text(text):
    counter = len(text) - 1
    while counter >= 0:
        yield text[counter]
        counter -= 1


for char in reverse_text("step"):
    print(char, end='')
