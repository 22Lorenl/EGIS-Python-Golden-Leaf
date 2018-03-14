#Importation of modules
import pygame
import random

#Pygame start
pygame.init()

#Screen Dimensions
display_width = 800
display_height = 600

#Screen
Gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Space Invaders I")
clock = pygame.time.Clock()

#Variables
FPS = 60
display_width = 800
display_height = 600
x = (display_width * 0.45)
y = (display_height * 0.8)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

destroyed = False

#Game Running
while not destroyed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            destroyed = True

    Gamedisplay.fill(white)
    pygame.display.update()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
