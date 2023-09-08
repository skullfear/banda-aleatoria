from banda import *
import pygame
from pygame.locals import *

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

instrument_image = pygame.image.load('guitarra.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(instrument_image, (100, 100)) 


