from models.nodo import Node
from global_variables import tree_development, build_tree, nodes_visited
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

        tree_development.append(son_node)

    if possible_movements.get('block_down').get('move'):
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
    for i in tree_development:
        print(str(i))


    next_node = tree_development[0]

    return is_goal, world, next_node


def uniform_cost(world, node):
    """
        Autor: Carlos Estifen Almario Galindez
        Fecha: Marzo 28 2017
        Método que contiene la logica del algoritmo por costo uniforme
        :return:
    """
    father_node = node
    is_goal, field = check_goal(world, node)
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

        # pregunta si el nodo que se expandio ya fue expandido
        if not son_node.in_list(nodes_visited) and not son_node.in_list(tree_development):
            tree_development.append(son_node)

    # ordena la lista de los nodos meta por el costo menor y elimina el nodo que se va a expandir
    tree_development.sort(key=lambda node: node.cost)
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
    return field == '5', field


def build_tree_solution(node):
    """
    Autor: Kevin Cardona
    Fecha: Marzo 8 2018
    :return: retorna un array con la solución del arbol.
    """
    node_solution = node
    build_tree.insert(0, node_solution)
    cost = 0

    while True:
        if node_solution.node:
            node_solution = node_solution.node
            cost += node_solution.cost
            build_tree.insert(0, node_solution)
        else:
            break

    return build_tree, cost


