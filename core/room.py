from random import randint


class Room3D:
    def __init__(self, name, max_size_x=5, max_size_y=5):
        self.name = name
        self.max_size_x = max_size_x
        self.max_size_y = max_size_y
        self._map = self.build()

    def build(self):
        return [[randint(0, 1) for _ in range(self.max_size_x)] for _ in range(self.max_size_y)]

    def __getitem__(self, index):
        return self._map.__getitem__(index)

    def __delitem__(self, index):
        self._map.__delitem__(index )

    def insert(self, index, value):
        self._map.insert(index, value)

    def __setitem__(self, index, value):
        self._map.__setitem__(index, value)

    def __getitem__(self, index):
        return self._map.__getitem__(index)

    def show(self):
        print('[')
        for row in self._map:
            line = ' '.join(str(i) for i in row)
            print(f'\t[ {line} ]')
        print(']')

