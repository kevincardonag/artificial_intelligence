
import pygame, sys
import read_file
from pygame.locals import *


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

        self.window = pygame.display.set_mode((500,500))
        self.background_window = pygame.Color(255,255,255)
        pygame.display.set_caption("Mario")

        self.block = pygame.image.load("images/bloque.png")
        self.tortle = pygame.image.load("images/tortle.png")
        self.mario = pygame.image.load("images/mario.png")
        self.princses = pygame.image.load("images/princesa.png")

        self.run()

    def run(self):
        """
        Autor: Kevin Cardona
        Fecha: Mayo 3 2018
        Método para correr la ventana del juego y escuchar los eventos que suceden en ella.
        la construcción de la matriz se denota por la variables "i" e "j", correspondientes a la posición en "X"
        e "Y" respectivamente.
        """
        while True:
            self.window.fill(self.background_window)

            for i in range(len(read_file.world)):
                for j in range(len(read_file.world)):
                    if read_file.world[i][j] == '1':
                        self.window.blit(self.block, (j * 50, i * 50))

                    if read_file.world[i][j] == '4':
                        self.window.blit(self.tortle, (j * 50, i * 50))

                    if read_file.world[i][j] == '2':
                        self.window.blit(self.mario, (j * 58, i * 53))

                    if read_file.world[i][j] == '5':
                        self.window.blit(self.princses, (j * 50, i * 50))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


game_window = GameWindow()
