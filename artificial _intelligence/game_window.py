import pygame
import sys
import time

from pygame.locals import *
from utils.read_file import read_file
from preferential_by_amplitude import preferential_by_amplitude
from uniform_cost import uniform_cost
from a_star import a_star
from constanst import HIGH, WIDTH
from global_variables import tree_development
from models.nodo import Node
from utils.read_world import search_mario, build_tree_solution
from avara import algorithm_avara
from preferential_by_depth import preferential_by_depth


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
        self.rect_mouse = pygame.Rect(0,0,1,1)

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
        self.flower = pygame.image.load("images/flower.png")

        self.world = read_file()
        self.run()

    def run(self):
        """
        Autor: Kevin Cardona
        Fecha: Mayo 3 2018
        Método para correr la ventana del juego y escuchar los eventos que suceden en ella.
        """
        count = 0
        type = 0

        while True:
            self.rewrite()
            pygame.display.update()

            self.clear_world()

            for i in range(len(self.world)):
                for j in range(len(self.world)):

                    if self.world[i][j] == '1':
                        self.window.blit(self.block, (j * 50, i * 50))

                    if self.world[i][j] == '4':
                        self.window.blit(self.tortle, (j * 50, i * 50))

                    if self.world[i][j] == '5':
                        self.window.blit(self.princses, (j * 50, i * 50))

                    if self.world[i][j] == '3':
                        self.window.blit(self.flower, (j * 50, i * 50))

                    if type == 0:
                        if self.world[i][j] == '2':
                            self.window.blit(self.mario, (j * 50, i * 50))

            # comparación para pintar el mario con el nodo solución
            if type:
                if count < len(build_tree):
                    self.window.blit(
                        self.mario,
                        (build_tree[count].position_y * 50, build_tree[count].position_x * 50)
                    )
                    count += 1
                    time.sleep(0.5)
                else:
                    type = 0
                    count = 0

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == K_RIGHT:
                        type = 1
                        build_tree, cost = self.execute_algorithm(type)

                        print(len(build_tree), 'amplitud')

                    if event.key == K_UP:
                        type = 2
                        build_tree, cost = self.execute_algorithm(type)
                        print(len(build_tree), 'costo ')

                    if event.key == K_LEFT:
                        type = 4
                        build_tree, cost = self.execute_algorithm(type)

                        print(len(build_tree), 'Avara')

                    if event.key == K_DOWN:
                        type = 5
                        build_tree, cost = self.execute_algorithm(type)

                        print(len(build_tree), 'A*')

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def execute_algorithm(self, type):

        """
        Autor: Carlos Almario
        Fecha: Marzo 02 2018
        Metodo para ejecutar los algoritmos dependiendo del paramtro de entrada

        :param type: tipo de algorito a ejecutar (int)
        :return: build_tree, lista con los nodos solución
                 cost, el costo de la solucion
        """
        position_x_mario, position_y_mario = search_mario(self.world)

        # limpiar lista tree_development
        self.node = Node()
        self.node.position_x = position_x_mario
        self.node.position_y = position_y_mario
        self.node.node = None
        self.node.world = self.world
        self.node.depth = 0

        # algoritmo preferente por amplitud
        if type == 1:

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
        if type == 2:

            tree_development.append(self.node)

            while True:
                goal, node_move = uniform_cost(self.world, self.node)
                if not goal:
                    self.node = node_move
                else:
                    build_tree, cost = build_tree_solution(node_move)
                    print(len(build_tree), 'costo')
                    break

        # algoritmo preferente por profundidad evitando ciclos
        if ALGORITHM_TYPE == 3:
            tree_development.append(self.node)

            expanded_nodes = 0
            while True:
                goal, node_move = preferential_by_depth(self.world, self.node)
                expanded_nodes += 1
                if not goal:
                    self.node = node_move
                else:
                    build_tree, cost = build_tree_solution(node_move)
                    break

        # algoritmo avara
        if type == 4:

            tree_development.append(self.node)
            while True:
                goal, node_move = algorithm_avara(self.world, self.node)
                if not goal:
                    self.node = node_move
                else:
                    build_tree, cost = build_tree_solution(node_move)
                    break

        # algoritmo A*
        if type == 5:

            tree_development.append(self.node)
            while True:
                goal, world, node_move = a_star(self.world, self.node)
                if not goal:
                    self.node = node_move
                else:
                    build_tree, cost = build_tree_solution(node_move)
                    break

        return build_tree, cost

    def create_text(self, text, a, b, c):
        """
            Autor: Carlos Almario
            Fecha: Marzo 28 2018
            Método para crear el texto que va se va a mostrar en la pantalla del proyecto
            :return:
        """

        return self.font_two.render(text, 0, (a, b, c))


    def clear_world(self):
        """
        Autor: Kevin Cardona
        Fecha: Marzo 6 2018
        Método para limpiar los graficos de la pantalla
        :return:
        """

        self.window.fill((0, 0, 0))
        self.background_window = pygame.Color(255, 255, 255)
        self.window.fill(self.background_window)

        # self.window.blit(self.create_text("Costo: " + self.cost, 255, 195, 0), ((len(read_file()) * 50) + 20, 50))

    def rewrite(self):
        # crea el rectanguo de la derecha y el rectangulo negro
        pygame.draw.rect(self.window, self.background_rect,
                         (len(read_file()) * 50, 0, WIDTH - len(read_file()) * 50, HIGH))
        pygame.draw.rect(self.window, self.background_rect_two,
                         ((len(read_file()) * 50) + 10, HIGH - 215, WIDTH - len(read_file()) * 50 - 20, 200))

        # muestra la palabra Algorimos en la parte derecha de la pantalla
        self.window.blit(self.texto, ((len(read_file()) * 50) + 20, 20))

        # muestra el costo en la pantalla
        cost = self.create_text("COSTO: " + self.cost, 255, 255, 255)
        num_nodes = self.create_text("NODOS EXPANDIDOS: " + self.number_nodes, 255, 255, 255)

        self.window.blit(cost, ((len(read_file()) * 50) + 10, HIGH - 215))
        self.window.blit(num_nodes, ((len(read_file()) * 50) + 10, HIGH - 200))

        self.rect_mouse.left, self.rect_mouse.top = pygame.mouse.get_pos()
        pygame.draw.rect(self.window, (0, 0, 0), self.rect_mouse)

game_window = GameWindow()
