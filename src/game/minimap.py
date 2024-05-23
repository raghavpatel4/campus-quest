import pygame as pg

from src.game.settings import TILE_SIZE
from src.game.world import World

MINIMAP_SIZE = 200

# Position minimap in top right corner
#MINIMAP_POS = (800, 10)


class Minimap:

    def __init__(self, screen, world):
        self.screen = screen
        self.world = world

    def draw_minimap(self):

        minimap_surface = pg.Surface((MINIMAP_SIZE, MINIMAP_SIZE))
        minimap_surface.fill((34, 139, 34))  # Fill with a grass-like color
        # rotate the minimap 90 degrees
        minimap_surface = pg.transform.rotate(minimap_surface, 180)

        # Calculate the scale of the minimap to the world - the entire cartesian grid should fit in the minimap
        scale_x = MINIMAP_SIZE / (self.world.grid_length_x * TILE_SIZE)
        scale_y = MINIMAP_SIZE / (self.world.grid_length_y * TILE_SIZE)

        grid_surface = pg.Surface((MINIMAP_SIZE, MINIMAP_SIZE), pg.SRCALPHA)

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                # Draw each tile on the minimap
                sq = self.world.world[x][y]["cartesian_rect"]
                rect = pg.Rect(sq[0][0] * scale_x, sq[0][1] * scale_y, TILE_SIZE * scale_x, TILE_SIZE * scale_y)
                # pg.draw.rect(grid_surface, (255, 255, 255, 128), rect, 1)  # Last value is the alpha (opacity)

                # Draw objects on the minimap
                tile = self.world.world[x][y]["tile"]
                if tile != "":
                    if tile == "tree":
                        object_color = (0, 100, 0)  # Dark green for trees
                    elif tile == "rock" or tile == "rock2":
                        object_color = (150, 75, 0)  # Brown for rocks
                    elif tile == "puddle":
                        object_color = (0, 0, 255)  # blue for water
                    else:
                        object_color = (255, 255, 255)  # Default to white

                    pg.draw.rect(minimap_surface, object_color, rect)

        # Draw the semi-transparent grid on top of the minimap
        grid_surface = pg.Surface((MINIMAP_SIZE, MINIMAP_SIZE), pg.SRCALPHA)
        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):
                sq = self.world.world[x][y]["cartesian_rect"]
                rect = pg.Rect(sq[0][0] * scale_x, sq[0][1] * scale_y, TILE_SIZE * scale_x, TILE_SIZE * scale_y)
                pg.draw.rect(grid_surface, (255, 255, 255, 16), rect, 1)  # Alpha set to 128 for 50% opacity

        # Blit the semi-transparent grid surface onto the minimap surface
        minimap_surface.blit(grid_surface, (0, 0))

        self.screen.blit(minimap_surface, (self.world.width * 0.84, self.world.height * 0.05))
