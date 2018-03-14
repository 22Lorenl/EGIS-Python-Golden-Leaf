#Pygame Template - skeleton for a new pygame project
import pygame
import random

# This is a copy

WIDTH = 800
HEIGHT = 600
FPS = 30

#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.y_speed = 5
    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

class Enemy(pygame.sprite.Sprite):
    #Sprite for the Enemy
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect= self.image.get_rect()
        self.rect.center = (WIDTH/3, HEIGHT/3)
        self.y_speed = 5
    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

class Asteroid(pygame.sprite.Sprite):
    #Sprite for the Asteroid
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/4, HEIGHT/4)
        self.y_speed = 5
    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
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
enemy = Enemy()
asteroid = Asteroid()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(asteroid)
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
