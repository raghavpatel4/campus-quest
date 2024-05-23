# utils.py
import pygame as pg


def draw_text(screen, text, size, color, pos):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=pos)

    screen.blit(text_surface, text_rect)


def draw_fps(screen, clock, pos):
    # Display the current FPS in the top left corner
    # Color code the FPS display based on the current FPS
    if clock.get_fps() >= 45:
        draw_text(
            screen,
            'fps = {}'.format(round(clock.get_fps())),
            36,
            (0, 255, 0),
            (10, 10)
        )
    elif clock.get_fps() >= 30:
        draw_text(
            screen,
            'fps = {}'.format(round(clock.get_fps())),
            36,
            (255, 255, 0),
            (10, 10)
        )
    elif clock.get_fps() < 30:
        draw_text(
            screen,
            'fps = {}'.format(round(clock.get_fps())),
            36,
            (255, 0, 0),
            (10, 10)
        )

