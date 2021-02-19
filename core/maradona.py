

class Maradona:
    def __init__(self, pos_x, pos_y, room):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.room = room
        self.n_steps = 0
        self.setup()


    def setup(self):
        self.room[self.pos_x][self.pos_y] = str(self)

    def __repr__(self):
        return 'M'

    def validate_move(self, x, y):
        if x >= self.room.max_size_x or y >= self.room.max_size_y:
            return False

        if x < 0 or y < 0:
            return False

        return True

    def move_right(self):
        y = self.pos_y + 1

        if not self.validate_move(self.pos_x, y):
            print('Cant go that way!')
            return False

        self.room[self.pos_x][self.pos_y] = 0
        self.room[self.pos_x][y] = str(self)
        self.pos_y = y
        self.n_steps += 1

    def move_left(self):
        y = self.pos_y - 1

        if not self.validate_move(self.pos_x, y):
            print('Cant go that way!')
            return False

        self.room[self.pos_x][self.pos_y] = 0
        self.room[self.pos_x][y] = str(self)
        self.pos_y = y
        self.n_steps += 1

    def move_up(self):
        x = self.pos_x - 1

        if not self.validate_move(x, self.pos_y):
            print('Cant go that way!')
            return False

        self.room[self.pos_x][self.pos_y] = 0
        self.room[x][self.pos_y] = str(self)
        self.pos_x = x
        self.n_steps += 1

    def move_down(self):
        x = self.pos_x + 1

        if not self.validate_move(x, self.pos_y):
            print('Cant go that way!')
            return False

        self.room[self.pos_x][self.pos_y] = 0
        self.room[x][self.pos_y] = str(self)
        self.pos_x = x
        self.n_steps += 1
