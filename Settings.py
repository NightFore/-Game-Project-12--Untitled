import pygame
from os import path

"""
    Settings
"""
project_title = "Untitled"
screen_size = WIDTH, HEIGHT = 1280, 720
FPS = 60
default_volume = 5

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
        "background_color": None,
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
            "center": True,
            "font": "menu", "font_color": WHITE,
            "inactive_color": LIGHT_SKY_BLUE, "active_color": DARK_SKY_BLUE, "border_color": BLACK, "border_size": 5,
            "sound_active": None, "sound_action": None}
    },

    # Main Menu --------------- #
    "main_menu": {
        "new_game":     {"rect": [640, 300, 280, 50], "type": "type_1", "text": "New Game"},
        "load":         {"rect": [640, 375, 280, 50], "type": "type_1", "text": "Load Game"},
        "options":      {"rect": [640, 450, 280, 50], "type": "type_1", "text": "Options"},
        "exit":         {"rect": [640, 525, 280, 50], "type": "type_1", "text": "Exit"}
    }
}