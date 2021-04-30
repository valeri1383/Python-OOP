class dictionary_iter:
    def __init__(self, my_dict):
        self.my_dict = my_dict
        self.my_dict_keys = list(self.my_dict.keys())
        self.length = len(self.my_dict)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.length:
            key = self.my_dict_keys[self.current_index]
            value = self.my_dict[key]
            self.current_index += 1
            return key, value
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
