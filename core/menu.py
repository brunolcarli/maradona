from random import randint, choice, seed
from time import sleep
from core.room import Room3D
from core.maradona import Maradona
from core.utils import all_clean
from core.external_requests import GraphQLQuery, GraphQLMutation


def manual_game(mara):
    controller = {
        'up': mara.move_up,
        'down': mara.move_down,
        'left': mara.move_left,
        'right': mara.move_right,
    }

    while True:
        print('------------------')
        print('what you gonna do?')
        action = input(' '.join(i for i in controller.keys()) + ' exit\n').lower()

        if action == 'exit':
            break

        operation = controller.get(action)
        if operation:
            operation()
        else:
            print('>>\nInvalid Operation\\<<\n')

        mara.room.show()
        print('Steps taken: ', mara.n_steps)

        if all_clean(mara.room._map):
            print('Finished cleaning')
            break
        else:
            print('There are still dirty to clean.')

    return mara.n_steps


def autopilot_game(mara):
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
        search = mara.search()
        if search:
            direction, distance = search
            for _ in range(distance):
                mara.__getattribute__(f'move_{direction}')()
        else:
            direction = choice(list(neighs.keys()))
            mara.__getattribute__(f'move_{direction}')()

    print('Finished!')
    print('Steps taken:', mara.n_steps)
    return mara.n_steps


def view_top_10():
    print('Please wait, communicationg with the server ...')
    data = GraphQLQuery.get_top_10()
    data = data.get('data')

    if not data:
        print('No data found.')
        return

    print('\nShow top 10 rank:\n')
    print('------------------------------')
    print('Name            Steps     Date')
    print('------------------------------')
    for rank in data.get('maradonaScores', []):
        name = rank.get('playerName')
        steps = rank.get('steps')
        date_time = rank.get('gameDatetime')
        print(f'{name}\t{steps}\t{date_time}')
    print('------------------------------\n')


def save_score(username, steps):
    save = input('Save this game? s/n').lower()
    if save == 's':
        print('Please wait, communicating with server...')
        data = GraphQLMutation.register_score(username, steps)
        data = data.get('data')

        if not data:
            print('Sorry something went wrong')
            return


def menu():
    # posição inicial do aspirador de pó
    mara_initial_state = (randint(3, 4), randint(0, 4))
    mx, my = mara_initial_state

    stage = input('Choose a stage by inserting any number:\n>\t')
    try:
        stage = int(stage)
    except ValueError:
        print('Invalid input. Setting stage to 0!')
        stage = 0

    while True:
        username = input('Insert a username:\n>\t').strip()
        if username:
            break

    # A fase (sujeira no tabuleiro) é definida pela semente
    seed(stage)

    # Cria uma sala e um aspirador de pó
    room = Room3D(1)
    mara = Maradona(mx, my, room)

    # exibe o mapa da sala
    print(f'Map of stage {stage}:')
    mara.room.show()

    game_mode = input('Choose mode:\n1 - Manual\n2-Autopilot\n3-Scores\n>\t').lower()

    if game_mode == '1' or game_mode == 'manual':
        steps = manual_game(mara)
        save_score(username, steps)

    elif game_mode == '2' or game_mode == 'auto':
        steps = autopilot_game(mara)
        save_score(username, steps)

    elif game_mode == '3':
        view_top_10()
