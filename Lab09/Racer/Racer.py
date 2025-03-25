import pygame, sys, os
from pygame.locals import *
import random, time

os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab09\Racer")

pygame.init()

FPS = pygame.time.Clock()

BLUE  = (0, 0, 255)                                                              #colors
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH  = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 60)                                       #fonts
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"Images\Street.png")                

screen = pygame.display.set_mode((400,600))            
screen.fill(WHITE)

INC_SPEED = pygame.USEREVENT + 1       

class Enemy(pygame.sprite.Sprite):                                                  
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"Images\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"Images\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_keys[K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_d]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"Images\Coin.png")
        self.rect = self.image.get_rect()
        self.weight = random.randint(1, 3)                        #assigning random weight from 1 to 3
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
                      
P1 = Player()
E1 = Enemy()
C = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
collectables = pygame.sprite.Group()
collectables.add(C)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)        

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:             #the place where it activates
            SPEED += 1      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))

    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10,10))

    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
        
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r'Sounds\crash.wav').play()
        time.sleep(1)
                   
        screen.fill(RED)
        screen.blit(game_over, (30,250))
          
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    if pygame.sprite.spritecollideany(P1, collectables):
        pygame.mixer.Sound(r'Sounds\collectCoin.wav').play()
        COINS += C.weight

        if COINS % 5 == 0:                                       #when N=5 speed increases
            pygame.event.post(pygame.event.Event(INC_SPEED))

        C.__init__()
        
    pygame.display.update()
    FPS.tick(60)