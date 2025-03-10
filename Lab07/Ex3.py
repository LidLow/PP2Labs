import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
X = 500 // 2
Y = 500 // 2
done = False

Clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and (Y - 20 > 24): Y -= 20
    if pressed[pygame.K_s] and (Y + 20 < 476): Y += 20
    if pressed[pygame.K_a] and (X - 20 > 24): X -= 20
    if pressed[pygame.K_d] and (X + 20 < 476): X += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (X, Y), 25)

    pygame.display.flip()
    Clock.tick(60)
    
pygame.quit()