# hud.py
import pygame as pg


def load_images():
    dorm = pg.image.load("assets/graphics/dorm.png").convert_alpha()
    tree = pg.image.load("assets/graphics/tree.png").convert_alpha()
    rock = pg.image.load("assets/graphics/rock.png").convert_alpha()
    rock2 = pg.image.load("assets/graphics/rock2.png").convert_alpha()

    return {"dorm": dorm, "tree": tree, "rock": rock, "rock2": rock2}


class Hud:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.hud_color = (118, 147, 173, 175)

        # resources hud
        self.resources_hud = pg.Surface((self.width, height * 0.04), pg.SRCALPHA).convert_alpha()
        self.resources_hud.fill(self.hud_color)

        # building hud
        self.build_hud = pg.Surface((self.width * 0.15, height * 0.25), pg.SRCALPHA).convert_alpha()
        self.build_hud.fill(self.hud_color)

        # select hud
        self.select_hud = pg.Surface((self.width * 0.3, height * 0.2), pg.SRCALPHA).convert_alpha()
        self.select_hud.fill(self.hud_color)

        self.images = load_images()
        self.tiles = self.create_build_hud()

    def create_build_hud(self):
        render_pos = [self.width * 0.84 + 10, self.height * 0.74 + 10]

        object_width = self.build_hud.get_width() // 5

        tiles = []
        for img_name, img in self.images.items():
            pos = render_pos.copy()
            img_tmp = img.copy()
            img_scale = self.img_scale(img_tmp, w=object_width)
            rect = img_scale.get_rect(topleft=pos)

            tiles.append({
                "name": img_name,
                "icon": img_scale,
                "img": self.images[img_name],
                "rect": rect
            })

            render_pos[0] += img_scale.get_width() + 10

        return tiles

    def draw_hud(self, screen):
        # resources hud
        screen.blit(self.resources_hud, (0, 0))

        # building hud
        screen.blit(self.build_hud, (self.width * 0.84, self.height * 0.74))

        # select hud
        screen.blit(self.select_hud, (self.width * 0.35, self.height * 0.79))

        for tile in self.tiles:
            screen.blit(tile["icon"], tile["rect"].topleft)

    def img_scale(self, img, w=None, h=None):
        if w is None and h is None:
            pass
        elif h is None:
            scale = w / img.get_width()
            h = img.get_height() * scale
            image = pg.transform.scale(img, (int(w), int(h)))
        elif w is None:
            scale = h / img.get_height()
            w = img.get_width() * scale
            image = pg.transform.scale(img, (int(w), int(h)))
        else:
            image = pg.transform.scale(img, (int(w), int(h)))

        return image
