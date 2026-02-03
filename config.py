import pygame

GREEN = (0, 255, 0)
DARK_GRAY = (50, 50, 50)
GRAY = (120, 120, 120)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (210, 210, 210)
RED = (170, 0, 0)

FPS = 60

menu_button_png = None
menu_button_font = None
title_font = None
text_font = None

# Ikkuna
def create_window():
    global WINDOW, CLOCK
    WINDOW = pygame.display.set_mode((1200, 800), 0, 0)
    pygame.display.set_caption("Peli")
    CLOCK = pygame.time.Clock()

    return WINDOW, CLOCK

# Fontit ja kuvat
def load_assets():
    global menu_button_png, menu_button_font, title_font, text_font
    menu_button_png = pygame.image.load("assets/buttons/button_background.png").convert_alpha()
    menu_button_font = pygame.font.Font("assets/fonts/MorrisRoman-Black.ttf", 40)
    title_font = pygame.font.Font("assets/fonts/MorrisRoman-Black.ttf", 100)
    text_font = pygame.font.Font("assets/fonts/MorrisRoman-Black.ttf", 20)


