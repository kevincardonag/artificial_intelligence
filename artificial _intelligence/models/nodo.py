
class Nodo(object):
    """
    Autor: carlos Almario
    Fecha: febrero 27 2018
    Clase Nodo
    """

    def __init__(self):
        """
        Autor: Kevin Cardona
        Fecha: Marzo 6 2018
        Se sobrescribe el init para crear las variables de la clase nodo.
        """
        self.nodo = self.__class__
        self.position_x = ""
        self.position_y = ""
        # self.possible_movements = []

    def move_up(self, position_x, position_y):
        """
        Autor: Kevin Cardona
        Fecha: febrero 17 2018
        movimiento arriba del ratón
        :param position_x: posición en x del ratón
        :param position_y: posición en y del ratón
        :return: moviente, nuevo valor de X e Y, Y UN BOOL INDICANDO SI ENCONTRO EL QUESO
        """
        move_x = position_x - 1
        move_y = position_y

        return move_x, move_y, False

    def move_left(self, position_x, position_y,):
        """
        Autor: Kevin Cardona
        Fecha: febrero 17 2018
        movimiento a la izquierda del ratón
        :param position_x: posición en x del ratón
        :param position_y: posición en y del ratón
        :return: moviente, nuevo valor de X e Y, Y UN BOOL INDICANDO SI ENCONTRO EL QUESO
        """
        move_x = position_x
        move_y = position_y - 1

        return move_x, move_y, False

    def move_down(self, position_x, position_y):
        """
        Autor: Kevin Cardona
        Fecha: febrero 17 2018
        movimiento abajo del ratón
        :param position_x: posición en x del ratón
        :param position_y: posición en y del ratón
        :return: moviente, nuevo valor de X e Y, Y UN BOOL INDICANDO SI ENCONTRO EL QUESO
        """
        move_x = position_x + 1
        move_y = position_y

        return move_x, move_y, False

    def move_rigth(self, position_x, position_y):
        """
        Autor: Kevin Cardona
        Fecha: febrero 17 2018
        movimiento a la derecha del ratón
        :param position_x: posición en x del ratón
        :param position_y: posición en y del ratón
        :return: moviente, nuevo valor de X e Y, Y UN BOOL INDICANDO SI ENCONTRO EL QUESO
        """
        move_x = position_x
        move_y = position_y + 1
        return move_x, move_y, False