import pygame
import sys
import time

from pygame.locals import *
from utils.read_file import read_file
from preferential_by_amplitude import preferential_by_amplitude
from uniform_cost import uniform_cost
from constanst import ALGORITHM_TYPE, HIGH, WIDTH
from global_variables import tree_development
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

        self.window = pygame.display.set_mode((WIDTH, HIGH))
        self.background_window = pygame.Color(255, 255, 255)
        self.background_rect = pygame.Color(160, 82, 45)
        self.cost = ""
        self.number_nodes = ""

        self.background_rect_two = pygame.Color(0, 0, 0)

        self.font = pygame.font.Font("images/SuperMario256.ttf", 20)
        self.font_two = pygame.font.SysFont("Arial", 10)

        self.texto = self.font.render("Algoritmos", 0, (255, 195, 0))

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

        # algoritmo preferente por amplitud
        if ALGORITHM_TYPE == 1:
            tree_development.append(self.node)

            expanded_nodes = 0
            while True:
                goal, node_move = preferential_by_amplitude(self.world, self.node)
                expanded_nodes += 1
                if not goal:
                    self.node = node_move
                else:
                    build_tree, cost = build_tree_solution(node_move)
                    break

        # algoritmo por costo uniforme
        if ALGORITHM_TYPE == 2:
            tree_development.append(self.node)

            while True:
                goal, node_move = uniform_cost(self.world, self.node)
                if not goal:
                    self.node = node_move
                else:
                    build_tree, cost = build_tree_solution(node_move)
                    break

        # algoritmo avara
        if ALGORITHM_TYPE == 4:

            while True:
                goal, node_move = algorithm_avara(self.world, self.node)
                if not goal:
                    self.node = node_move
                else:
                    build_tree, cost = build_tree_solution(node_move)
                    break

        # contador para recorrer la lista de la solución.
        count = 0

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

            for i in range(len(self.world)):
                for j in range(len(self.world)):

                    if self.world[i][j] == '1':
                        self.window.blit(self.block, (j * 50, i * 50))

                    if self.world[i][j] == '4':
                        self.window.blit(self.tortle, (j * 50, i * 50))

                    if self.world[i][j] == '5':
                        self.window.blit(self.princses, (j * 50, i * 50))

            if count < len(build_tree):
                self.window.blit(self.mario, (build_tree[count].position_y * 50,  build_tree[count].position_x * 50))
                count += 1
                time.sleep(0.5)

    def create_text(self, text, a, b, c):
        """
            Autor: Carlos Almario
            Fecha: Marzo 28 2018
            Método para crear el texto que va se va a mostrar en la pantalla del proyecto
            :return:
        """

        return self.font_two.render(text, 0, (a, b, c))

game_window = GameWindow()
