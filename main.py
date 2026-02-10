import pygame
pygame.init()

from config import *
from gamestates import *

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

    game.update()
    game.draw()

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()




