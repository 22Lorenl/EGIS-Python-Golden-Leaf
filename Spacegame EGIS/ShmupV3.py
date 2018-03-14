#Pygame Template - skeleton for a new pygame project
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 60

#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

#Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 6)
        self.speedx = random.randrange(-1,1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 6)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -15

    def update(self):
        self.rect.y += self.speedy
        #Kill if it moves off the screen
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
fighter = Fighter()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()
all_sprites.add(fighter)
for x in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fighter.shoot()
    #update
    all_sprites.update()

    #check to see if a bullet hits a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)


    #check to see if mob(s) hit the Fighter
    hits = pygame.sprite.spritecollide(fighter, mobs, False)
    if hits:
        running = False
    #Draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *After drawing everything, flip display
    pygame.display.flip()

pygame.quit()
