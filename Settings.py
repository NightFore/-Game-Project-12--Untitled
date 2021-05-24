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
GREEN_2 = 0, 200, 0
GREEN_3 = 0, 145, 0
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
        "new_game": {"type": "type_1", "pos": (640, 300), "text": "New Game", "variable": "tutorial_menu", "action": "sprite.game.update_menu"},
        "load_game": {"type": "type_1", "pos": (640, 375), "text": "Load Game"},
        "options": {"type": "type_1", "pos": (640, 450), "text": "Options", "action": "sprite.kill"},
        "exit": {"type": "type_1", "pos": (640, 525), "text": "Exit", "action": "sprite.game.quit_game"},
    },
    "tutorial_menu": {
        "next": {"type": "type_2", "pos": (625, 645), "text": "←", "variable": "main_menu", "action": "sprite.game.update_menu"},
        "return": {"type": "type_2", "pos": (1185, 645), "text": "→", "variable": "level_menu", "action": "sprite.game.update_menu"},
    },
    "level_menu": {
        "pause": {"type": "type_3", "pos": (1260, 20), "text": "Pause", "variable": "pause_menu", "action": "sprite.game.update_menu"},
    },

}

ENTITY_DICT = {
    "type": {
        "player": {
            "align": "center", "size": (50, 50),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": BLUE,
            "move_speed": (750, 750)
        },
        "type_1": {
            "align": "center", "size": (50, 50),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": RED,
            "move_speed": (0, 150)
        },
        "type_2": {
            "align": "center", "size": (50, 50),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": RED,
            "move_speed": (0, 200)
        },
    },

    "level_menu": {
        "player": {"type": "player", "pos": (640, 360), "variable": "player"},
        "entity_1": {"type": "type_1", "pos": (0, 0)},
        "entity_2": {"type": "type_2", "pos": (0, 0)},
    },
}

WALL_DICT = {
    "type": {
        "wall_1_horizontal": {
            "align": "nw", "size": (600, 60),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": GREEN,
        },
        "wall_2_horizontal": {
            "align": "nw", "size": (600, 75),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": GREEN_2,
        },
        "wall_3_horizontal": {
            "align": "nw", "size": (450, 50),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": GREEN_3,
        },
        "wall_1_vertical": {
            "align": "nw", "size": (340, 600),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": GREEN,
        },
        "wall_2_vertical": {
            "align": "nw", "size": (75, 600),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": GREEN_2,
        },
        "wall_3_vertical": {
            "align": "nw", "size": (50, 450),
            "border": False, "border_size": (0, 0), "border_color": None,
            "color": GREEN_3,
        },
    },

    "level_menu": {
        "wall_1_n": {"difficulty": 1, "type": "wall_1_horizontal", "pos": (340, 0)},
        "wall_1_s": {"difficulty": 1, "type": "wall_1_horizontal", "pos": (340, 660)},
        "wall_1_w": {"difficulty": 1, "type": "wall_1_vertical", "pos": (0, 60)},
        "wall_1_e": {"difficulty": 1, "type": "wall_1_vertical", "pos": (940, 60)},
        "wall_2_n": {"difficulty": 2, "type": "wall_2_horizontal", "pos": (340, 60)},
        "wall_2_s": {"difficulty": 2, "type": "wall_2_horizontal", "pos": (340, 585)},
        "wall_2_w": {"difficulty": 2, "type": "wall_2_vertical", "pos": (340, 60)},
        "wall_2_e": {"difficulty": 2, "type": "wall_2_vertical", "pos": (865, 60)},
        "wall_3_n": {"difficulty": 3, "type": "wall_3_horizontal", "pos": (415, 135)},
        "wall_3_s": {"difficulty": 3, "type": "wall_3_horizontal", "pos": (415, 535)},
        "wall_3_w": {"difficulty": 3, "type": "wall_3_vertical", "pos": (415, 135)},
        "wall_3_e": {"difficulty": 3, "type": "wall_3_vertical", "pos": (815, 135)},
    },
}