import pygame

# Värit
GREEN = (0, 255, 0)
DARK_GRAY = (50, 50, 50)
GRAY = (120, 120, 120)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (210, 210, 210)
RED = (170, 0, 0)

# Ikkuna
FPS = 60
WINDOW = pygame.display.set_mode((1200, 800), 0, 0)
pygame.display.set_caption("RPG Game")
CLOCK = pygame.time.Clock()

#Fontit ja kuvat
menu_button_png = pygame.image.load("assets/buttons/button_background.png").convert_alpha()
menu_button_font = pygame.font.Font("assets/fonts/MorrisRoman-Black.ttf", 40)
title_font = pygame.font.Font("assets/fonts/MorrisRoman-Black.ttf", 100)
text_font = pygame.font.Font("assets/fonts/MorrisRoman-Black.ttf", 20)
