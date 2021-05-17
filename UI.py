import pygame
from os import path

from Class import *

def init_menu(game, menu, button=False, entity=False):
    if button:
        update_button(game, menu)
    if entity:
        update_entity(game, menu)

def clear_menu(game, button=False, entity=False):
    if button:
        for button in game.buttons:
            button.kill()
    if entity:
        for entity in game.entities:
            entity.kill()

def update_button(game, menu):
    for button in game.button_dict[menu]:
        Button(game, game.button_dict, game.buttons, data=menu, item=button)

def update_entity(game, menu):
    for entity in game.entity_dict[menu]:
        Entity(game, game.entity_dict, game.entities, data=menu, item=entity)


def main_menu(game, menu):
    clear_menu(game, button=True, entity=True)
    init_menu(game, menu, button=True, entity=True)



MENU_DICT = {
    "main_menu": main_menu,
}
