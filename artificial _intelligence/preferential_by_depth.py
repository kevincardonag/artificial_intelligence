from models.nodo import Node
from global_variables import tree_development, build_tree
from utils.read_world import read_matriz, check_goal
from global_variables import tree_development, build_tree


def preferential_by_depth(world, node):
    """
    Autor: Kevin Cardona
    Fecha: Abril 4 2017
    Método que contiene la logica del algoritmo por profundidad evitando ciclos
    :return:
    """
    father_node = node
    is_goal = check_goal(world, node)
    if is_goal:
        return is_goal, node

    possible_movements = read_matriz(world, node)
    father_node.possible_movements = possible_movements

    if possible_movements.get('block_up').get('move'):

        # se crea el nodo hijo
        son_node = Node()

        # se le asigna un padre al nodo hijo
        son_node.node = father_node

        # se hace el moviento hacia arriba del nodo hijo
        x, y = father_node.move_up(position_x=father_node.position_x, position_y=father_node.position_y)
        son_node.position_x = x
        son_node.position_y = y

        son_node.depth = father_node.depth + 1

        # evitar devolverse
        to_be_return = next_position_is_to_be_return(son_node)
        if not to_be_return:

            # evitar el ciclo
            node_found = search_node_in_tree(son_node)
            if not node_found:

                # si el nodo esta parado es una flor.
                if possible_movements.get('block_up').get('flower'):
                    son_node.flower = True

                if father_node.flower:
                    son_node.flower = True
                    son_node.cost = father_node.cost + 1
                else:
                    son_node.cost = father_node.cost + possible_movements.get('block_up').get('cost')

                tree_development.insert(0, son_node)

    if possible_movements.get('block_right').get('move'):
        # se crea el nodo hijo
        son_node = Node()

        # se le asigna un padre al nodo hijo
        son_node.node = father_node

        # se hace el moviento hacia arriba del nodo hijo
        x, y = father_node.move_right(position_x=father_node.position_x, position_y=father_node.position_y)
        son_node.position_x = x
        son_node.position_y = y
        son_node.depth = father_node.depth + 1

        # evitar devolverse
        to_be_return = next_position_is_to_be_return(son_node)
        if not to_be_return:

            # evitar el ciclo
            node_found = search_node_in_tree(son_node)
            if not node_found:

                # si el nodo esta parado es una flor.
                if possible_movements.get('block_right').get('flower'):
                    son_node.flower = True

                if father_node.flower:
                    son_node.flower = True
                    son_node.cost = father_node.cost + 1
                else:
                    son_node.cost = father_node.cost + possible_movements.get('block_right').get('cost')

                tree_development.insert(0, son_node)

    if possible_movements.get('block_left').get('move'):
        # se crea el nodo hijo
        son_node = Node()

        # se le asigna un padre al nodo hijo
        son_node.node = father_node

        # se hace el moviento hacia arriba del nodo hijo
        x, y = father_node.move_left(position_x=father_node.position_x, position_y=father_node.position_y)
        son_node.position_x = x
        son_node.position_y = y
        son_node.depth = father_node.depth + 1

        # evitar devolverse
        to_be_return = next_position_is_to_be_return(son_node)
        if not to_be_return:

            # evitar el ciclo
            node_found = search_node_in_tree(son_node)
            if not node_found:

                # si el nodo esta parado es una flor.
                if possible_movements.get('block_left').get('flower'):
                    son_node.flower = True

                if father_node.flower:
                    son_node.flower = True
                    son_node.cost = father_node.cost + 1
                else:
                    son_node.cost = father_node.cost + possible_movements.get('block_left').get('cost')

                tree_development.insert(0, son_node)

    if possible_movements.get('block_down').get('move'):
        # se crea el nodo hijo
        son_node = Node()

        # se le asigna un padre al nodo hijo
        son_node.node = father_node

        # se hace el moviento hacia arriba del nodo hijo
        x, y = father_node.move_down(position_x=father_node.position_x, position_y=father_node.position_y)
        son_node.position_x = x
        son_node.position_y = y
        son_node.depth = father_node.depth + 1

        # evitar devolverse
        to_be_return = next_position_is_to_be_return(son_node)
        if not to_be_return:

            # evitar el ciclo
            node_found = search_node_in_tree(son_node)
            if not node_found:

                # si el nodo esta parado es una flor.
                if possible_movements.get('block_down').get('flower'):
                    son_node.flower = True

                if father_node.flower:
                    son_node.flower = True
                    son_node.cost = father_node.cost + 1
                else:
                    son_node.cost = father_node.cost + possible_movements.get('block_down').get('cost')

                tree_development.insert(0, son_node)

    # elimine el nodo padre del array
    index_father_node = tree_development.index(father_node)
    del tree_development[index_father_node]

    next_node = tree_development[0]
    return is_goal, next_node


def search_node_in_tree(node):
    """
    Autor: Kevin Cardona
    Fecha: Abril 4 2018
    Método que me indica si el nodo ya existe en el arbol
    :return: bool
    """
    found = False

    while True:
        try:
            if node.position_x == node.node.position_x and node.position_y == node.node.position_y:
                found = True
                break
            else:
                node = node.node
        except AttributeError:
            break
    return found


def next_position_is_to_be_return(node):
    """
    Autor: Kevin Cardona
    Fecha: abril 4 2018
    Método que me indica si creo el nodo seria devolverse
    :param node: instancia de la clase node
    :return: bool
    """
    to_be_return = False

    try:
        first_condition = node.position_x == node.node.node.position_x
        second_condition = node.position_y == node.node.node.position_y

        if first_condition and second_condition:
            to_be_return = True
    except AttributeError:
        to_be_return = False

    return to_be_return
