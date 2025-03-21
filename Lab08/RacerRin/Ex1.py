import pygame as zxc
import os
import sys
import random

os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab08\RacerRin\Images")

zxc.init()

screen = zxc.display.set_mode((400, 400))
FPS = zxc.time.Clock()
done = False

class Enemy(zxc.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = zxc.transform.rotate(zxc.image.load("Motorcycle.png"), -90)
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,360),0) 
 
    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 400):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Player(zxc.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = zxc.transform.rotate(zxc.image.load("Motorcycle.png"), -90)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 320)
 
    def update(self):
        pressed_keys = zxc.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[zxc.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < 400:        
              if pressed_keys[zxc.K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)  


P1 = Player()
E1 = Enemy()
 
while True:     
    for event in zxc.event.get():              
        if event.type == zxc.QUIT:
            zxc.quit()
            sys.exit()
    P1.update()
    E1.move()
     
    screen.fill((255, 255, 255))
    P1.draw(screen)
    E1.draw(screen)
         
    zxc.display.update()
    FPS.tick(60)