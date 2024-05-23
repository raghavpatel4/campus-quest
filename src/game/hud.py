# hud.py
import pygame as pg

class Hud:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.hud_color = (190, 155, 93, 175)

        # resources hud
        self.resources_hud = pg.Surface((self.width, height * 0.04), pg.SRCALPHA).convert_alpha()
        self.resources_hud.fill(self.hud_color)

        # building hud
        self.build_hud = pg.Surface((self.width * 0.15, height * 0.25), pg.SRCALPHA).convert_alpha()
        self.build_hud.fill(self.hud_color)

        # select hud
        self.select_hud = pg.Surface((self.width * 0.3, height * 0.2), pg.SRCALPHA).convert_alpha()
        self.select_hud.fill(self.hud_color)

    def draw_hud(self, screen):
        screen.blit(self.resources_hud, (0, 0))
        screen.blit(self.build_hud, (self.width * 0.84, self.height * 0.74))
        screen.blit(self.select_hud, (self.width * 0.35, self.height * 0.79))