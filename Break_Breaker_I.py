#WIP
import math
import pygame

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

#Size of blocks
block_width = 23
block_height = 15

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pyame.Surface([block_width, block_heighht])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ball(pygame.sprite.Sprite):
    speed = 10.0
    x =  0.0
    y = 180.0
    direction = 200
    width = 10
    height = 10
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(black)
        self.rect = self.image.get_rect()
#For the horizontal bounce property
    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff
    def update(self):
        direction_radians = math.sin(direction_radians)
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(directions_radians)
        self.rect.x = self.x
        selfrect.y = self.y
#If ball goes to the top of the screen
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
#If ball goes to the left of the screen
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
#If ball goes to te right of the screen
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1
#If  ball goes to the bottom side of the screen --- Note: Change later that when ball drops --> game is over
        if self.y > 600:
            return True
        else:
            return False

#Represents the rectangle paddle
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 75
        self.width = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((black))
        self.rect = self.image.get_rect()
        self.screenheight = pygame.dislay.get_surface().get_height()
        self.screenheight = oygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = 0
        self.rect.y = self.screenheight - self.height
    def update(self):
#Indicating that control is by mouse, not by arrow keys! --- Note: Possibility where controls may be altered
        pos = pyame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width

pygame.init()

#Screen Dimensions
screen = pygame.display.set_mode([800, 600])

#Title of game
pygame.display.set_caption('My first pygame')

#If mouse hovers over window --> dissappear
pygame.mouse.set_visible(0)

#Font
font = pygame.font.Font(None, 36)

#Background
background = pygame.Surface(screen.get_size())

#Sprite Lists
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

#Player paddle object
player = Player()
allsprites.add(player)

#Ball
ball = Ball()
allsprites.add(ball)
ball.add(ball)

#The top of the block --- y position ---
top = 80

#number of blocks to create
blockcount = 32

#Create rows of blocks
for row in range(5):
#32 columns of blocks
    for column in range(0, blockcount):
#Block info
        block.Block(blue, column * (block_width + 2) + 1, top)
        block.add(block)
        allsprite.add(block)
    top += block_height + 2

clock = pygame.time.Clock()

game_over = False

while not exit_program:
    clock.tick(30)
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

    if not game_over:
        player.update()
        game_over = ball.update()

    if game_over:
        text - font.render("Game Over", True, white)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 300
        screen.blit(text, textpos)

    if pygame.sprite.spritecollide(ball, blocks, True):
        diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)
        ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
        ball.bounce(diff)

    deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
        
    if len(deadblocks) > 0:
        ball.bounce(0)

        if len(blocks) == 0:
            game_over = True

        allsprites.draw(screen)

        pygame.display.flip()

pygame.quit()
        


        
        
        
