import pygame
from config import *
from ui import UIElement


class Player(UIElement):
    def __init__(self, x, y, width, height, background):
        super().__init__(x, y, width, height, background)
        self.speed = 2

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed