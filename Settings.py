import pygame
from os import path

"""
    Settings
"""
project_title = "Untitled"
screen_size = WIDTH, HEIGHT = 1280, 720
FPS = 60
default_volume = 100

"""
    Colors
"""
BLACK = 0, 0, 0
WHITE = 255, 255, 255

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

YELLOW = 255, 255, 0
MAGENTA = 255, 0, 255
CYAN = 0, 255, 255

LIGHT_SKY_BLUE = 140, 205, 245
DARK_SKY_BLUE = 15, 160, 240

"""
    Game Settings
"""
GAME_DICT = {
    "background": {
        "background_image": None,
        "background_color": DARK_SKY_BLUE,
    },

    "HUD": {

    },

    "font": {

    },

    "color": {
    }
}

MUSIC_DICT = {
    "main_menu": "PerituneMaterial_Whisper_loop.ogg"
}

FONT_DICT = {
    "menu": {"ttf": "LiberationSerif-Regular.ttf", "size": 40}
}

UI_DICT = {
    # Type  ------------------- #
    "type": {
        "type_1": {
            "align": "nw", "size": (500, 680),
            "border": True, "border_size": (5, 5), "border_color": BLACK,
            "font": "menu", "font_color": WHITE,
            "color": LIGHT_SKY_BLUE,
            "sound_active": None, "sound_action": None},
        "type_2": {
            "align": "nw", "size": (710, 680),
            "border": True, "border_size": (5, 5), "border_color": BLACK,
            "font": "menu", "font_color": WHITE,
            "color": LIGHT_SKY_BLUE,
            "sound_active": None, "sound_action": None},
        "type_3": {
            "align": "nw", "size": (710, 680),
            "border": True, "border_size": (5, 5), "border_color": BLACK,
            "font": "menu", "font_color": WHITE, "font_align": "w", "font_delay": (20, ),
            "color": LIGHT_SKY_BLUE,
            "sound_active": None, "sound_action": None},
    },

    # Menu -------------------- #
    "main_menu": {},
    "tutorial_menu": {
        "ui_1": {"type": "type_1", "pos": (25, 20), "text": None, "variable": None, "action": "None"},
        "ui_2": {"type": "type_2", "pos": (550, 20), "text": None, "variable": None, "action": "None"},
    },
}

BUTTON_DICT = {
    # Type  ------------------- #
    "type": {
        "type_1": {
            "align": "center", "size": (280, 50),
            "border": True, "border_size": (5, 5), "border_color": BLACK,
            "font": "menu", "font_color": WHITE,
            "inactive_color": LIGHT_SKY_BLUE, "active_color": DARK_SKY_BLUE,
            "sound_active": None, "sound_action": None},
        "type_2": {
            "align": "center", "size": (100, 70),
            "border": True, "border_size": (5, 5), "border_color": BLACK,
            "font": "menu", "font_color": WHITE,
            "inactive_color": LIGHT_SKY_BLUE, "active_color": DARK_SKY_BLUE,
            "sound_active": None, "sound_action": None},
        "type_3": {
            "align": "ne", "size": (120, 50),
            "border": True, "border_size": (5, 5), "border_color": BLACK,
            "font": "menu", "font_color": WHITE,
            "inactive_color": LIGHT_SKY_BLUE, "active_color": DARK_SKY_BLUE,
            "sound_active": None, "sound_action": None},
    },

    # Menu -------------------- #
    "main_menu": {
        "new_game": {"type": "type_1", "pos": (640, 300), "text": "New Game", "variable": "tutorial_menu", "action": "self.game.update_menu"},
        "load_game": {"type": "type_1", "pos": (640, 375), "text": "Load Game"},
        "options": {"type": "type_1", "pos": (640, 450), "text": "Options", "action": "self.kill"},
        "exit": {"type": "type_1", "pos": (640, 525), "text": "Exit", "action": "self.game.quit_game"},
    },
    "tutorial_menu": {
        "next": {"type": "type_2", "pos": (625, 645), "text": "←", "variable": "main_menu", "action": "self.game.update_menu"},
        "return": {"type": "type_2", "pos": (1185, 645), "text": "→", "variable": "level_menu", "action": "self.game.update_menu"},
    },
    "level_menu": {
        "pause": {"type": "type_3", "pos": (1260, 20), "text": "Pause", "variable": "pause_menu", "action": "self.game.update_menu"},
    },

}

ENTITY_DICT = {
    "type": {
        "type_player": {
            "align": "center", "size": (50, 50),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": BLUE
        },
        "type_1": {
            "align": "center", "size": (50, 50),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": RED
        },
    },

    "main_menu": {
        "item": {"type": "type_1", "pos": (150, 125)}
    },

    "level_menu": {
        "player": {"type": "type_player", "pos": (640, 360), "variable": "player"}
    },
}

