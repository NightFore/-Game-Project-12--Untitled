import pygame
import random
from Settings import *
from os import path
vec = pygame.math.Vector2

def init_sprite(sprite, game, dict, group=None, data=None, item=None, parent=None, variable=None):
    # Initialization -------------- #
    sprite.game = game
    sprite.groups = sprite.game.all_sprites, group
    sprite.data = data
    sprite.item = item
    sprite.parent = parent
    sprite.variable = variable
    pygame.sprite.Sprite.__init__(sprite, sprite.groups)

    # Dict ------------------------ #
    sprite.dict = dict
    sprite.object = sprite.dict[sprite.data][sprite.item]
    sprite.settings = sprite.dict["type"][sprite.object["type"]]

def init_rect(sprite):
    # Settings
    sprite.pos = sprite.object["pos"]
    sprite.size = sprite.settings["size"]
    sprite.center = sprite.settings["align"]
    sprite.surface = pygame.Surface(sprite.size)
    sprite.rect = sprite.game.align_rect(sprite.surface, sprite.pos[0], sprite.pos[1], "center")

    # Border
    sprite.border_size = sprite.settings["border_size"]
    sprite.border_color = sprite.settings["border_color"]
    sprite.surface_rect = (sprite.border_size[0], sprite.border_size[1], sprite.size[0] - 2*sprite.border_size[0], sprite.size[1] - 2*sprite.border_size[1])

def init_surface(surface, surface_rect, color, border_color=None):
    surface = surface.copy()
    if border_color is not None:
        surface.fill(border_color)
    pygame.draw.rect(surface, color, surface_rect)
    return surface



"""
    Sprite's update functions
"""
def update_time_dependent(sprite):
    if sprite.table:
        sprite.current_time += sprite.dt
        if sprite.current_time >= sprite.animation_time:
            if sprite.index == len(sprite.images)-1:
                sprite.loop += 1
            sprite.current_time = 0
            sprite.index = (sprite.index + 1) % len(sprite.images)
            sprite.image = sprite.images[sprite.index]
        if sprite.animation_loop and sprite.index == 0 and sprite.loop != 0:
            sprite.kill()
        sprite.image = pygame.transform.rotate(sprite.image, 0)


def update_center(sprite):
    if sprite.center:
        sprite.rect = sprite.image.get_rect()
        sprite.rect.center = sprite.pos


def update_bobbing(sprite):
    if sprite.bobbing:
        offset = BOB_RANGE * (sprite.tween(sprite.step / BOB_RANGE) - 0.5)
        sprite.rect.centery = sprite.pos.y + offset * sprite.dir
        sprite.step += BOB_SPEED
        if sprite.step > BOB_RANGE:
            sprite.step = 0
            sprite.dir *= -1



# Gameplay / Interface
def update_move(sprite):
    if sprite.vel == (0, 0):
        if not sprite.game.debug_mode:
            sprite.vel = vec(sprite.move_speed.elementwise() * sprite.range[0])
        else:
            sprite.vel = vec(sprite.debug_move_speed.elementwise() * sprite.range[0])
    if abs(sprite.pos_dt[0] + sprite.vel.x * sprite.dt) <= sprite.grid_dt[0] and abs(
            sprite.pos_dt[1] + sprite.vel.y * sprite.dt) <= sprite.grid_dt[1]:
        sprite.pos += sprite.vel * sprite.dt
        sprite.pos_dt += sprite.vel.x * sprite.dt, sprite.vel.y * sprite.dt
    else:
        sprite.grid_pos += sprite.range[0]
        sprite.pos = vec(sprite.pos - sprite.pos_dt + sprite.grid_dt.elementwise() * sprite.range[0])
        sprite.pos_dt = vec(0, 0)
        sprite.vel = vec(0, 0)
        del sprite.range[0]

# Miscellaneous
def load_file(path, image=False):
    file = []
    for file_name in os.listdir(path):
        if image:
            file.append(pygame.image.load(path + os.sep + file_name).convert_alpha())
        else:
            file.append(path + os.sep + file_name)
    return file


def load_image(image_path, image_directory):
    if isinstance(image_directory, list):
        images = []
        for image in image_directory:
            images.append(pygame.image.load(path.join(image_path, image)).convert_alpha())
        return images
    else:
        return pygame.image.load(path.join(image_path, image_directory)).convert_alpha()


def load_tile_table(filename, width, height, reverse, colorkey=(0, 0, 0)):
    image = pygame.image.load(filename).convert_alpha()
    image.set_colorkey(colorkey)
    image_width, image_height = image.get_size()
    tile_table = []
    if not reverse:
        for tile_y in range(int(image_height / height)):
            line = []
            tile_table.append(line)
            for tile_x in range(int(image_width / width)):
                rect = (tile_x * width, tile_y * height, width, height)
                line.append(image.subsurface(rect))
    else:
        for tile_x in range(int(image_width / width)):
            column = []
            tile_table.append(column)
            for tile_y in range(int(image_height / height)):
                rect = (tile_x * width, tile_y * height, width, height)
                column.append(image.subsurface(rect))
    return tile_table


def transparent_surface(width, height, color, border, colorkey=(0, 0, 0)):
    surface = pygame.Surface((width, height)).convert()
    surface.set_colorkey(colorkey)
    surface.fill(color)
    surface.fill(colorkey, surface.get_rect().inflate(-border, -border))
    return surface


def sort_list(list, var, reverse=False):
    if reverse:
        list.reverse()

    for i in range(len(list)):
        # Display list
        # print(list)

        if list[i] == var:
            cpt = 0
            while list[i + cpt] == var and i + cpt < len(list)-1:
                cpt += 1
            list[i] = list[i+cpt]
            list[i+cpt] = var

    if reverse:
        list.reverse()
