import pygame
from config import *


# Yleinen UI luokka
class UIElement(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, background):
        super().__init__()
        
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.background = background
        self.visible = True
        self.enabled = True
        self._render_background()

    def _render_background(self):
        self.image.fill((0, 0, 0, 0))
        
        if isinstance(self.background, pygame.Surface):
            background = pygame.transform.scale(self.background, (self.rect.width, self.rect.height))
            self.image.blit(background, (0, 0))
        
        elif isinstance(self.background, tuple):
            self.image.fill(self.background)

    def set_background(self, background):
        self.background = background
        self._render_background()


# Nappi keskitetyllä tekstillä
class Button(UIElement):
    def __init__(self, x, y, width, height, text, font, default_text_color, hover_text_color, click_text_color, background, action):
        super().__init__(x, y, width, height, background)

        self.text = text
        self.font = font
        self.default_text_color = default_text_color
        self.hover_text_color = hover_text_color
        self.click_text_color = click_text_color
        self.text_color = self.default_text_color

        self.action = action
        self.hovered = False
        self.pressed = False
        self.mask = pygame.mask.from_surface(self.image)

        self._render_text()

    def _render_text(self):
        self._render_background()

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.image.blit(text_surface, text_rect)


    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0] - self.rect.x
        y = mouse_pos[1] - self.rect.y

        if 0 <= x < self.rect.width and 0 <= y < self.rect.height:
            self.hovered = self.mask.get_at((x, y))
        
        else:
            self.hovered = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1 and self.hovered:
                self.pressed = True
                self.text_color = self.click_text_color

        elif event.type == pygame.MOUSEBUTTONUP:
            
            if event.button == 1 and self.pressed:
                
                if self.hovered:
                    self.action()
                    self.hovered = False

                self.pressed = False

    def update(self):
       
        if not self.pressed:
            
            if self.hovered:
                self.text_color = self.hover_text_color
            
            else:
                self.text_color = self.default_text_color

        self._render_text()


class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, text, font, text_color):
        super().__init__()

        self.x = x
        self.y = y
        self.text = text
        self.text_color = text_color
        self.font = font
        self._render_text()

    def _render_text(self):
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        WINDOW.blit(self.image, self.rect)

    def handle_event(self, event):
        pass


    def update(self):
        self._render_text()