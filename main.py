import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (197, 201, 199), [60, 50, 10, 500], 0)
    pygame.draw.rect(screen, (255, 255, 255), [70, 60, 450, 100], 0)

    pygame.display.flip()

pygame.quit()
