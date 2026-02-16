from config import *
from ui import Button, Text


# Tietää tämänhetkisen tilan, piirtää ja päivittää
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


# Yleinen pelitilaluokka
class GameState:
    def __init__(self, game):
        self.game = game
        self.ui_elements = pygame.sprite.Group()
        self.centerx = WINDOW.get_width() // 2
        self.centery = WINDOW.get_height() // 2
    
    def handle_event(self, event):
        for element in self.ui_elements:
            element.handle_event(event)

    def update(self):
        self.ui_elements.update()

    def draw(self):
        WINDOW.fill(BLACK)
        self.ui_elements.draw(WINDOW)

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


# Kaikki pelitilat, peritään GameState luokka ja lisätään piirrettävät objektit
class MainMenu(GameState):
    def __init__(self, game):
        super().__init__(game)
        
        self.ui_elements.add(
            Button(self.centerx, self.centery - 100, 300, 200, "New Game", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.new_game),
            Button(self.centerx, self.centery, 300, 200, "Load Game", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.load_game),
            Button(self.centerx, self.centery + 100, 300, 200, "Map Editor", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.map_editor),
            Button(self.centerx, self.centery + 200, 300, 200, "Exit", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.exit_game),
            Text(self.centerx, self.centery - 300, "Game", title_font, LIGHT_GRAY)
        )

    
class NewGame(GameState):
    def __init__(self, game):
        super().__init__(game)
        
        self.ui_elements.add(
            Button(200, self.centery + 375, 300, 200, "Back", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.main_menu), 
            Button(WINDOW.get_width() - 200, self.centery + 375, 300, 200, "Play", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.playing)
        )


class LoadGame(GameState):
    def __init__(self, game):
        super().__init__(game)
        
        self.ui_elements.add(
            Button(200, self.centery + 375, 300, 200, "Back", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.main_menu), 
            Button(WINDOW.get_width() - 200, self.centery + 375, 300, 200, "Play", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.playing)
        )


class Playing(GameState):
    def __init__(self, game):
        super().__init__(game)
        
        self.ui_elements.add(
            Button(200, self.centery + 375, 300, 200, "Back", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.main_menu), 
            Button(WINDOW.get_width() - 200, self.centery + 375, 300, 200, "Play", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.playing)
        )


class MapEditor(GameState):
    def __init__(self, game):
        super().__init__(game)
        
        self.ui_elements.add(
            Button(200, self.centery + 375, 300, 200, "Back", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.main_menu), 
            Button(WINDOW.get_width() - 200, self.centery + 375, 300, 200, "Play", menu_button_font, LIGHT_GRAY, GRAY, RED, menu_button_png, self.playing)
        )


# Luodaan GameManager olio, joka pyörittää eri pelitiloja
game = GameManager()