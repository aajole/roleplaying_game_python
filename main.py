import pygame
pygame.init()

from ui import *
from config import *

# Tilat
game_state = "main_menu"
running = True


# Nappien toiminnot
def main_menu():
    global game_state
    game_state = "main_menu"

def new_game():
    global game_state
    game_state = "new_game"

def load_game():
    global game_state
    game_state = "load_game"

def map_editor():
    global game_state
    game_state = "map_editor"

def playing():
    global game_state
    game_state = "playing"

def exit_game():
    global running
    running = False


# Päävalikko
button_x = WINDOW.get_width() // 2 - menu_button_png.get_width() // 2
main_menu_buttons = [
Button(button_x, 250, "New Game", menu_button_font, LIGHT_GRAY, menu_button_png, new_game),
Button(button_x, 350, "Load Game", menu_button_font, LIGHT_GRAY, menu_button_png, load_game),
Button(button_x, 450, "Map Editor", menu_button_font, LIGHT_GRAY, menu_button_png, map_editor),
Button(button_x, 550, "Exit", menu_button_font, LIGHT_GRAY, menu_button_png, exit_game)]

menu_title = title_font.render("Game", True, LIGHT_GRAY)
menu_title_rect = menu_title.get_rect()
menu_title_rect.centerx = WINDOW.get_width() // 2
menu_title_rect.y = 100


# Uusi peli
new_game_buttons = [
Button(100, 100, "Class 1", menu_button_font, LIGHT_GRAY, menu_button_png, new_game),
Button(100, 200, "Class 2", menu_button_font, LIGHT_GRAY, menu_button_png, new_game),
Button(1100 - menu_button_png.get_width(), 650, "Play", menu_button_font, LIGHT_GRAY, menu_button_png, playing),
Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, main_menu)
]

# Latausvalikko
load_game_buttons = [
Button(1100 - menu_button_png.get_width(), 650, "Play", menu_button_font, LIGHT_GRAY, menu_button_png, playing),
Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, main_menu)
]

# Karttaeditori
map_editor_buttons = [
Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, main_menu)
]

# Peli käynnissä
playing_buttons = [
Button(50, 0, "Menu", menu_button_font, LIGHT_GRAY, menu_button_png, main_menu)
]


# Ikkunoiden piirto
def draw_main_menu():
    WINDOW.fill(BLACK)
    WINDOW.blit(menu_title, menu_title_rect)
    
    for button in main_menu_buttons:
        button.update()
        button.draw()

def draw_new_game():
    WINDOW.fill(BLACK)

    for button in new_game_buttons:
        button.update() 
        button.draw()

def draw_load_menu():
    WINDOW.fill(BLACK)

    for button in load_game_buttons:
        button.update()
        button.draw()

def draw_map_editor():
    WINDOW.fill(BLACK)

    for button in map_editor_buttons:
        button.update()
        button.draw()

def draw_playing():
    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, GRAY, (350, 50, 800, 700), width = 2)
    
    for button in playing_buttons:
        button.update()
        button.draw()
        

# Pääloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == "main_menu":
        draw_main_menu()

    elif game_state == "new_game":
        draw_new_game()

    elif game_state == "load_game":
        draw_load_menu()

    elif game_state == "playing":
        draw_playing()
    
    elif game_state == "map_editor":
        draw_map_editor()


    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()




