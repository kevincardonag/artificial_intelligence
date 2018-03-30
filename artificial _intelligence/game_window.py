import pygame
import sys
import time

from pygame.locals import *
from utils.read_file import read_file
from preferential_by_amplitude import preferential_by_amplitude
from constanst import ALGORITHM_TYPE
from global_variables import tree_development, build_tree
from models.nodo import Node
from utils.read_world import search_mario, build_tree_solution
from avara import algorithm_avara


class GameWindow():
    """
    Autor: Kevin Cardona
    Fecha: Mayo 3 2018
    Clase para crear la pantalla de juego
    """

    def __init__(self):
        """
        Autor: Kevin Cardona
        Fecha: Mayo 3 2018
        Se sobrescribe el init para crear las variable de la clase GameWindow
        """
        pygame.init()

        pygame.font.init()  # you have to call this at the start,
        self.my_font = pygame.font.SysFont('Comic Sans MS', 40)

        self.window = pygame.display.set_mode((500, 500))
        self.background_window = pygame.Color(255, 255, 255)
        pygame.display.set_caption("Mario")

        self.block = pygame.image.load("images/bloque.png")
        self.tortle = pygame.image.load("images/tortle.png")
        self.mario = pygame.image.load("images/mario.png")
        self.princses = pygame.image.load("images/princesa.png")
        self.mario_and_tortle = pygame.image.load("images/mario_and_tortle.png")
        self.mario_and_princes = pygame.image.load("images/mario_and_princes.png")
        self.block_white = pygame.image.load("images/bloque_blanco.png")

        self.world = read_file()
        self.run()

    def run(self):
        """
        Autor: Kevin Cardona
        Fecha: Mayo 3 2018
        Método para correr la ventana del juego y escuchar los eventos que suceden en ella.
        """
        self.window.fill(self.background_window)
        position_x_mario, position_y_mario = search_mario(self.world)

        self.node = Node()
        self.node.position_x = position_x_mario
        self.node.position_y = position_y_mario
        self.node.node = None
        self.node.world = self.world
        self.node.depth = 0

        if ALGORITHM_TYPE == 1:
            tree_development.append(self.node)

            while True:
                goal, node_move = preferential_by_amplitude(self.world, self.node)
                if not goal:
                    self.node = node_move
                else:
                    build_tree_solution(node_move)
                    break

        if ALGORITHM_TYPE == 2:

            while True:
                goal, node_move = algorithm_avara(self.world, self.node)
                if not goal:
                    self.node = node_move
                else:
                    build_tree_solution(node_move)
                    break
        # contador para recorrer la lista de la solución.
        count = 0

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

            if count < len(build_tree):
                current_node = build_tree[count]
                self.window.blit(self.mario, (current_node.position_y * 50, current_node.position_x * 50))
                count += 1
                time.sleep(1)
            else:
                text_winner = self.my_font.render('Ganaste', False, (231, 37, 18))
                self.window.blit(text_winner, (100, 100))
                text_depth = "Profundidad del arbol {0}".format(current_node.depth)
                text_render = self.my_font.render(text_depth, False, (231, 37, 18))
                self.window.blit(text_render, (100, 160))

            for i in range(len(self.world)):
                for j in range(len(self.world)):

                    if self.world[i][j] == '1':
                        self.window.blit(self.block, (j * 50, i * 50))

                    if self.world[i][j] == '4':
                        self.window.blit(self.tortle, (j * 50, i * 50))

                    if self.world[i][j] == '5':
                        self.window.blit(self.princses, (j * 50, i * 50))

                    if self.world[i][j] == '4' and i == current_node.position_x and j == current_node.position_y:
                        self.window.blit(self.mario_and_tortle, (j * 50, i * 50))

                    if self.world[i][j] == '5' and i == current_node.position_x and j == current_node.position_y:
                        self.window.blit(self.mario_and_princes, (j * 50, i * 50))


game_window = GameWindow()
