import pygame as zxc
import math

def main():
    zxc.init()
    SCREEN = zxc.display.set_mode((1500, 1000))
    FPS = zxc.time.Clock()

    RGB = (255, 255, 255)
    COLORNAME = "White"

    RADIUS = 10
    POSITIONS = []

    GEOFIGACTIVE = False
    CLICKS = 0
    POS = []
   
    FIGURES = ("Circle", "Rectangle", "Square", "Right triangle", "Equilateral triangle", "Rhombus")
    FIGURE = FIGURES[0]

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

    colorOBJ = paletteSC(PALETTE)               #new generator for color changeing
    figureOBJ = figureMode(FIGURES)             #new generator for figeure changeing
    
    while True:
        for event in zxc.event.get():
            if event.type == zxc.QUIT:
                return
            if event.type == zxc.KEYDOWN:               #change radius
                if event.key == zxc.K_z:
                    RADIUS -= 1 if RADIUS > 0 else 0
                if event.key == zxc.K_x:
                    RADIUS += 1

                if event.key == zxc.K_c:                   #clear SCREEN
                    POSITIONS.clear()
                    SCREEN.fill((0, 0, 0))
                if event.key == zxc.K_e:                    #eraser mode
                    POSITIONS.clear()
                    RGB = (0, 0, 0)
                if event.key == zxc.K_d:                    #draw mode
                    POSITIONS.clear()           
                    RGB = (255, 255, 255)   
                if event.key == zxc.K_r:                    #change color
                    colorTuple = next(colorOBJ)
                    RGB = colorTuple[1]
                    COLORNAME = colorTuple[0]

            pressed = zxc.key.get_pressed()
            if pressed[zxc.K_a]:                                 #figure drawing works when a is pressed
                GEOFIGACTIVE = True

                if event.type == zxc.MOUSEWHEEL:                        #figure choose mode
                    FIGURE = next(figureOBJ)
                if event.type == zxc.MOUSEBUTTONDOWN and event.button in [1, 3]:      #figuer draw mode
                    CLICKS += 1
                    POS.append(zxc.mouse.get_pos())

                    if CLICKS == 2:
                        drawFigure(SCREEN, RGB, FIGURE, POS)

                        CLICKS = 0
                        POS.clear()
                        POSITIONS.clear()
            else:
                GEOFIGACTIVE = False
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
            drawLineBetween(SCREEN, POSITIONS[i], POSITIONS[i + 1], RADIUS, RGB)
            i += 1

        zxc.display.set_caption(f"Width: {RADIUS * 2} | Color: {COLORNAME}" + (f" | Figure: {FIGURE}" if GEOFIGACTIVE else ""))
        zxc.display.flip()
        
        FPS.tick(60)

def paletteSC(PALETTE):
    while True:
        for key, value in PALETTE.items():
            yield (key, value) 

def figureMode(FIGURES):
    while True:
        for figure in FIGURES:
            yield figure

def drawFigure(SCREEN, RGB, FIGURE, POS):
    if FIGURE == "Circle":
        radius = round(((POS[0][0] - POS[1][0])**2 + (POS[0][1] - POS[1][1])**2)**0.5)
        zxc.draw.circle(SCREEN, RGB, POS[0], radius)
    
    elif FIGURE == "Rectangle":
        zxc.draw.rect(SCREEN, RGB, (min(POS[0][0], POS[1][0]), min(POS[0][1], POS[1][1]), abs(POS[0][0] - POS[1][0]), abs(POS[0][1] - POS[1][1])))
    
    elif FIGURE == "Square":
        zxc.draw.rect(SCREEN, RGB, (min(POS[0][0], POS[1][0]), min(POS[0][1], POS[1][1]), max(abs(POS[0][0] - POS[1][0]), abs(POS[0][1] - POS[1][1])), max(abs(POS[0][0] - POS[1][0]), abs(POS[0][1] - POS[1][1]))))
    
    elif FIGURE == "Right triangle":
        zxc.draw.polygon(SCREEN, RGB, [(POS[0][0], POS[0][1]), (POS[1][0], POS[0][1]), (POS[0][0], POS[1][1])])

    elif FIGURE == "Equilateral triangle":
        side = max(abs(POS[0][0] - POS[1][0]), abs(POS[0][1] - POS[1][1]))
        x1, y1 = POS[0] 
        x2, y2 = x1 + side, y1
        x3, y3 = x1 + side / 2, y1 - (math.sqrt(3) / 2) * side

        zxc.draw.polygon(SCREEN, RGB, [(x1, y1), (x2, y2), (x3, y3)])
    
    elif FIGURE == "Rhombus":
        cx, cy = (POS[0][0] + POS[1][0]) // 2, (POS[0][1] + POS[1][1]) // 2
        dx, dy = abs(POS[0][0] - POS[1][0]) // 2, abs(POS[0][1] - POS[1][1]) // 2

        zxc.draw.polygon(SCREEN, RGB, [(cx, cy - dy), (cx + dx, cy), (cx, cy + dy), (cx - dx, cy)])

    return 

def drawLineBetween(SCREEN, start, end, width, RGB):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        zxc.draw.circle(SCREEN, RGB, (x, y), width)

main()