
def read_file():
    """
    Autor: Carlos Almario
    Fecha: febrero 27 2018
    Archivo read_file.py, Contiene una función para leer un archivo txt e insertarlos en una matriz
    :return:
    """
    world = []

    with open('matriz.txt') as matriz:
        """ Crea la matriz con base a los datos del archivo txt """
        [world.append(line_matriz.strip().split(" ")) for line_matriz in matriz]

    return world
