
import pygame,sys
import read_file
import Nodo
from pygame.locals import *


pygame.init()

window = pygame.display.set_mode((500,500))
background_window = pygame.Color(255,255,255)
pygame.display.set_caption("Mario")

block = pygame.image.load("images/bloque.png")
tortle = pygame.image.load("images/tortle.png")
mario = pygame.image.load("images/mario.png")
princses = pygame.image.load("images/princesa.png")



while True:
    window.fill(background_window)


    for i in range(len(read_file.world)):
        for j in range(len(read_file.world)):
            if read_file.world[i][j] == '1':
                window.blit(block,(j*50,i*50))

            if read_file.world[i][j] == '4':
                window.blit(tortle, (j * 50, i * 50))

            if read_file.world[i][j] == '2':
                window.blit(mario, (j * 58, i * 53))

            if read_file.world[i][j] == '5':
                window.blit(princses, (j * 50, i * 50))


    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()