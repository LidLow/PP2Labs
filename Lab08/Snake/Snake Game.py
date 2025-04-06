import pygame, random

pygame.init()

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = 900
HEIGHT = 900

FPS = 5

screen = pygame.display.set_mode((HEIGHT, WIDTH))

#One cell is 30x30 pixels
#The grid is 30x30 cells

CELL = 30

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, GRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [WHITE, GRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(15, 15), Point(14, 15)]
        self.dx = 0
        self.dy = 0
        self.lvl = 0
        self.points = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, RED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def checkFoodCollision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score()
            self.body.append(Point(head.x, head.y))
            food.__init__()                                                 #new coordinates for the food

    def checkWallCollision(self):                                           #wall collisison
        head = self.body[0]
        if head.x not in range(0, 30) or head.y not in range(0, 30):
            global running
            running = False                                 

    def score(self):                                                        #score system
        self.points += 1
        if self.points % 5 == 0:
            self.points = 0
            self.lvl += 1
            global FPS                                                      #increasing the speed after each new level
            FPS += 1

class Food:
    def __init__(self):
        self.pos = Point(random.randint(0, 29), random.randint(0, 29))

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    
clock = pygame.time.Clock()

food = Food()   
snake = Snake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_a:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_s:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_w:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()

    snake.move()
    snake.checkFoodCollision(food)
    snake.checkWallCollision()

    snake.draw()
    food.draw()

    pygame.display.set_caption(f"Level: {snake.lvl} | Points: {snake.points + snake.lvl }") #displaying the points and level

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()