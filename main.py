from random import randint, choice
from core.room import Room3D
from core.maradona import Maradona
from core.utils import all_clean

from time import sleep


if __name__ == '__main__':

    mara_initial_state = (randint(3, 4), randint(0, 4))
    mx, my = mara_initial_state

    room = Room3D(1)
    mara = Maradona(mx, my, room)
    mara.room.show()

    controller = {
        'up': mara.move_up,
        'down': mara.move_down,
        'left': mara.move_left,
        'right': mara.move_right,
    }

    game_mode = input('Choose mode:\n1 - Manual\n2 - Autopilot\n>\t').lower()

    if game_mode == '1' or game_mode == 'manual':
        while True:
            print('what you gonna do?')
            action = input(' '.join(i for i in controller.keys()) + ' exit\n').lower()

            if action == 'exit':
                break

            operation = controller.get(action)
            if operation:
                operation()
            else:
                print('Invalid')

            mara.room.show()
            print(mara.check_neighbors())
            print('Steps taken: ', mara.n_steps)

            if all_clean(mara.room._map):
                print('Finished cleaning')
                break
            else:
                print('There are still dirty to clean.')

    elif game_mode == '2' or game_mode == 'auto':
        print('Cleaning the dirty ...')
        while True:
            sleep(.666)
            mara.room.show()
            # se a sala estiver limpa, pare.
            if all_clean(mara.room._map):
                break
            
            # verifica os vizinhos
            neighs = mara.check_neighbors()

            # decide a direção do movimento
            if 1 not in neighs.values():
                possible = [k for k, v in neighs.items() if v is not None]
                direction = choice(possible)
                mara.__getattribute__(f'move_{direction}')()

            else:
                for direction, dirty in neighs.items():
                    if dirty:
                        mara.__getattribute__(f'move_{direction}')()

        print('Finished!')
        print('Steps taken:', mara.n_steps)
