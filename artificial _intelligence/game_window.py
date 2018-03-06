import pygame
import sys

from pygame.locals import *
from utils.read_file import read_file
from algorithm_types import preferential_by_amplitude
from constanst import ALGORITHM_TYPE


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

        self.window = pygame.display.set_mode((500, 500))
        self.background_window = pygame.Color(255, 255, 255)
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
            preferential_by_amplitude(self.world, position_x_mario, position_y_mario)

        while True:

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
                    self.window.blit(self.mario, (j * 58, i * 53))

                if world[i][j] == '5':
                    self.window.blit(self.princses, (j * 50, i * 50))

        return position_x_mario, position_y_mario

game_window = GameWindow()
