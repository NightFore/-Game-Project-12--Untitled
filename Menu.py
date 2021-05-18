import pygame
from os import path

from Class import *
from Function import *

def init_menu(game, menu, ui=True, button=True, entity=True):
    if ui:
        update_ui(game, menu)
    if button:
        update_button(game, menu)
    if entity:
        update_entity(game, menu)

def clear_menu(game, ui=True, button=True, entity=True):
    if ui:
        for ui in game.uis:
            ui.kill()
    if button:
        for button in game.buttons:
            button.kill()
    if entity:
        for entity in game.entities:
            entity.kill()

def update_ui(game, menu):
    if menu in game.ui_dict:
        for ui in game.ui_dict[menu]:
            UI(game, game.ui_dict, game.uis, data=menu, item=ui)

def update_button(game, menu):
    if menu in game.button_dict:
        for button in game.button_dict[menu]:
            Button(game, game.button_dict, game.buttons, data=menu, item=button)

def update_entity(game, menu):
    if menu in game.entity_dict:
        for entity in game.entity_dict[menu]:
            Entity(game, game.entity_dict, game.entities, data=menu, item=entity)


def main_menu(game, menu):
    clear_menu(game)
    init_menu(game, menu)

def tutorial_menu(game, menu):
    clear_menu(game)
    init_menu(game, menu)

def level_menu(game, menu):
    clear_menu(game)
    init_menu(game, menu)

def pause_menu(game, menu):
    game.paused = not game.paused



MENU_DICT = {
    "main_menu": main_menu,
    "tutorial_menu": tutorial_menu,
    "level_menu": level_menu,
    "pause_menu": pause_menu,
}
