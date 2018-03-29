def read_matriz(world, node):
    """
    Autor: Kevin Cardona
    Fecha: febrero 17 2018
    método que analiza la world para saber que hay alrededor del ratón
    :param world: world inicial del juego
    :param nodo: posición del mario en x
    :return: resumen de los posibles moviemientos que puede hacer mario
    """
    position_mario_x = node.position_x
    position_mario_y = node.position_y

    # preguntar arriba
    if (position_mario_x - 1) < 0:
        block_up = {'move':False,'cost':0}
    else:
        block_up = world[position_mario_x - 1][position_mario_y].strip()
        block_up = get_field(field=block_up)

    # preguntar derecha
    try:
        block_right = world[position_mario_x][position_mario_y + 1].strip()

        block_right = get_field(field=block_right)
    except Exception:
        block_right = {'move':False,'cost':0}

    # preguntar izq
    if (position_mario_y - 1) < 0:
        block_left = {'move':False,'cost':0}
    else:
        block_left = world[position_mario_x][position_mario_y - 1].strip()
        block_left = get_field(field=block_left)

    # preguntar abajo
    try:
        block_down = world[position_mario_x + 1][position_mario_y].strip()

        block_down = get_field(field=block_down)
    except Exception:
        block_down = {'move':False,'cost':0}

    possible_movements = {
        'block_up': block_up,
        'block_right': block_right,
        'block_left': block_left,
        'block_down': block_down
    }



    return possible_movements


def get_field(field):
    """
    Autor: Kevin Cardona
    Fecha: febrero 17 2018
    método auxiliar para analizar que hay dentro de cada casilla
    :param field: casilla de la matriz
    :return: bool
    """
    if field == '1':
        field = {'move':False,'cost': 0}
    elif field == '0':
        field = {'move': True, 'cost': 1}
    elif field == '3':
        field = {'move': True, 'cost': 1}
    elif field == '4':
        field = {'move': True, 'cost': 10}

    elif field == '2':
        field = {'move': True, 'cost': 1}

    elif field == '5':
        field = {'move': True, 'cost': 1}

    return field



