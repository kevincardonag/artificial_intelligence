from models.nodo import Node
from global_variables import tree_development, build_tree
from utils.read_world import read_matriz, check_goal


def preferential_by_amplitude(world, node):
    """
    Autor: Kevin Cardona
    Fecha: Marzo 6 2017
    Método que contiene la logica del algoritmo por amplitud
    :return:
    """
    father_node = node
    is_goal = check_goal(world, node)
    if is_goal:
        return is_goal, node

    possible_movements = read_matriz(world, node)

    father_node.possible_movements = possible_movements

    if possible_movements.get('block_up'):
        # se crea el nodo hijo
        son_node = Node()

        # se le asigna un padre al nodo hijo
        son_node.node = father_node

        # se hace el moviento hacia arriba del nodo hijo
        x, y = father_node.move_up(position_x=father_node.position_x, position_y=father_node.position_y)
        son_node.position_x = x
        son_node.position_y = y

        tree_development.append(son_node)

    if possible_movements.get('block_right'):
        # se crea el nodo hijo
        son_node = Node()

        # se le asigna un padre al nodo hijo
        son_node.node = father_node

        # se hace el moviento hacia arriba del nodo hijo
        x, y = father_node.move_right(position_x=father_node.position_x, position_y=father_node.position_y)
        son_node.position_x = x
        son_node.position_y = y

        tree_development.append(son_node)

    if possible_movements.get('block_left'):
        # se crea el nodo hijo
        son_node = Node()

        # se le asigna un padre al nodo hijo
        son_node.node = father_node

        # se hace el moviento hacia arriba del nodo hijo
        x, y = father_node.move_left(position_x=father_node.position_x, position_y=father_node.position_y)
        son_node.position_x = x
        son_node.position_y = y

        tree_development.append(son_node)

    if possible_movements.get('block_down'):
        # se crea el nodo hijo
        son_node = Node()

        # se le asigna un padre al nodo hijo
        son_node.node = father_node

        # se hace el moviento hacia arriba del nodo hijo
        x, y = father_node.move_down(position_x=father_node.position_x, position_y=father_node.position_y)
        son_node.position_x = x
        son_node.position_y = y

        tree_development.append(son_node)

    # elimine el primer nodo del array
    del tree_development[0]

    next_node = tree_development[0]
    next_node.depth = father_node.depth + 1
    return is_goal, next_node
