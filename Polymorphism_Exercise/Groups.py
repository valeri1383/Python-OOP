class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)


class Group:
    def __init__(self, name, people=[]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join([x.name + ' ' + x.surname for x in self.people])}"

    def __getitem__(self, idx):
        return f'Person {idx}: {self.people[idx].name} {self.people[idx].surname}'

    def __getitem__(self, name):
        return f'Person {name}: {self.people[name].name} {self.people[name].surname}'

    def __add__(self, other):
        group = Group(name=f'{self.name} {other.name}')
        group.people.extend(self.people + other.people)
        return group


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
