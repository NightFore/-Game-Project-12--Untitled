import pygame
import random
import pytweening as tween
from Settings import *
from Function import *
vec = pygame.math.Vector2

class Button(pygame.sprite.Sprite):
    def __init__(self, game, dict, group=None, object=None, action=None, variable=None):
        # Initialization -------------- #
        self.game = game
        self.groups = self.game.all_sprites, group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.object = object
        self.variable = variable
        self.action = action

        # Dict ------------------------ #
        self.dict = dict
        self.object = self.dict[object[0]][object[1]]
        self.settings = self.dict["type"][self.object["type"]]

        # Settings -------------------- #
        self.center = self.settings["center"]
        self.font = self.game.font_dict[self.settings["font"]]
        self.font_color = self.settings["font_color"]
        self.inactive_color = self.settings["inactive_color"]
        self.active_color = self.settings["active_color"]
        self.border_color = self.settings["border_color"]
        self.border_size = self.settings["border_size"]
        self.sound_active = self.settings["sound_active"]
        self.sound_action = self.settings["sound_action"]
        self.button_rect = self.object["rect"]
        self.text = self.object["text"]
        self.sound = False

        # Check ----------------------- #
        self.font_check = False

        # Surface --------------------- #
            # Inactive
        self.inactive = pygame.Surface((self.button_rect[2], self.button_rect[3]))
        self.inactive.fill(self.border_color)
        pygame.draw.rect(self.inactive, self.inactive_color, (self.border_size, self.border_size, self.button_rect[2] - self.border_size*2, self.button_rect[3] - self.border_size*2))

            # Active
        self.active = pygame.Surface((self.button_rect[2], self.button_rect[3]))
        self.active.fill(self.border_color)
        pygame.draw.rect(self.active, self.active_color, (self.border_size, self.border_size, self.button_rect[2] - self.border_size*2, self.button_rect[3] - self.border_size*2))

        # Rect ------------------------ #
        self.image = self.inactive
        self.rect = self.image.get_rect()
        if self.center:
            self.rect.center = (self.button_rect[0], self.button_rect[1])
        self.text_pos = self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2

    def update(self):
        if self.rect.collidepoint(self.game.mouse):
            self.image = self.active
            if self.sound_active is not None and not self.sound:
                pygame.mixer.Sound.play(self.sound_active)
                self.sound = True
            if self.game.click[1] and self.action is not None:
                if self.sound_action is not None:
                    pygame.mixer.Sound.play(self.sound_action)
                if self.variable is not None:
                    self.action(self.variable)
                else:
                    self.action()
        else:
            self.image = self.inactive
            self.sound = False

    def draw(self):
        self.game.gameDisplay.blit(self.image, self)
        if self.text is not None and self.font is not None:
            self.game.draw_text(self.text, self.font, self.font_color, self.text_pos, "center")
        elif not self.font_check:
            self.font_check = True
            print("Font not initialized, text: %s" % self.text)
