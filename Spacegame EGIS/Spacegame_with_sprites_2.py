#Pygame Template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#set up assets(art and sound) folders
#Image file = C:\Users\egis\Desktop\EGIS Python Golden-Leaf\Spacegame EGIS\Images\Player_ship.png
#Image folder = C:\Users\egis\Desktop\EGIS Python Golden-Leaf\Spacegame EGIS\Images
game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "Images")

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_folder, "Player_ship.png")).convert()
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

#Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#Game loop
running = True
while running:
    #Keep loop running at the right speed
    clock.tick(FPS)
    #process imput (events)
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False
    #update
    all_sprites.update()
    #Draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *After drawing everything, flip display
    pygame.display.flip()

pygame.quit()