import pygame
import sys
import time

from pygame.locals import *
from utils.read_file import read_file
from algorithm_types import preferential_by_amplitude, build_tree_solution, uniform_cost
from constanst import ALGORITHM_TYPE, HIGH, WIDTH
from global_variables import tree_development, build_tree
from models.nodo import Node


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

        self.background_rect_two = pygame.Color(0,0,0)

        self.font = pygame.font.Font("images/SuperMario256.ttf",20)
        self.font_two = pygame.font.SysFont("Arial", 10)

        self.texto = self.font.render("Algoritmos",0,(255, 195, 0))

        pygame.display.set_caption("Mario")

        self.block = pygame.image.load("images/bloque.png")
        self.tortle = pygame.image.load("images/tortle.png")
        self.mario = pygame.image.load("images/mario.png")
        self.princses = pygame.image.load("images/princesa.png")

        self.world = read_file()
        self.run()

    def run(self):
        """
        Autor: Kevin Cardona
        Fecha: Mayo 3 2018
        Método para correr la ventana del juego y escuchar los eventos que suceden en ella.
        """
        self.window.fill(self.background_window)

        position_x_mario, position_y_mario = self.draw_world(self.world)

        if ALGORITHM_TYPE == 1:

            self.node = Node()
            self.node.position_x = position_x_mario
            self.node.position_y = position_y_mario
            self.node.node = None
            self.node.world = self.world
            tree_development.append(self.node)


            aux = 0
            while True:
                goal, world, node_move = preferential_by_amplitude(self.world, self.node)
                if not goal:
                    self.world = world
                    self.node = node_move
                    aux += 1


                else:
                    print('YOU WIN')
                    build_tree_solution(node_move)

                    break

            build_tree = build_tree_solution(node_move)

        if ALGORITHM_TYPE == 2:

            self.node = Node()
            self.node.position_x = position_x_mario
            self.node.position_y = position_y_mario
            self.node.node = None
            self.node.world = self.world
            tree_development.append(self.node)

            aux = 0
            while True:
                goal, world, node_move = uniform_cost(self.world, self.node)
                if not goal:
                    self.world = world
                    self.node = node_move
                    aux += 1
                else:
                    print('YOU WIN')
                    build_tree_solution(node_move)
                    break

            build_tree, cost = build_tree_solution(node_move)
            print('nodos expandidos: ' + str(aux)+' Costo: '+str(cost))

            self.number_nodes = str(aux)
            self.cost = str(cost)

        count = 0
        while True:
            self.clear_world()
            self.draw_world(read_file())

            if (count < len(build_tree)):
                self.window.blit(self.mario, (build_tree[count].position_y * 50,  build_tree[count].position_x * 50))
                count+=1

                time.sleep(0.5)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def draw_world(self, world):
        """
        Autor: Kevin Cardona
        Fecha: Marzo 6 2018
        Método para dibujar el mundo, consta de un doble for para dibujar las posiciones en x y posiciones en y
        """
        position_x_mario, position_y_mario = '', ''

        for i in range(len(world)):
            for j in range(len(world)):
                if world[i][j] == '1':
                    self.window.blit(self.block, (j * 50, i * 50))

                if world[i][j] == '4':
                    self.window.blit(self.tortle, (j * 50, i * 50))

                if world[i][j] == '2':
                    position_x_mario, position_y_mario = i, j
                    #self.window.blit(self.mario, (j * 58, i * 53))

                if world[i][j] == '5':
                    self.window.blit(self.princses, (j * 50, i * 50))

        return position_x_mario, position_y_mario



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
        # crea el rectanguo de la derecha y el rectangulo negro
        pygame.draw.rect(self.window, self.background_rect,(len(read_file()) * 50, 0, WIDTH - len(read_file()) * 50, HIGH))
        pygame.draw.rect(self.window, self.background_rect_two,((len(read_file()) * 50)+10, HIGH - 215, WIDTH - len(read_file()) * 50 -20, 200))

        # muestra la palabra Algorimos en la parte derecha de la pantalla
        self.window.blit(self.texto,((len(read_file()) * 50)+20,20))

        # muestra el costo en la pantalla
        cost = self.create_text("COSTO: "+self.cost, 255, 255,255)
        num_nodes = self.create_text("NODOS EXPANDIDOS: "+self.number_nodes, 255, 255,255)

        self.window.blit(cost, ((len(read_file()) * 50)+10, HIGH - 215))
        self.window.blit(num_nodes, ((len(read_file()) * 50) + 10, HIGH - 200))


        #self.window.blit(self.create_text("Costo: " + self.cost, 255, 195, 0), ((len(read_file()) * 50) + 20, 50))

    def create_text(self,text, a, b, c):
        """
            Autor: Carlos Almario
            Fecha: Marzo 28 2018
            Método para crear el texto que va se va a mostrar en la pantalla del proyecto
            :return:
        """

        return self.font_two.render(text, 0, (a, b,c))





game_window = GameWindow()
