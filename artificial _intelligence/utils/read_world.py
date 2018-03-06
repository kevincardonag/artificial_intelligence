def read_matriz(matriz, position_mario_x, position_mario_y):
    """
    Autor: Kevin Cardona
    Fecha: febrero 17 2018
    método que analiza la matriz para saber que hay alrededor del ratón
    :param matriz: matriz inicial del juego
    :param position_mario_x: posición del mario en x
    :param position_mario_y: posición del mario en y
    :return: la nueva posición en X e Y, y un bool indicando si encontro el queso o No.
    """
    possible_movements = []

    # preguntar derecha
    try:
        block_rigth = matriz[position_mario_x][position_mario_y + 1].strip()

    except Exception:
        block_rigth = False

    # preguntar izq
    if (position_mouse_y - 1) < 0:
        block_left = False
    else:
        block_left = matriz[position_mouse_x][position_mouse_y - 1].strip()

        if block_left == 'Q':
            return position_mouse_x, position_mouse_y, True

        block_left = self.get_field(block_left)

    # preguntar arriba
    if (position_mouse_x - 1) < 0:
        block_up = False
    else:
        block_up = matriz[position_mouse_x - 1][position_mouse_y].strip()
        if block_up == 'Q':
            return position_mouse_x, position_mouse_y, True
        block_up = self.get_field(block_up)

    # preguntar abajo
    try:
        block_down = matriz[position_mouse_x + 1][position_mouse_y].strip()
        if block_down == 'Q':
            return position_mouse_x, position_mouse_y, True
        block_down = self.get_field(block_down)

    except Exception:
        block_down = False

    fields = {
        'block_rigth': block_rigth,
        'block_left': block_left,
        'block_up': block_up,
        'block_down': block_down
    }

    return step(position_mouse_x, position_mouse_y, **fields)


def step(position_x, position_y, **kwargs):
    """
    Autor: Kevin Cardona
    Fecha: febrero 17 2018
    método que tiene las condiciones para hacer un paso.
    :param position_x: posición en x del ratón
    :param position_y: posición en y del ratón
    :param kwargs: kwargs de la función
    :return: moviente, nuevo valor de X e Y, Y UN BOOL INDICANDO SI ENCONTRO EL QUESO
    """
    left = kwargs['block_left']
    up = kwargs['block_up']
    rigth = kwargs['block_rigth']
    down = kwargs['block_down']

    if left and up and rigth and down:
        return move_up(position_x, position_y)

    if left and up and rigth and not down:
        return self.move_up(position_x, position_y)

    if left and up and not rigth and down:
        return self.move_up(position_x, position_y,)

    if left and up and not rigth and not down:
        return self.move_left(position_x, position_y,)

    if left and not up and rigth and down:
        return self.move_left(position_x, position_y,)

    if left and not up and rigth and not down:
        return self.move_rigth(position_x, position_y,)

    if left and not up and not rigth and down:
        return self.move_left(position_x, position_y,)

    if left and not up and not rigth and not down:
        return self.move_left(position_x, position_y,)

    if not left and up and rigth and down:
        return self.move_up(position_x, position_y,)

    if not left and up and rigth and not down:
        return self.move_rigth(position_x, position_y,)

    if not left and up and not rigth and down:
        return self.move_down(position_x, position_y,)

    if not left and up and not rigth and down:
        return self.move_up(position_x, position_y,)

    if not left and not up and rigth and down:
        return self.move_rigth(position_x, position_y,)

    if not left and not up and rigth and not down:
        return self.move_rigth(position_x, position_y,)

    if not left and not up and not rigth and down:
        return self.move_down(position_x, position_y,)


def get_field(self, field):
    """
    Autor: Kevin Cardona
    Fecha: febrero 17 2018
    método auxiliar para analizar que hay dentro de cada casilla
    :param field: casilla de la matriz
    :return: bool
    """
    if field == '1':
        field = False
    elif field == '0':
        field = True
    elif field == '3':
        field = True
    elif field == '4':
        field = True

    return field