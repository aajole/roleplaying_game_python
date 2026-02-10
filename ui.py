import pygame
from config import *





class Button:
    
    def __init__(self, x, y, text, font, text_color, image, action):
        
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

        self.text = text
        self.action = action

        self.font = font
        self.text_color = text_color
        self.buttontext = self.font.render(text, True, text_color)

    
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
                self.text_color = GRAY

                # Hiiri pohjassa napin päällä
                if mouse_pressed:
                    self.text_color = RED

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
                self.text_color = LIGHT_GRAY

        else:
            self.pressed = False
            self.text_color = LIGHT_GRAY
            
        self.buttontext = self.font.render(self.text, True, self.text_color)

    
    # Nappien piirto
    def draw(self):
        WINDOW.blit(self.image, self.rect)
        WINDOW.blit(self.buttontext, 
                    (self.rect.centerx - self.buttontext.get_width() // 2,
                    self.rect.centery - self.buttontext.get_height() // 2))
        





