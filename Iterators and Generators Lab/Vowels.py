class vowels:
    def __init__(self, text):
        self.text = text
        self.current_idx = 0
        self.vowels = ['a', 'e', 'u', 'o', 'y', 'i']

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx < len(self.text):
            temp = self.current_idx
            self.current_idx += 1
            if self.text[temp].lower() in self.vowels:
                return self.text[temp]
            else:
                return self.__next__()
        raise StopIteration()



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
