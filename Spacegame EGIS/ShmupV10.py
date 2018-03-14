#Pygame Template - skeleton for a new pygame project
import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), "img")
snd_dir = path.join(path.dirname(__file__), "sounds")

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

font_name = pygame.font.match_font("arial")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE) #Alias/ non aliased text
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
#Video V7 8:41
def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x ,y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

#class Player(pygame.sprite.Sprite):

#class Mob(pygame.sprite.Sprite):

#class Bullet(pygame.sprite.Sprite):

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
#2 on line 51 = width of outline
#Video 10:23 , 9

class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #transform.scale = scale image to proportional size
        self.image = pygame.transform.scale(fighter_img, (50, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 21
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 6)
        self.speedx = random.randrange(-1,1)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 6)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet1_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -15

    def update(self):
        self.rect.y += self.speedy
        #Kill if it moves off the screen
        if self.rect.bottom < 0:
            self.kill()

#Load all game graphics
background = pygame.image.load(path.join(img_dir, "starfield2.png")).convert()
background_rect = background.get_rect()
fighter_img = pygame.image.load(path.join(img_dir, "playerShip1_blue.png")).convert()
#meteor_img = pygame.image.load(path.join(img_dir, "meteor1.png")).convert()
bullet1_img = pygame.image.load(path.join(img_dir, "laser1.png")).convert()
meteor_images = []
meteor_list = ["meteor1.png", "meteor2.png", "meteor3.png"]

for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []

for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
# The music
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, "Laser1.wav"))
explosion_sounds = []
for snd in ['Explosion1.wav', 'Explosion2.wav']:
    explosion_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
pygame.mixer.music.load(path.join(snd_dir, "wind.mp3"))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()
fighter = Fighter()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()
all_sprites.add(fighter)
for x in range(8):
    newmob()

score = 0
pygame.mixer.music.play(loops = -1)
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

    #check to see if a bullet hits a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 100 - hit.radius
        random.choice(explosion_sounds).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        newmob()


    #check to see if mob(s) hit the Fighter (specifies circle collision)
    hits = pygame.sprite.spritecollide(fighter, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        fighter.shield -= hit.radius * 1.5
        random.choice(explosion_sounds).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        newmob()
        if fighter.shield <= 0:
            running = False
    #Draw/render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    draw_shield_bar(screen, 5, 5, fighter.shield)
    # *After drawing everything, flip display
    pygame.display.flip()

pygame.quit()
