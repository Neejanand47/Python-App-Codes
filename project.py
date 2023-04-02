import pygame

pygame.init()

pygame.display.set_mode((480, 580))
pygame.display.set_caption("a racing game by simply code")

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()            