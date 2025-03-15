import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
X, Y = 245, 245
R = 0
Clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]: 
        Y -= 5
        R += 1
    if pressed[pygame.K_s]: 
        Y += 5 
        R += 1
    if pressed[pygame.K_a]: 
        X -= 5
        R += 1
    if pressed[pygame.K_d]: 
        X += 5
        R += 1

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (R, 0, 0), pygame.Rect(X, Y, 10, 10))
    pygame.display.flip()
    Clock.tick(60)

pygame.quit()