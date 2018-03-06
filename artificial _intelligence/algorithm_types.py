from models.nodo import Nodo
from globlal_variables import tree_development, build_tree
from utils.read_world import read_matriz


def preferential_by_amplitude(world, position_x_mario, position_y_mario):
    """
    Autor: Kevin Cardona
    Fecha: Marzo 6 2017
    Método que contiene la logica del algoritmo por amplitud
    :return:
    """
    nodo = Nodo()
    nodo.position_x = position_x_mario
    nodo.position_y = position_y_mario
    nodo.nodo = None

    tree_development.append(nodo)
    read_matriz(world, position_x_mario, position_y_mario)
