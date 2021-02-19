from core.room import Room3D
from core.maradona import Maradona


if __name__ == '__main__':
    r = Room3D(1)
    m = Maradona(2, 2, r)
    m.room.show()

    while True:
        system = {
            'up': m.move_up,
            'down': m.move_down,
            'left': m.move_left,
            'right': m.move_right,
        }


        print('what you gonna do?')
        action = input(str(system.keys()) + 'exit\n').lower()

        if action == 'exit':
            break


        operation = system.get(action)
        if operation:
            operation()
        else:
            print('Invalid')

        m.room.show()
        print('Steps taken: ', m.n_steps)
