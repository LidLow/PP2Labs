import pygame as zxc

def main():
    zxc.init()
    screen = zxc.display.set_mode((1000, 1000))
    FPS = zxc.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        for event in zxc.event.get():
            if event.type == zxc.QUIT:
                return
            if event.type == zxc.KEYDOWN:
                pass
            
            if event.type == zxc.MOUSEMOTION and zxc.mouse.get_pressed()[0]:
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))

        drawLineBetween(screen, points[i], points[i + 1], radius)
    
        zxc.display.flip()
        
        FPS.tick(60)

def drawLineBetween(screen, start, end, width):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        zxc.draw.circle(screen, (255, 255, 255), (x, y), width)

main()