import pygame, random, sys
import SQL

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

CELL = 25
WIDTH = 500
HEIGHT = 500

CLOCK = pygame.time.Clock()
FPS = 5

PAUSED = False

SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))

NEW_FOOD = pygame.USEREVENT + 1                     
pygame.time.set_timer(NEW_FOOD, 10000)          #execution of the event after 10 seconds

FONT = pygame.font.SysFont("Verdana", 60)   
FONT_SMALL = pygame.font.SysFont("Verdana", 32)                                    #font
PAUSE_SCREEN = FONT.render("Paused", True, BLACK)

def getUserInfo():
    user_name = ""
    input_box = pygame.Rect(100, 200, 300, 50)
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(user_name) > 0:
                    return SQL.checkUser(user_name)
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                elif len(user_name) < 20:
                    user_name += event.unicode

        enters = FONT_SMALL.render("Enter your name:", True, BLACK)
        name_text = FONT_SMALL.render(user_name, True, BLACK)

        SCREEN.fill(WHITE)
        SCREEN.blit(enters, (input_box.x, input_box.y - 40))
        SCREEN.blit(name_text, (input_box.x + 5, input_box.y + 10))

        pygame.draw.rect(SCREEN, BLACK, input_box, 2)

        pygame.display.flip()
        CLOCK.tick(30)

def drawGrid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(SCREEN, GRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def drawGridChess():
    colors = [WHITE, GRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(SCREEN, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self, level, score):
        self.body = [Point(7, 7), Point(7, 7)]
        self.dx = 1
        self.dy = 0
        self.score = score
        self.level = level

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(SCREEN, RED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(SCREEN, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def checkFoodCollision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            global FPS
            FPS += 1
            self.score += FOOD.weight 
            self.body.append(Point(head.x, head.y))
            food.__init__()                                                 #new coordinates of FOOD class OBJ

    def checkWallCollision(self):                                           #wall collisison
        head = self.body[0]
        if head.x not in range(0, HEIGHT // CELL) or head.y not in range(0, WIDTH // CELL):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

class Food:
    def __init__(self):
        self.pos = Point(random.randint(0, HEIGHT // CELL - 1), random.randint(0, WIDTH // CELL - 1))
        self.weight = random.randint(1, 3)
        pygame.time.set_timer(NEW_FOOD, 10000)

    def draw(self):
        pygame.draw.rect(SCREEN, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

USER_INFO = getUserInfo()

FOOD = Food()   
SNAKE = Snake(USER_INFO[1], USER_INFO[2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == NEW_FOOD:
            FOOD.__init__()           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAUSE:
                PAUSED = not PAUSED
            if event.key == pygame.K_z:
                SQL.saveScore(USER_INFO[0], SNAKE.level, SNAKE.score)
            if event.key == pygame.K_d and SNAKE.dx != -1:
                SNAKE.dx = 1
                SNAKE.dy = 0
            elif event.key == pygame.K_a and SNAKE.dx != 1:
                SNAKE.dx = -1
                SNAKE.dy = 0
            elif event.key == pygame.K_s and SNAKE.dy != -1:
                SNAKE.dx = 0
                SNAKE.dy = 1
            elif event.key == pygame.K_w and SNAKE.dy != 1:
                SNAKE.dx = 0
                SNAKE.dy = -1

    drawGridChess()

    if not PAUSED:
        SNAKE.move()
    if PAUSED:
        SCREEN.fill(WHITE)
        SCREEN.blit(PAUSE_SCREEN, (250, 50))

    SNAKE.checkFoodCollision(FOOD)
    SNAKE.checkWallCollision()

    SNAKE.draw()
    FOOD.draw()

    pygame.display.set_caption(f"Score: {SNAKE.score}")

    pygame.display.flip()
    CLOCK.tick(FPS)