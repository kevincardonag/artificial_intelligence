from utils.read_world import check_goal, read_matriz
import numpy as np
from models.nodo import Node
from global_variables import tree_development, build_tree


def algorithm_avara(world, node):
    """
    Autor: Kevin Cardona
    Fecha: febrero 17 2018
    método que analiza el mundo para saber que hay alrededor del ratón
    :param world: mundo inicial del juego
    :param node: posición del mario en x
    :return: resumen de los posibles moviemientos que puede hacer mario
    """
    father_node = node
    is_goal = check_goal(world, father_node)
    if is_goal:
        return is_goal, node

    possible_movements = read_matriz(world, father_node)

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

        # se agrega el valor de la heuristica al Nodo
        heuristic = calculate_heuristic(son_node)
        son_node.heuristic = heuristic
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

        # se agrega el valor de la heuristica al Nodo
        heuristic = calculate_heuristic(son_node)
        son_node.heuristic = heuristic
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

        # se agrega el valor de la heuristica al Nodo
        heuristic = calculate_heuristic(son_node)
        son_node.heuristic = heuristic
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

        # se agrega el valor de la heuristica al Nodo
        heuristic = calculate_heuristic(son_node)
        son_node.heuristic = heuristic
        tree_development.append(son_node)

    organized = sorted(tree_development, key=lambda node: node.heuristic)
    next_node = organized[0]

    index = tree_development.index(next_node)
    del tree_development[index]

    next_node.depth = father_node.depth + 1
    return is_goal, next_node


def calculate_heuristic(son_node):
    """
    Kevin Cardona
    Método para calcular la heuristica
    :param son_node: Instancia de la clase nodo
    :return: integer
    """
    position_x = son_node.position_x - 4
    position_y = son_node.position_y - 9
    difference = np.array([position_x, position_y])
    heuristic = np.linalg.norm(difference)
    return heuristic