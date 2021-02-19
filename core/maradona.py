"""
Contém elementos do aspirador.
"""

class Maradona:
    """
    Maradona é o aspirador de pó.
    Ele deve andar por uma sala de dimensão XY limpando a poeira da sala.
    Cada passo que maradona der dentro da sala deverá ser contado.
    Maradona deverá se mover para cima, baixo, direita e esquerda (ou Norte, Sul,
    Leste e Oeste se preferir).
    Maradona não pode ir além dos limites (paredes) da sala.
    Mas maradona poderá ir para outra sala se necessário.
    """
    def __init__(self, pos_x, pos_y, room):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.room = room
        self.n_steps = 0

        self.visited = []
        self.setup()

    def setup(self):
        """
        Iinicializa a localização do maradona na sala.
        """
        self.room[self.pos_x][self.pos_y] = str(self)

    def __repr__(self):
        """
        Maradona é representado pela letra M no tabuleiro.
        """
        return 'M'

    def record(self, coord):
        """
        Memoriza coordenadas ja visitadas.
        """
        self.visited.append(coord)

    def validate_move(self, x, y):
        """
        Verifica se o movimento a ser realizado é válido.
        """
        if x >= self.room.max_size_x or y >= self.room.max_size_y:
            return False

        if x < 0 or y < 0:
            return False

        return True

    def move_right(self, step=1):
        """
        Movimenta maradona para a direita (Leste) uma quantidade de passos.
        Por padrão, maradona dará um passo.
        """
        y = self.pos_y + step

        if not self.validate_move(self.pos_x, y):
            print('Cant go that way!')
            return False

        self.room[self.pos_x][self.pos_y] = 0
        self.record((self.pos_x, self.pos_y))
        self.room[self.pos_x][y] = str(self)
        self.pos_y = y
        self.n_steps += step

    def move_left(self, step=1):
        """
        Movimenta maradona para a esquerda (Oeste) uma quantidade de passos.
        Por padrão, maradona dará um passo.
        """
        y = self.pos_y - step

        if not self.validate_move(self.pos_x, y):
            print('Cant go that way!')
            return False

        self.room[self.pos_x][self.pos_y] = 0
        self.record((self.pos_x, self.pos_y))
        self.room[self.pos_x][y] = str(self)
        self.pos_y = y
        self.n_steps += step

    def move_up(self, step=1):
        """
        Movimenta maradona para a cima (Norte) uma quantidade de passos.
        Por padrão, maradona dará um passo.
        """
        x = self.pos_x - step

        if not self.validate_move(x, self.pos_y):
            print('Cant go that way!')
            return False

        self.room[self.pos_x][self.pos_y] = 0
        self.record((self.pos_x, self.pos_y))
        self.room[x][self.pos_y] = str(self)
        self.pos_x = x
        self.n_steps += step

    def move_down(self, step=1):
        """
        Movimenta maradona para a baixo (Sul) uma quantidade de passos.
        Por padrão, maradona dará um passo.
        """
        x = self.pos_x + step

        if not self.validate_move(x, self.pos_y):
            print('Cant go that way!')
            return False

        self.room[self.pos_x][self.pos_y] = 0
        self.record((self.pos_x, self.pos_y))
        self.room[x][self.pos_y] = str(self)
        self.pos_x = x
        self.n_steps += step

    def check_neighbors(self, n=1):
        """
        Verifica o conteúdo dos vizinhos, isto é se tem sujeira ou se é uma parede (limite máximo).
        Retorna um dicionário contendo o valor dos vizinhos de cada direção.
        1 se houver poeira.
        0 se estiver limpo.
        None se for o limite.
        """
        up_n = self.room[self.pos_x-n][self.pos_y] if self.validate_move(self.pos_x-n, self.pos_y) else None
        down_n = self.room[self.pos_x+n][self.pos_y] if self.validate_move(self.pos_x+n, self.pos_y) else None
        left_n = self.room[self.pos_x][self.pos_y-n] if self.validate_move(self.pos_x, self.pos_y-n) else None
        right_n = self.room[self.pos_x][self.pos_y+n] if self.validate_move(self.pos_x, self.pos_y+n) else None

        return {'up': up_n, 'down': down_n, 'left': left_n, 'right': right_n}

    def search(self):
        print('searching elements...')

        for i in range(1, len(self.room._map)+1):
            neighs = self.check_neighbors(n=i)
            if any(neighs.values()):
                for k, v in neighs.items():
                    if v:
                        return (k, i)
