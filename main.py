from random import randint, choice, seed
from core.room import Room3D
from core.maradona import Maradona
from core.utils import all_clean

from time import sleep


if __name__ == '__main__':

    # posição inicial do aspirador de pó
    mara_initial_state = (randint(3, 4), randint(0, 4))
    mx, my = mara_initial_state

    stage = input('Choose a stage by inserting any number:\n>\t')
    try:
        stage = int(stage)
    except ValueError:
        print('Invalid input. Setting stage to 0!')
        stage = 0

    # A fase (sujeira no tabuleiro) é definida pela semente
    seed(stage)

    # Cria uma sala e um aspirador de pó
    room = Room3D(1)
    mara = Maradona(mx, my, room)

    # exibe o mapa da sala
    print(f'Map of stage {stage}:')
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
            if not any(neighs.values()):
                search = mara.search()
                if search:
                    direction, distance = search
                    for _ in range(distance):
                        mara.__getattribute__(f'move_{direction}')()
                else:
                    direction = choice(list(neighs.keys()))
                    mara.__getattribute__(f'move_{direction}')()

            else:
                for direction, dirty in neighs.items():
                    if dirty:
                        mara.__getattribute__(f'move_{direction}')()

        print('Finished!')
        print('Steps taken:', mara.n_steps)
