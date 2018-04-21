import pygame
import random
from Settings import *
from Sprites import *

class Game:
    #Start Game Window
    def __init__(self):
        self.running = True
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
    #Starts the Game
    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.fighter = Fighter()
        self.all_sprites.add(self.fighter)
        self.run()
    #Game Loop
    def run(self):
        self.clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    #Game Loop Update
    def update(self):
        self.all_sprites.update()

    #Game Loop events
    def events(self):
        for event in pygame.event.get():
            #Closing Window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                running = False
                sys.exit()

    #Game Loop events
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    def show_gameover_screen(self):
        pass

    def show_start_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new_game()
    g.show_gameover_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
