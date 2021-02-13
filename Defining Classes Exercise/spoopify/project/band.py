
class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        if album.published:
            return "Album has been published. It cannot be removed."
        if album_name not in self.albums:
            return f"Album {album_name} is not found."
        self.albums.remove(album_name)
        return f"Album {album_name} has been removed."

    def details(self):
        data = f'Band {self.name}\n'
        for a in self.albums:
            data += f'{a.details()}\n'
        return data
