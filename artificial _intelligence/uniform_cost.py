from models.nodo import Node
from utils.read_world import read_matriz, check_goal
from global_variables import tree_development, build_tree, nodes_visited


def uniform_cost(world, node):
    """
        Autor: Carlos Estifen Almario Galindez
        Fecha: Marzo 28 2017
        Método que contiene la logica del algoritmo por costo uniforme
        :return:
    """
    father_node = node
    is_goal = check_goal(world, node)
    if is_goal:
        return is_goal, node

    possible_movements = read_matriz(world, node)
    father_node.possible_movements = possible_movements

    nodes_visited.append(father_node)

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
        # si el nodo esta parado es una flor.

        if possible_movements.get('block_down').get('flower'):
            son_node.flower = True
            nodes_visited.clear()

        if father_node.flower:
            son_node.flower = True
            son_node.cost = father_node.cost + 1
        else:
            son_node.cost = father_node.cost + possible_movements.get('block_down').get('cost')

        # pregunta si el nodo que se expandio ya fue expandido

        if not son_node.in_list(nodes_visited) and not son_node.in_list(tree_development):
            tree_development.append(son_node)

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
        # si el nodo esta parado es una flor.
        if possible_movements.get('block_up').get('flower') and not father_node.flower:
            son_node.flower = True
            nodes_visited.clear()

        if father_node.flower:
            son_node.flower = True
            son_node.cost = father_node.cost + 1
        else:
            son_node.cost = father_node.cost + possible_movements.get('block_up').get('cost')

        # pregunta si el nodo que se expandio ya fue expandido
        if not son_node.in_list(nodes_visited) and not son_node.in_list(tree_development):
            tree_development.append(son_node)

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

        # si el nodo esta parado es una flor.
        if possible_movements.get('block_right').get('flower'):
            son_node.flower = True
            nodes_visited.clear()

        if father_node.flower:
            son_node.flower = True
            son_node.cost = father_node.cost + 1
        else:
            son_node.cost = father_node.cost + possible_movements.get('block_right').get('cost')

        # pregunta si el nodo que se expandio ya fue expandido
        if not son_node.in_list(nodes_visited) and not son_node.in_list(tree_development):
            tree_development.append(son_node)

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

        # si el nodo esta parado es una flor.
        if possible_movements.get('block_left').get('flower'):
            son_node.flower = True

        if father_node.flower:
            son_node.flower = True
            son_node.cost = father_node.cost + 1
        else:
            son_node.cost = father_node.cost + possible_movements.get('block_left').get('cost')
        # pregunta si el nodo que se expandio ya fue expandido

        if not son_node.in_list(nodes_visited) and not son_node.in_list(tree_development):
            tree_development.append(son_node)

    # ordena la lista de los nodos meta por el costo menor y elimina el nodo que se va a expandir
    tree_development.sort(key=lambda node: node.cost)
    del tree_development[0]
    next_node = tree_development[0]
    # next_node.depth = father_node.depth + 1

    return is_goal, next_node

