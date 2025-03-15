import pygame as zxc
import datetime

import os
os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab07\Pictures")

zxc.init()

screen = zxc.display.set_mode((800, 600))
FPS = zxc.time.Clock()
done = False

backGnd = zxc.image.load("clock.png")

angleM = 0
minArrow = zxc.image.load("min_hand.png")
minArrowRect = minArrow.get_rect()

angleS = 0
secArrow = zxc.image.load("sec_hand.png")
secArrowRect = secArrow.get_rect(center=(400, 300))

while not done:
    for event in zxc.event.get():
        if event.type == zxc.QUIT:
            done = True

    rotateSecArrow = zxc.transform.rotate(secArrow, angleS)
    rotateSecArrowRect = rotateSecArrow.get_rect(center=secArrowRect.center)

    rotateMinArrow = zxc.transform.rotate(minArrow, angleM)
    rotateMinArrowRect = rotateMinArrow.get_rect(center=minArrowRect.center)

    screen.blit(backGnd, (0, 0))
    screen.blit(rotateSecArrow, rotateSecArrowRect.topleft)
    screen.blit(rotateMinArrow, rotateMinArrowRect.topleft)
    
    curTime = datetime.datetime.now() # current time
    angleM = curTime.minute * -7.5
    angleS = curTime.second * -6

    zxc.display.flip()

    FPS.tick(60)

zxc.quit()