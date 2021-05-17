import pygame
from os import path

from Class import *

def main_menu(game, menu):
    for button in game.button_dict[menu]:
        Button(game, game.button_dict, game.buttons, data=menu, item=button)

    Entity(game, game.entity_dict, game.entities, data="data", item="item")


MENU_DICT = {
    "main_menu": main_menu
}
