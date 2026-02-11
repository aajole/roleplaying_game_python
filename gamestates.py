import pygame
from config import *
from ui import Button


class GameManager:
    def __init__(self):
        self.running = True
        
        self.main_menu = MainMenu(self)
        self.new_game = NewGame(self)
        self.load_game = LoadGame(self)
        self.playing = Playing(self)
        self.map_editor = MapEditor(self)

        self.current_state = self.main_menu

    def switch_state(self, new_state):
        self.current_state = new_state

    def update(self):
        self.current_state.update()
        
    def draw(self):
        self.current_state.draw()


class GameState:
    def __init__(self, game):
        self.game = game
    
    def update(self):
        for ui_element in self.ui_elements:
            ui_element.update()

    def draw(self):
        WINDOW.fill(BLACK)
        
        for ui_element in self.ui_elements:
            ui_element.draw()

    def main_menu(self):
        self.game.switch_state(self.game.main_menu)

    def new_game(self):
        self.game.switch_state(self.game.new_game)

    def load_game(self):
        self.game.switch_state(self.game.load_game)

    def map_editor(self):
        self.game.switch_state(self.game.map_editor)

    def playing(self):
        self.game.switch_state(self.game.playing)

    def exit_game(self):
        self.game.running = False


class MainMenu(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.button_x = WINDOW.get_width() // 2 - menu_button_png.get_width() // 2
        self.ui_elements = [
        Button(self.button_x, 250, "New Game", menu_button_font, LIGHT_GRAY, menu_button_png, self.new_game),
        Button(self.button_x, 350, "Load Game", menu_button_font, LIGHT_GRAY, menu_button_png, self.load_game),
        Button(self.button_x, 450, "Map Editor", menu_button_font, LIGHT_GRAY, menu_button_png, self.map_editor),
        Button(self.button_x, 550, "Exit", menu_button_font, LIGHT_GRAY, menu_button_png, self.exit_game)
        ]

    def draw(self):
        menu_title = title_font.render("Game", True, LIGHT_GRAY)
        menu_title_rect = menu_title.get_rect()
        menu_title_rect.centerx = WINDOW.get_width() // 2
        menu_title_rect.y = 100
        
        WINDOW.fill(BLACK)
        WINDOW.blit(menu_title, menu_title_rect)
        
        for ui_element in self.ui_elements:
            ui_element.draw()

    
class NewGame(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.ui_elements = [
        Button(100, 100, "Class 1", menu_button_font, LIGHT_GRAY, menu_button_png, self.main_menu),
        Button(100, 200, "Class 2", menu_button_font, LIGHT_GRAY, menu_button_png, self.main_menu),
        Button(1100 - menu_button_png.get_width(), 650, "Play", menu_button_font, LIGHT_GRAY, menu_button_png, self.playing),
        Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, self.main_menu)
        ]


class LoadGame(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.ui_elements = [
        Button(1100 - menu_button_png.get_width(), 650, "Play", menu_button_font, LIGHT_GRAY, menu_button_png, self.playing),
        Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, self.main_menu)
        ]


class Playing(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.ui_elements = [
        Button(50, 0, "Menu", menu_button_font, LIGHT_GRAY, menu_button_png, self.main_menu)
        ]


class MapEditor(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.ui_elements = [
        Button(100, 650, "Back", menu_button_font, LIGHT_GRAY, menu_button_png, self.main_menu)
        ]

game = GameManager()