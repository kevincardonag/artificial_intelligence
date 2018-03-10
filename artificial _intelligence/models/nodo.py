
class Node(object):
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
        self.node = self.__class__
        self.position_x = ""
        self.position_y = ""
        self.possible_movements = ""

    def __str__(self):
        """
        Autor: Kevin Cardona
        Fecha: 10 de marzo 2018
        Método para la representación de la clase nodo
        :return:
        """
        return "[{0}-{1}]".format(self.position_x, self.position_y)

    def move_up(self, position_x, position_y):
        """
        Autor: Kevin Cardona
        Fecha: febrero 17 2018
        movimiento arriba del ratón
        :param position_x: posición en x del ratón
        :param position_y: posición en y del ratón
        :return: moviente, nuevo valor de X e Y
        """
        move_x = position_x - 1
        move_y = position_y

        return move_x, move_y

    def move_left(self, position_x, position_y,):
        """
        Autor: Kevin Cardona
        Fecha: febrero 17 2018
        movimiento a la izquierda del ratón
        :param position_x: posición en x del ratón
        :param position_y: posición en y del ratón
        :return: moviente, nuevo valor de X e Y
        """
        move_x = position_x
        move_y = position_y - 1

        return move_x, move_y

    def move_down(self, position_x, position_y):
        """
        Autor: Kevin Cardona
        Fecha: febrero 17 2018
        movimiento abajo del ratón
        :param position_x: posición en x del ratón
        :param position_y: posición en y del ratón
        :return: moviente, nuevo valor de X e Y
        """
        move_x = position_x + 1
        move_y = position_y

        return move_x, move_y

    def move_right(self, position_x, position_y):
        """
        Autor: Kevin Cardona
        Fecha: febrero 17 2018
        movimiento a la derecha del ratón
        :param position_x: posición en x del ratón
        :param position_y: posición en y del ratón
        :return: moviente, nuevo valor de X e Y
        """
        move_x = position_x
        move_y = position_y + 1
        return move_x, move_y
