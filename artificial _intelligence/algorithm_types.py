from models.nodo import Node
from global_variables import tree_development, build_tree
from utils.read_world import read_matriz


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
        return is_goal, world, node

    possible_movements = read_matriz(world, node)

    father_node.test = possible_movements

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

    return is_goal, world, next_node


def check_goal(world, node):
    """
    Autor: Kevin Cardona
    Fecha: Marzo 6 2018
    Método que comprueba si el nodo es meta
    :param world: matriz que reprenta el mundo de mario
    :param node: nodo (posición de mario)
    :return: bool
    """
    field = world[node.position_x][node.position_y]
    return field == '5'


def build_tree_solution(node):
    """
    Autor: Kevin Cardona
    Fecha: Marzo 8 2018
    :return: retorna un array con la solución del arbol.
    """
    node_solution = node
    build_tree.insert(0, node_solution)

    while True:
        if node_solution.node:
            node_solution = node_solution.node
            build_tree.insert(0, node_solution)
        else:
            break
