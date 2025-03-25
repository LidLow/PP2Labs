import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

radius = 25
FPS = pygame.time.Clock()

color = (255, 255, 255)
radius = 15
points = []

done = False
erase = False

variable = "circle"

shapes = ("circle", "rectangle")

def gen(shapes):
     while True:
          for ev in shapes:
               yield ev

Shape = gen(shapes)

def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

while not done:  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            erase = not erase

        if pygame.mouse.get_pressed()[0] and erase:
            position = pygame.mouse.get_pos()
            points = points + [position]
        if event.type == pygame.MOUSEBUTTONUP:       
            points.clear()

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                variable = next(Shape)

            if event.key == pygame.K_v:
                if variable == "circle":
                    pygame.draw.circle(screen, color, pygame.mouse.get_pos(), radius)
                elif variable == "rectangle":
                    pygame.draw.rect(screen, color, pygame.mouse.get_pos(), (radius, radius))  

        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, points[i], points[i + 1], radius, color)
            i += 1

    pygame.display.flip()
    FPS.tick(60)

pygame.quit()