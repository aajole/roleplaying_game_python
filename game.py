import pygame


pygame.init()


# Ikkuna ja FPS
window = pygame.display.set_mode((1200, 800), 0, 0)
pygame.display.set_caption("Peli")
clock = pygame.time.Clock()
FPS = 60


# Tilat
game_state = "main_menu"
running = True


# Värit
green = (0, 255, 0)
dark_gray = (50, 50, 50)
gray = (120, 120, 120)
black = (0, 0, 0)
white = (255, 255, 255)
light_gray = (210, 210, 210)
red = (170, 0, 0)


# Fontit ja kuvat
menu_button_png = pygame.image.load("buttons/button_background.png").convert_alpha()
menu_button_font = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 40)
title_font = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 100)
text_font = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 20)

class Button:
    
    def __init__(self, x, y, text, image, action):
        
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

        self.text = text
        self.action = action

        self.text_color = light_gray
        self.buttontext = menu_button_font.render(text, True, light_gray)

    
    def update(self):
        
        # Kursorin ja klikkauksen seuranta
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        # Onko hiiri napin päällä
        if self.rect.collidepoint(mouse_pos):
            x = mouse_pos[0] - self.rect.x
            y = mouse_pos[1] - self.rect.y
            
            # Tarkistetaan, että hiiri on näkyvän pikselin päällä
            if self.image.get_at((x, y)).a > 0:
                self.text_color = gray

                # Hiiri pohjassa napin päällä
                if mouse_pressed:
                    self.text_color = red

                    if not getattr(self, "pressed", False):
                        self.pressed = True

                # Hiiri vapautetaan
                else:
                    if getattr(self, "pressed", False):
                        self.pressed = False

                        if self.action:
                            self.action()

            # Hiiri pois napin päältä
            else:
                self.pressed = False
                self.text_color = light_gray

        else:
            self.pressed = False
            self.text_color = light_gray
            
        self.buttontext = menu_button_font.render(self.text, True, self.text_color)

    
    # Nappien piirto
    def draw(self):
        window.blit(self.image, self.rect)
        window.blit(self.buttontext, 
                    (self.rect.centerx - self.buttontext.get_width() // 2,
                    self.rect.centery - self.buttontext.get_height() // 2))


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
button_x = window.get_width() // 2 - menu_button_png.get_width() // 2
main_menu_buttons = [
Button(button_x, 250, "New Game", menu_button_png, new_game),
Button(button_x, 350, "Load Game", menu_button_png, load_game),
Button(button_x, 450, "Map Editor", menu_button_png, map_editor),
Button(button_x, 550, "Exit", menu_button_png, exit_game)]

menu_title = title_font.render("Joku Peli", True, light_gray)
menu_title_rect = menu_title.get_rect()
menu_title_rect.centerx = window.get_width() // 2
menu_title_rect.y = 100


# Uusi peli
new_game_buttons = [
Button(100, 100, "Class 1", menu_button_png, new_game),
Button(100, 200, "Class 2", menu_button_png, new_game),
Button(1100 - menu_button_png.get_width(), 650, "Play", menu_button_png, playing),
Button(100, 650, "Back", menu_button_png, main_menu)
]


# Latausvalikko
load_game_buttons = [
Button(1100 - menu_button_png.get_width(), 650, "Play", menu_button_png, playing),
Button(100, 650, "Back", menu_button_png, main_menu)
]


# Karttaeditori
map_editor_buttons = [
Button(100, 650, "Back", menu_button_png, main_menu)
]

# Peli käynnissä
playing_buttons = [
Button(50, 0, "Menu", menu_button_png, main_menu)
]






# Ikkunoiden piirto
def draw_main_menu():
    window.fill(black)
    window.blit(menu_title, menu_title_rect)
    
    for button in main_menu_buttons:
        button.update()
        button.draw()

def draw_new_game():
    window.fill(black)

    for button in new_game_buttons:
        button.update() 
        button.draw()

def draw_load_menu():
    window.fill(black)

    for button in load_game_buttons:
        button.update()
        button.draw()

def draw_map_editor():
    window.fill(black)

    for button in map_editor_buttons:
        button.update()
        button.draw()

def draw_playing():
    window.fill(black)
    pygame.draw.rect(window, gray, (350, 50, 800, 700), width = 2)
    
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
    clock.tick(FPS)

pygame.quit()




