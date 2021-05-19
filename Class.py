import pygame
import random
import pytweening as tween
from Settings import *
from Function import *
vec = pygame.math.Vector2


class UI(pygame.sprite.Sprite):
    def __init__(self, game, dict, group=None, data=None, item=None, parent=None, variable=None, action=None):
        init_sprite(self, game, dict, group, data, item, parent, variable, action)
        init_rect(self)
        self.surface = init_surface(self.surface, self.surface_rect, self.settings["color"], border_color=self.border_color)

        # Font Settings --------------- #
        self.text = self.object["text"]
        self.text_pos = self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2
        self.font = self.game.font_dict[self.settings["font"]]
        self.font_color = self.settings["font_color"]

        # Check ----------------------- #
        self.font_check = False

    def draw(self):
        self.game.gameDisplay.blit(self.surface, self.rect)
        if self.text is not None:
            if self.font is not None:
                self.game.draw_text(self.text, self.font, self.font_color, self.text_pos, "center")
            elif not self.font_check:
                self.font_check = True
                print("Font not initialized, text: %s" % self.text)

    def update(self):
        pass

class Button(pygame.sprite.Sprite):
    def __init__(self, game, dict, group=None, data=None, item=None, parent=None, variable=None, action=None):
        init_sprite(self, game, dict, group, data, item, parent, variable, action)
        init_rect(self)

        # Surface --------------------- #
        self.inactive_surface = init_surface(self.surface, self.surface_rect, self.settings["inactive_color"], border_color=self.border_color)
        self.active_surface = init_surface(self.surface, self.surface_rect, self.settings["active_color"], border_color=self.border_color)

        # Font Settings --------------- #
        self.text = self.object["text"]
        self.text_pos = self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2
        self.font = self.game.font_dict[self.settings["font"]]
        self.font_color = self.settings["font_color"]

        # Sound Settings -------------- #
        self.sound_active = self.settings["sound_active"]
        self.sound_action = self.settings["sound_action"]

        # Check ----------------------- #
        self.font_check = False
        self.sound_check = False

    def draw(self):
        self.game.gameDisplay.blit(self.surface, self.rect)
        if self.text is not None:
            if self.font is not None:
                self.game.draw_text(self.text, self.font, self.font_color, self.text_pos, "center")
            elif not self.font_check:
                self.font_check = True
                print("Font not initialized, text: %s" % self.text)

    def update(self):
        if self.rect.collidepoint(self.game.mouse):
            self.surface = self.active_surface
            if self.sound_active is not None and not self.sound:
                pygame.mixer.Sound.play(self.sound_active)
                self.sound_check = True
            if self.game.click[1] and self.action is not None:
                if self.sound_action is not None:
                    pygame.mixer.Sound.play(self.sound_action)
                if self.variable is not None:
                    self.action(self.variable)
                else:
                    self.action()
        else:
            self.surface = self.inactive_surface
            self.sound_check = False




class Entity(pygame.sprite.Sprite):
    def __init__(self, game, dict, group=None, data=None, item=None, parent=None, variable=None, action=None):
        init_sprite(self, game, dict, group, data, item, parent, variable, action)
        init_rect(self)
        self.inactive_surface = init_surface(self.surface, self.surface_rect, self.settings["color"])
        self.init_move()

    def draw(self):
        self.game.gameDisplay.blit(self.inactive_surface, self.rect)

    def update(self):
        self.update_move()

    def init_move(self):
        self.pos = vec(self.object["pos"][:])
        self.pos_dt = vec(0, 0)
        self.vel = vec(0, 0)
        self.move_speed = vec(self.settings["move_speed"])

    def update_move(self):
        if self.variable == "player":
            keys = pygame.key.get_pressed()
            move = [0, 0]
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                move[1] = -1
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                move[1] = 1
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                move[0] = -1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                move[0] = 1
            self.vel = vec(self.move_speed.elementwise() * move)
        elif self.vel == (0, 0):
            self.vel = self.move_speed
        self.pos += self.vel * self.dt
        self.pos_dt += self.vel.x * self.dt, self.vel.y * self.dt
        self.rect = self.game.align_rect(self.surface, int(self.pos[0]), int(self.pos[1]), self.center)




class Wall(pygame.sprite.Sprite):
    def __init__(self, game, dict, group=None, data=None, item=None, parent=None, variable=None, action=None):
        init_sprite(self, game, dict, group, data, item, parent, variable, action)
        init_rect(self)
        self.inactive_surface = init_surface(self.surface, self.surface_rect, self.settings["color"])

    def draw(self):
        self.game.gameDisplay.blit(self.inactive_surface, self.rect)

    def update(self):
        pass
