import pygame
from pygame.locals import *
import random
from sys import exit
from time import sleep

#Game - starting principles
#Dimensions of screen + starting of program

pygame.init()
display_width = 100
display_height = 800

#Starting location of ball
startx = random.randint(0, display_width)
starty = random.randint(200, display_height)


#Variabes I
dx = 10
dy = 8

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
Some_random_color = (6, 66, 123)

color_selection_1 = (white, red, green, blue, Some_random_color)

color = random.choice(color_selection_1)

#Display I
Display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()

#Forever bouncing ball part
while True:
    Display.fill(color)

    if startx > display_width or startx <= 0:
        dx = -dx

    if starty > display_height or starty <=0:
        dy = -dy

    startx = startx + dx
    starty = starty + dy

#Forever changing color part
    x = random.randint(0,255)
    y = random.randint(0,255)
    z = random.randint(0,255)
    ballColor = (red, green, blue)

    pygame.draw.circle(Display, ballColor, [startx, starty], 10)
    sleep(.1)
    pygame.display.update()








