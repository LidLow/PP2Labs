import pygame as zxc
import time

def main():
    zxc.init()
    screen = zxc.display.set_mode((1500, 1000))
    FPS = zxc.time.Clock()

    RGB = (255, 255, 255)
    COLORNAME = "White"

    RADIUS = 10
    POSITIONS = []

    CIRCLEACTIVE = False
    RECTACTIVE = False
    CLICKS = 0
    POS = []

    PALETTE = {
        "Red": (255, 0, 0),
        "Green": (0, 255, 0),
        "Blue": (0, 0, 255),
        "Yellow": (255, 255, 0),
        "Cyan": (0, 255, 255),
        "Magenta": (255, 0, 255),
        "Black": (0, 0, 0),
        "White": (255, 255, 255),
        "Gray": (128, 128, 128),
        "Orange": (255, 165, 0),
        "Purple": (128, 0, 128),
        "Brown": (139, 69, 19)
    }

    obj = paletterSC(PALETTE)               #generator for color chageing
    
    while True:
        for event in zxc.event.get():
            if event.type == zxc.QUIT:
                return
            if event.type == zxc.KEYDOWN:               #change radius
                if event.key == zxc.K_z:
                    RADIUS -= 1 if RADIUS > 0 else 0
                if event.key == zxc.K_x:
                    RADIUS += 1

                if event.key == zxc.K_c:                   #clear screen
                    POSITIONS.clear()
                    screen.fill((0, 0, 0))
                if event.key == zxc.K_e:                    #eraser mode
                    POSITIONS.clear()
                    RGB = (0, 0, 0)
                if event.key == zxc.K_d:                    #draw mode
                    POSITIONS.clear()           
                    RGB = (255, 255, 255)   
                if event.key == zxc.K_r:                    #change color
                    objTuple = next(obj)
                    RGB = objTuple[1]
                    COLORNAME = objTuple[0]

                if event.key == zxc.K_a:        #draw cirlce
                    CIRCLEACTIVE = True
                    print(CIRCLEACTIVE)
                if event.key == zxc.K_s:        #draw rect
                    RECTACTIVE = True
                    print(RECTACTIVE)
                
            if CIRCLEACTIVE and event.type == zxc.MOUSEBUTTONDOWN:
                CLICKS += 1
                POS.append(zxc.mouse.get_pos())

                if CLICKS == 2:
                    TEMP_RADIUS = round(((POS[0][0] - POS[1][0])**2 + (POS[0][1] - POS[1][1])**2)**0.5)
                    zxc.draw.circle(screen, RGB, POS[0], TEMP_RADIUS)

                    CIRCLEACTIVE = False
                    CLICKS = 0
                    POS.clear()
                    POSITIONS.clear()

            if RECTACTIVE and event.type == zxc.MOUSEBUTTONDOWN:
                CLICKS += 1
                POS.append(zxc.mouse.get_pos())
                print("OK")

                if CLICKS == 2:
                    zxc.draw.rect(screen, RGB, (min(POS[0][0], POS[1][0]), min(POS[0][1], POS[1][1]), abs(POS[0][0] - POS[1][0]), abs(POS[0][1] - POS[1][1])))

                    RECTACTIVE = False
                    CLICKS = 0
                    POS.clear()
                    POSITIONS.clear()
                    
            if zxc.mouse.get_pressed()[0]:                  #draw while pressing lef button
                position = zxc.mouse.get_pos()
                POSITIONS = POSITIONS + [position]
                POSITIONS = POSITIONS[-256:]

            if event.type == zxc.MOUSEBUTTONUP:         #clear previous positions
                POSITIONS.clear()                      


        i = 0
        while i < len(POSITIONS) - 1:
            drawLineBetween(screen, POSITIONS[i], POSITIONS[i + 1], RADIUS, RGB)
            i += 1
        

        zxc.display.set_caption(f"Width: {RADIUS * 2} | Color: {COLORNAME}")
        zxc.display.flip()
        
        FPS.tick(60)

def paletterSC(PALETTE):
    while True:
        for key, value in PALETTE.items():
            yield (key, value) 

def drawLineBetween(screen, start, end, width, RGB):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        zxc.draw.circle(screen, RGB, (x, y), width)

main()