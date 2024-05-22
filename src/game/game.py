import pygame as pg
import sys

from game.camera import Camera
from src.game.world import World
from src.game.settings import TILE_SIZE
from src.game.utils import draw_fps


class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # world
        self.world = World(50, 50, self.width, self.height)

        # camera
        self.camera = Camera(self.width, self.height, self.world)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        self.camera.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.world.grass_tiles, (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                # Draw the cartesian grid
                # sq = self.world.world[x][y]["cartesian_rect"]
                # rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                # pg.draw.rect(self.screen, (255, 255, 255), rect, 1)

                render_pos = self.world.world[x][y]["render_pos"]

                tile = self.world.world[x][y]["tile"]
                if tile != "":
                    self.screen.blit(self.world.tiles[tile],
                                     (render_pos[0] + self.world.grass_tiles.get_width() / 2 + self.camera.scroll.x,
                                      render_pos[1] - (self.world.tiles[tile].get_height() - TILE_SIZE) + self.camera.scroll.y))

                # Draw the isometric grid
                # p = self.world.world[x][y]["iso_polygon"]
                # Offset the polygon to the center of the screen
                # p = [(x + self.width / 2, y + self.height / 4) for x, y in p]
                # pg.draw.polygon(self.screen, (0, 0, 255), p, 1)

        draw_fps(self.screen, self.clock, (10, 10))

        pg.display.flip()
