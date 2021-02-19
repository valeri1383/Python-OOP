class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guest = 0

    def from_stars(self):
        return Hotel(self)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room == room_number:
                room.free_room(room_number)

    def print_status(self):
        free = []
        taken = []
        for room in self.rooms:
            if room.is_taken:
                taken.append(room.number)
                self.guest += room.guests
            else:
                free.append(room.number)
        print(f'Hotel {self.name} stars Hotel has {self.guest} total guests')

        print(f'Free rooms: {", ".join([str(x) for x in free])}')

        print(f'Taken rooms: {", ".join([str(x) for x in taken])}')
