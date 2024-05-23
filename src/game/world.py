import pygame as pg
import random
import noise
from src.game.settings import TILE_SIZE


def load_images():
    block = pg.image.load("assets/graphics/block.png").convert_alpha()
    tree = pg.image.load("assets/graphics/tree.png").convert_alpha()
    rock = pg.image.load("assets/graphics/rock.png").convert_alpha()
    rock2 = pg.image.load("assets/graphics/rock2.png").convert_alpha()
    puddle = pg.image.load("assets/graphics/puddle.png").convert_alpha()
    dorm = pg.image.load("assets/graphics/dorm.png").convert_alpha()

    return {"block": block, "tree": tree, "rock": rock, "rock2": rock2, "puddle": puddle, "dorm": dorm}


class World:
    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.perlin_scale = grid_length_x / 2

        self.grass_tiles = pg.Surface(
            (grid_length_x * TILE_SIZE * 2,
             grid_length_y * TILE_SIZE + 2 * TILE_SIZE)
        ).convert_alpha()
        self.tiles = load_images()
        self.world = self.create_world()

    def create_world(self):
        world = []

        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

                render_pos = world_tile["render_pos"]
                self.grass_tiles.blit(self.tiles["block"],
                                      (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))

        return world

    def grid_to_world(self, grid_x, grid_y):
        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]

        iso_polygon = [self.cart_to_iso(x, y) for x, y in rect]

        min_x = min([x for x, y in iso_polygon])
        min_y = min([y for x, y in iso_polygon])

        r = random.randint(1, 100)
        perlin = 100 * noise.pnoise2(grid_x / self.perlin_scale, grid_y / self.perlin_scale)

        if perlin >= 15 or perlin <= -35:
            tile = "tree"
        else:
            if r <= 1:
                tile = "tree"
            elif r == 2:
                tile = "rock"
            elif r == 3:
                tile = "rock2"
            elif r == 4:
                tile = "puddle"
            else:
                tile = ""

        out = {
            "grid": [grid_x, grid_y],
            "cartesian_rect": rect,
            "iso_polygon": iso_polygon,
            "render_pos": [min_x, min_y],
            "tile": tile
        }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y) / 2
        return iso_x, iso_y
