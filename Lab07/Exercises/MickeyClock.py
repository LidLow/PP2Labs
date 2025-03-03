import pygame

def musicCenter():
    pass

pygame.init()
screen = pygame.display.set_mode((1200, 900))
image = pygame.image.load(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab07\Exercises\mickeyclock.jpeg")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        screen.blit(image, (0, 0))

        pygame.display.flip()