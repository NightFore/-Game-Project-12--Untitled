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

BUTTON_DICT = {
    # Type  ------------------- #
    "type": {
        "type_1": {
            "align": "center", "size": (280, 50),
            "border": True, "border_size": (5, 5), "border_color": BLACK,
            "font": "menu", "font_color": WHITE,
            "inactive_color": LIGHT_SKY_BLUE, "active_color": DARK_SKY_BLUE,
            "sound_active": None, "sound_action": None}
    },

    # Main Menu --------------- #
    "main_menu": {
        "button_1": {"type": "type_1", "pos": (640, 300), "text": "New Game", "variable": None, "action": "None"},
        "button_2": {"type": "type_1", "pos": (640, 375), "text": "Load Game", "variable": None, "action": "None"},
        "button_3": {"type": "type_1", "pos": (640, 450), "text": "Options", "variable": None, "action": "self.kill"},
        "button_4": {"type": "type_1", "pos": (640, 525), "text": "Exit", "variable": None, "action": "self.game.quit_game"}
    }
}

ENTITY_DICT = {
    "type": {
        "type_1": {
            "align": "center", "size": (50, 50),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": RED
        }
    },

    "main_menu": {
        "item": {"type": "type_1", "pos": (150, 125)}
    }
}

