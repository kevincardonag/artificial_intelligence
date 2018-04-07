from models.nodo import Node
from utils.read_world import read_matriz, check_goal
from global_variables import tree_development, build_tree, nodes_visited
from  avara import calculate_heuristic


def a_star(world, node):
    """
        Autor: Carlos Estifen Almario Galindez
        Fecha: Marzo 28 2017
        Método que contiene la logica del algoritmo por costo uniforme
        :return:
    """
    father_node = node
    is_goal = check_goal(world, node)
    if is_goal:
        return is_goal, world, node

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
        son_node.cost = father_node.cost + possible_movements.get('block_down').get('cost')
        son_node.heuristic = calculate_heuristic(son_node)
        son_node.f = son_node.cost + son_node.heuristic

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

        son_node.cost = father_node.cost + possible_movements.get('block_up').get('cost')
        son_node.heuristic = calculate_heuristic(son_node)
        son_node.f = son_node.cost + son_node.heuristic

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

        son_node.cost = father_node.cost + possible_movements.get('block_right').get('cost')
        son_node.heuristic = calculate_heuristic(son_node)
        son_node.f = son_node.cost + son_node.heuristic

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

        son_node.cost = father_node.cost + possible_movements.get('block_left').get('cost')
        son_node.heuristic = calculate_heuristic(son_node)
        son_node.f = son_node.cost + son_node.heuristic

        # pregunta si el nodo que se expandio ya fue expandido
        if not son_node.in_list(nodes_visited) and not son_node.in_list(tree_development):
            tree_development.append(son_node)

    # ordena la lista de los nodos meta por el costo menor y elimina el nodo que se va a expandir
    tree_development.sort(key=lambda node: node.f)
    del tree_development[0]
    next_node = tree_development[0]

    return is_goal, world, next_node
