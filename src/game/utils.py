# utils.py
import pygame as pg


def draw_text(screen, text, size, color, pos):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=pos)

    screen.blit(text_surface, text_rect)


def draw_fps(screen, clock, pos):
    draw_text(
        screen,
        'fps = {}'.format(round(clock.get_fps())),
        36,
        (255, 255, 255),
        (10, 10)
    )
