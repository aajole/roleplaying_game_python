import pygame
from config import *
from ui import Button


class GameState:
    def __init__(self):
        self.running = True
        self.current_state = None

    def switch_state(self, new_state):
        self.current_state = new_state

    def update(self):
        self.current_state.update()
        
    def draw(self):
        self.current_state.draw()


class MainMenu:
    def __init__(self, game):
        button_x = WINDOW.get_width() // 2 - menu_button_png.get_width() // 2
        self.game = game
        self.ui_elements = [
        Button(button_x, 250, "New Game", menu_button_font, LIGHT_GRAY, menu_button_png, self.new_game),
        Button(button_x, 350, "Load Game", menu_button_font, LIGHT_GRAY, menu_button_png, self.load_game),
        Button(button_x, 450, "Map Editor", menu_button_font, LIGHT_GRAY, menu_button_png, self.map_editor),
        Button(button_x, 550, "Exit", menu_button_font, LIGHT_GRAY, menu_button_png, self.exit_game)
        ]
        
    def new_game(self):
        self.game.switch_state(NewGame(self.game))

    def load_game(self):
        self.game.switch_state(LoadGame(self.game))

    def map_editor(self):
        self.game.switch_state(MapEditor(self.game))

    def exit_game(self):
        self.game.running = False

    def update(self):
        
        for ui_element in self.ui_elements:
            ui_element.update()

    def draw(self):
        menu_title = title_font.render("Game", True, LIGHT_GRAY)
        menu_title_rect = menu_title.get_rect()
        menu_title_rect.centerx = WINDOW.get_width() // 2
        menu_title_rect.y = 100
        
        WINDOW.fill(BLACK)
        WINDOW.blit(menu_title, menu_title_rect)
        
        for ui_element in self.ui_elements:
            ui_element.draw()

    
class NewGame:
    def __init__(self, game):
        self.game = game
        self.ui_elements = [
        Button(100, 100, "Class 1", menu_button_font, LIGHT_GRAY, menu_button_png, self.back),
        Button(100, 200, "Class 2", menu_button_font, LIGHT_GRAY, menu_button_png, self.back),
        Button(1100 - menu_button_png.get_width(), 650, "Play", menu_button_font, LIGHT_GRAY, menu_button_png, self.playing),
        Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, self.back)
        ]
        
    def playing(self):
        self.game.switch_state(Playing(self.game))

    def back(self):
        self.game.switch_state(MainMenu(self.game))
    
    def update(self):
        for ui_element in self.ui_elements:
            ui_element.update()

    def draw(self):
        WINDOW.fill(BLACK)
        
        for ui_element in self.ui_elements:
            ui_element.draw()
        

class LoadGame:
    def __init__(self, game):
        self.game = game
        self.ui_elements = [
        Button(1100 - menu_button_png.get_width(), 650, "Play", menu_button_font, LIGHT_GRAY, menu_button_png, self.playing),
        Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, self.back)
        ]

    def playing(self):
        self.game.switch_state(Playing(self.game))

    def back(self):
        self.game.switch_state(MainMenu(self.game))

    def update(self):
        
        for ui_element in self.ui_elements:
            ui_element.update()

    def draw(self):
        WINDOW.fill(BLACK)
        
        for ui_element in self.ui_elements:
            ui_element.draw()


class Playing:
    def __init__(self, game):
        self.game  = game
        self.ui_elements = [
        Button(50, 0, "Menu", menu_button_font, LIGHT_GRAY, menu_button_png, self.main_menu)
        ]

    def main_menu(self):
        self.game.switch_state(Playing(self.game))

    def update(self):
        
        for ui_element in self.ui_elements:
            ui_element.update()

    def draw(self):
        WINDOW.fill(BLACK)
        
        for ui_element in self.ui_elements:
            ui_element.draw()


class MapEditor:
    def __init__(self, game):
        self.game = game
        self.ui_elements = [
        Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, self.back)
        ]

    def back(self):
        self.game.switch_state(MainMenu(self.game))

    def update(self):
        
        for ui_element in self.ui_elements:
            ui_element.update()

    def draw(self):
        WINDOW.fill(BLACK)
        
        for ui_element in self.ui_elements:
            ui_element.draw()


game = GameState()
game.switch_state(MainMenu(game))